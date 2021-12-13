import asyncio
import logging
from datetime import datetime

import asynctest
import pytz
from lusidfeature import lusid_feature

import lusid_asyncio as lusid
import lusid_asyncio.models as models
from lusid_asyncio import ApiException
from tests.utilities import InstrumentLoader
from tests.utilities import TestDataUtilities, IdGenerator


class ReferencePortfolio(asynctest.TestCase):
    use_default_loop = True

    @classmethod
    def setUpClass(cls):

        # Log any exceptions
        cls.logger = logging.getLogger()
        cls.logger.setLevel(logging.INFO)

        # Create API client
        api_client = TestDataUtilities.api_client()

        # Instantiate APIs we will use
        cls.reference_portfolio_api = lusid.ReferencePortfolioApi(api_client)
        cls.portfolios_api = lusid.PortfoliosApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)

        # Load instruments
        cls.instrument_loader = InstrumentLoader(cls.instruments_api)

        loop = asyncio.get_event_loop()
        cls.instrument_ids = loop.run_until_complete(cls.instrument_loader.load_instruments())

        cls.id_generator = IdGenerator(scope=TestDataUtilities.tutorials_scope)

    @classmethod
    def tearDownClass(cls):
        loop = asyncio.get_event_loop()
        for _, scope, code in cls.id_generator.pop_scope_and_codes():
            try:
                loop.run_until_complete(cls.portfolios_api.delete_portfolio(scope, code))
            except ApiException as ex:
                print(ex)

    @lusid_feature("F39")
    async def test_create_reference_portfolio(self):

        _, _, portfolio_code = self.id_generator.generate_scope_and_code("portfolio")
        f39_reference_portfolio_name = "F39p_Reference Portfolio Name"

        # Details of the new reference portfolio to be created
        request = models.CreateReferencePortfolioRequest(
            display_name=f39_reference_portfolio_name,
            code=portfolio_code,
        )

        # Create the reference portfolio in LUSID in the tutorials scope
        result = await self.reference_portfolio_api.create_reference_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_reference_portfolio_request=request,
        )

        self.assertEqual(result.id.code, request.code)

    @lusid_feature("F40")
    async def test_upsert_reference_portfolio_constituents(self):

        constituent_weights = [10, 20, 30, 15, 25]
        effective_date = datetime(year=2021, month=3, day=29, tzinfo=pytz.UTC)

        _, _, portfolio_code = self.id_generator.generate_scope_and_code("portfolio")
        f40_reference_portfolio_name = "F40p_Reference Portfolio Name"

        # Create a new reference portfolio
        request = models.CreateReferencePortfolioRequest(
            display_name=f40_reference_portfolio_name,
            code=portfolio_code,
            created=effective_date,
        )

        await self.reference_portfolio_api.create_reference_portfolio(
            scope=TestDataUtilities.tutorials_scope,
            create_reference_portfolio_request=request,
        )

        # Check that all instruments were created successfully
        self.assertEqual(len(constituent_weights), len(self.instrument_ids))

        # Create the constituent requests
        individual_constituent_requests = [
            models.ReferencePortfolioConstituentRequest(
                instrument_identifiers={
                    TestDataUtilities.lusid_luid_identifier: instrument_id
                },
                weight=constituent_weight,
                currency="GBP",
            )
            for instrument_id, constituent_weight in zip(
                self.instrument_ids, constituent_weights
            )
        ]

        # Create a bulk constituent upsert request
        bulk_constituent_request = models.UpsertReferencePortfolioConstituentsRequest(
            effective_from=effective_date,
            weight_type="Static",
            constituents=individual_constituent_requests,
        )

        # Make the upsert request via the reference portfolio API
        await self.reference_portfolio_api.upsert_reference_portfolio_constituents(
            scope=TestDataUtilities.tutorials_scope,
            code=portfolio_code,
            upsert_reference_portfolio_constituents_request=bulk_constituent_request,
        )

        # Get reference portfolio holdings
        constituent_holdings = (
            await self.reference_portfolio_api.get_reference_portfolio_constituents(
                scope=TestDataUtilities.tutorials_scope,
                code=portfolio_code,
            )
        )

        # Validate count of holdings
        self.assertEqual(len(constituent_holdings.constituents), 5)

        # Validate instruments on holdings
        for constituent, upserted_instrument in zip(
                constituent_holdings.constituents, self.instrument_ids
        ):
            self.assertEqual(constituent.instrument_uid, upserted_instrument)

        # Validate holding weights
        for constituent, weight in zip(
                constituent_holdings.constituents, constituent_weights
        ):
            self.assertEqual(constituent.weight, weight)