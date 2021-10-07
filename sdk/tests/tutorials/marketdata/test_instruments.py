import unittest

import asynctest
import lusid_asyncio as lusid
import lusid_asyncio.models as models
from lusidfeature import lusid_feature
from lusid_asyncio.exceptions import ApiException
from tests.utilities import TestDataUtilities


class Instruments(asynctest.TestCase):
    property_definitions_api = None
    use_default_loop = True

    def setUp(self):
        # create a configured API client
        api_client = TestDataUtilities.api_client()

        self.instruments_api = lusid.InstrumentsApi(api_client)
        self.property_definitions_api = lusid.PropertyDefinitionsApi(api_client)

    @classmethod
    async def ensure_property_definition(cls, code):

        try:
            await cls.property_definitions_api.get_property_definition(
                domain="Instrument",
                scope=TestDataUtilities.tutorials_scope,
                code=code
            )
        except ApiException as e:
            # property definition doesn't exist (returns 404), so create one
            property_definition = models.CreatePropertyDefinitionRequest(
                domain="Instrument",
                scope=TestDataUtilities.tutorials_scope,
                life_time="Perpetual",
                code=code,
                value_required=False,
                data_type_id=models.ResourceId("system", "string")
            )

            # create the property
            await cls.property_definitions_api.create_property_definition(definition=property_definition)

    @lusid_feature("F41")
    async def test_seed_instrument_master(self):
        response = await self.instruments_api.upsert_instruments(request_body={

            "BBG005SZG253": models.InstrumentDefinition(
                name="AB DYNAMICS PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG005SZG253"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_1_example3")
                }
            ),

            "BBG00J50FHL5": models.InstrumentDefinition(
                name="BOKU INC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG00J50FHL5"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_2_example3")
                }
            ),

            "BBG001LSHYT8": models.InstrumentDefinition(
                name="DOTDIGITAL GROUP PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG001LSHYT8"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_3_example3")
                }
            ),

            "BBG00YG2ZBC7": models.InstrumentDefinition(
                name="INSPIRE FAITHWARD LARCAP MOM",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG00YG2ZBC7"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_4_example3")
                }
            ),

            "BBG000GRHJJ2": models.InstrumentDefinition(
                name="VOLEX PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value="BBG000GRHJJ2"),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_5_example3")
                }
            )
        })

        self.assertEqual(len(response.values), 5, response.failed)

    @lusid_feature("F22")
    async def test_lookup_instrument_by_unique_id(self):

        figi = "BBG005SZG253"

        # set up the instrument
        response = await self.instruments_api.upsert_instruments(request_body={
            figi: models.InstrumentDefinition(
                name="AB DYNAMICS PLC",
                identifiers={
                    "Figi": models.InstrumentIdValue(value=figi),
                    "ClientInternal": models.InstrumentIdValue(value="internal_id_1_example3")
                }
            )
        })
        self.assertEqual(len(response.values), 1, response.failed)

        # look up an instrument that already exists in the instrument master by a
        # unique id, in this case an OpenFigi, and also return a list of aliases
        looked_up_instruments = await self.instruments_api.get_instruments(identifier_type="Figi",
                                                                     request_body=[figi],
                                                                     property_keys=[
                                                                         "Instrument/default/ClientInternal"
                                                                     ])

        self.assertTrue(figi in looked_up_instruments.values, msg=f"cannot find {figi}")

        instrument = looked_up_instruments.values[figi]
        self.assertTrue(instrument.name, "AB DYNAMICS PLC")

        property = next(filter(lambda i: i.key == "Instrument/default/ClientInternal", instrument.properties), None)
        self.assertTrue(property.value, "internal_id_1_example3")

    @lusid_feature("F23")
    async def test_list_available_identifiers(self):

        identifiers = await self.instruments_api.get_instrument_identifier_types()
        self.assertGreater(len(identifiers.values), 0)

    @lusid_feature("F24")
    async def test_list_all_instruments(self):

        page_size = 5

        # list the instruments, restricting the number that are returned
        instruments = await self.instruments_api.list_instruments(limit=page_size)

        self.assertLessEqual(len(instruments.values), page_size)

    @lusid_feature("F25")
    async def test_list_instruments_by_identifier_type(self):

        figis = ["BBG005SZG253", "BBG00J50FHL5", "BBG001LSHYT8"]

        # get a set of instruments querying by FIGIs
        instruments = await self.instruments_api.get_instruments(identifier_type="Figi", request_body=figis)

        for figi in figis:
            self.assertTrue(figi in instruments.values, msg=f"{figi} not returned")

    @lusid_feature("F26")
    async def test_edit_instrument_property(self):

        property_value = models.PropertyValue(label_value="Insurance")
        property_key = f"Instrument/{TestDataUtilities.tutorials_scope}/CustomSector"
        identifier_type = "Figi"
        identifier = "BBG005SZG253"

        # update the instrument
        await self.instruments_api.upsert_instruments_properties(upsert_instrument_property_request=[
            models.UpsertInstrumentPropertyRequest(
                identifier_type=identifier_type,
                identifier=identifier,
                properties=[models.ModelProperty(key=property_key, value=property_value)]
            )
        ])

        # get the instrument with value
        instrument = await self.instruments_api.get_instrument(
            identifier_type=identifier_type,
            identifier=identifier,
            property_keys=[property_key]
        )

        self.assertGreaterEqual(len(instrument.properties), 1)

        prop = list(
            filter(lambda p: p.key == property_key and p.value.label_value == property_value.label_value, instrument.properties))

        self.assertEqual(len(prop), 1, f"cannot find property key=${property_key} value={property_value}")

