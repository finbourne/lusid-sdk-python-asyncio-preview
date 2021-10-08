from collections import namedtuple

import lusid_asyncio as lusid
import lusid_asyncio.models as models


class InstrumentLoader:
    __InstrumentSpec = namedtuple("InstrumentSpec", ["Figi", "Name"])

    __instruments = [
        __InstrumentSpec("BBG000FD8G46", "HISCOX LTD"),
        __InstrumentSpec("BBG000DW76R4", "ITV PLC"),
        __InstrumentSpec("BBG000PQKVN8", "MONDI PLC"),
        __InstrumentSpec("BBG000BDWPY0", "NEXT PLC"),
        __InstrumentSpec("BBG000BF46Y8", "TESCO PLC")
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
