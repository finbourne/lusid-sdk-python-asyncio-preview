import unittest
import uuid

import asynctest
import lusid_asyncio as lusid
import lusid_asyncio.models as models
from lusid_asyncio import OrderRequest
from lusid_asyncio import OrderSetRequest
from lusid_asyncio import PerpetualProperty
from lusid_asyncio import PropertyValue
from lusid_asyncio import ResourceId
from lusidfeature import lusid_feature
from tests.utilities import InstrumentLoader
from tests.utilities import TestDataUtilities
import json


class Orders(asynctest.TestCase):
    use_default_loop = True

    tests_scope = {'simple-upsert': 'Orders-SimpleUpsert-TestScope'}
    test_codes = ['TIF', 'OrderBook', 'PortfolioManager', 'Account', 'Strategy']

    @staticmethod
    async def load_properties(api_client, scopes, codes):
        for scope in scopes:
            for code in codes:
                try:
                    await lusid.PropertyDefinitionsApi(api_client).create_property_definition(
                        create_property_definition_request=models.CreatePropertyDefinitionRequest(
                            domain="Order",
                            scope=scope,
                            code=code,
                            display_name=code,
                            constraint_style="Property",
                            data_type_id=lusid.ResourceId(scope="system", code="string"),
                        )
                    )
                except lusid.ApiException as e:
                    if json.loads(e.body)["name"] == "PropertyAlreadyExists":
                        pass # ignore if the property definition exists

    async def setUp(cls):
        # create a configured API client
        api_client = TestDataUtilities.api_client()
        cls.orders_api = lusid.OrdersApi(api_client)
        cls.instruments_api = lusid.InstrumentsApi(api_client)
        instrument_loader = InstrumentLoader(cls.instruments_api)
        cls.instrument_ids = await instrument_loader.load_instruments()
        await cls.load_properties(api_client=api_client, scopes=cls.tests_scope.values(), codes=cls.test_codes)

    @lusid_feature("F4")
    async def test_upsert_simple_order(self):
        """Makes a request for a single order."""

        orders_scope = self.tests_scope['simple-upsert']
        # Create unique order id
        order_id = str(uuid.uuid4())

        # Construct order arguments
        instrument_identifiers = {TestDataUtilities.lusid_luid_identifier: self.instrument_ids[0]}
        ##Create ResourceId for order
        order_resource_id = models.ResourceId(orders_scope, order_id)
        portfolio_id = ResourceId(orders_scope, "OrdersTestPortfolio")
        properties = {f"Order/{orders_scope}/TIF": PerpetualProperty(f"Order/{orders_scope}/TIF", PropertyValue("GTC")),
                      f"Order/{orders_scope}/OrderBook":
                          PerpetualProperty(f"Order/{orders_scope}/OrderBook", PropertyValue("UK Test Orders")),
                      f"Order/{orders_scope}/PortfolioManager":
                          PerpetualProperty(f"Order/{orders_scope}/PortfolioManager", PropertyValue("F Bar")),
                      f"Order/{orders_scope}/Account":
                          PerpetualProperty(f"Order/{orders_scope}/Account", PropertyValue("J Wilson")),
                      f"Order/{orders_scope}/Strategy":
                          PerpetualProperty(f"Order/{orders_scope}/Strategy", PropertyValue("RiskArb"))}

        quantity = 100
        # Construct request
        order_request = OrderRequest(properties=properties,
                                     instrument_identifiers=instrument_identifiers,
                                     quantity=quantity, side='buy',
                                     portfolio_id=portfolio_id, id=order_resource_id)

        order_set_request = OrderSetRequest(order_requests=[order_request])

        upsert_result = await self.orders_api.upsert_orders(order_set_request=order_set_request)

        self.assertEqual(len(upsert_result.values),1)
        response=upsert_result.values[0].to_dict()
        self.assertEqual(response['id']['code'], order_id)
        self.assertEqual(response['lusid_instrument_id'], self.instrument_ids[0])
        self.assertEqual(response['quantity'], 100)
        self.assertEqual(response['properties'][f"Order/{orders_scope}/TIF"]['key'] , f"Order/{orders_scope}/TIF")