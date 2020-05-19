from data.CoinCryptData import CoinCryptData
import psycopg2
from services.CoinRestService import CoinRestService
import datetime
from datetime import timedelta
import asyncio


async def run_history_service(base, time_start):
    try:

        coinCryptData = CoinCryptData()
        coinRestService = CoinRestService()

        allassetcursor = coinCryptData.getallcrypt()
        for crypt in allassetcursor:
            quote = crypt[0]
            resp = coinRestService.gethistory(base, quote, time_start)
            if resp is None:
                raise Exception
            else:
                coinCryptData.addcoinhistory(resp, base, quote)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)


async def initialise_base():
    time_start = datetime.datetime.strptime('2016-01-01', "%Y-%m-%d")

    today = datetime.datetime.today()

    crypto = ['BTC', 'ETH', 'XRP', 'LTC']

    while time_start < today:

        time_start = time_start.isoformat()
        for currency in crypto:
            base = currency
            await run_history_service(base, time_start)

        time_start = datetime.datetime.strptime((time_start[0:10]), "%Y-%m-%d")
        time_start = time_start + timedelta(days=1)

loop = asyncio.get_event_loop()
tasks = [loop.create_task(initialise_base()), loop.create_task(initialise_base())]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

