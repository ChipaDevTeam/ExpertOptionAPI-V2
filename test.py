import asyncio
from ExpertOptionApiV2.stable_api import ExpertOptionApiV2

TOKEN = "6c4bbfd4640b9b46ee145650e331b030"

async def main():
    api = ExpertOptionApiV2(TOKEN, server_region="wss://fr24g1eu.expertoption.finance/ws/v40")
    await api.connect()

    print(api.GetSingleCandles())

if __name__ == '__main__':
    asyncio.run(main())
