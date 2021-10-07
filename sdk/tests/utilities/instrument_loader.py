from collections import namedtuple

import lusid_asyncio as lusid
import lusid_asyncio.models as models


class InstrumentLoader:
    __InstrumentSpec = namedtuple("InstrumentSpec", ["Figi", "Name"])

    __instruments = [
        __InstrumentSpec("BBG005SZG253", "AB DYNAMICS PLC"),
        __InstrumentSpec("BBG00J50FHL5", "BOKU INC"),
        __InstrumentSpec("BBG001LSHYT8", "DOTDIGITAL GROUP PLC"),
        __InstrumentSpec("BBG00YG2ZBC7", "INSPIRE FAITHWARD LARCAP MOM"),
        __InstrumentSpec("BBG000GRHJJ2", "VOLEX PLC")
    ]

    def __init__(self, instruments_api: lusid.InstrumentsApi):
        self.instruments_api = instruments_api

    async def load_instruments(self):
        instruments_to_create = {
            i.Figi: models.InstrumentDefinition(
                name=i.Name,
                identifiers={
                    "Figi": models.InstrumentIdValue(value=i.Figi)
                }
            ) for i in self.__instruments
        }

        response = await self.instruments_api.upsert_instruments(request_body=instruments_to_create)

        assert (len(response.failed) == 0), response.failed

        return sorted([i.lusid_instrument_id for i in response.values.values()])

    async def delete_instruments(self):
        for i in self.__instruments:
            await self.instruments_api.delete_instrument("Figi", i.Figi)
