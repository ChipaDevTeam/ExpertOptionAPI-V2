import asyncio
from ExpertOptionApiV2.stable_api import ExpertOptionApiV2

TOKEN = "6c4bbfd4640b9b46ee145650e331b030"

async def main():
    api = ExpertOptionApiV2(TOKEN, server_region="wss://fr24g1eu.expertoption.finance/ws/v40")
    await api.connect()

    #print(await api.GetBalance()) # ✅ works!
    print(await api.PlaceOrder(amount=1, type="call", assetid=240, exptime=60, isdemo=1)) # ❌ Does not work
    # print(await api.GetSingleCandles()) # ✅ works!

if __name__ == '__main__':
    asyncio.run(main())
