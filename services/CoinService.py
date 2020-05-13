from data.CoinCryptData import CoinCryptData
import psycopg2
from services.CoinRestService import CoinRestService

try:

    coinCryptData = CoinCryptData()
    coinRestService = CoinRestService()

    crypto = ['BTC', 'ETH', 'XRP', 'LTC']

    for currency in crypto:
        base = currency

        cryptsCursor = coinCryptData.getallcrypt()
        for crypt in cryptsCursor:
            quote = {crypt[0]}
            resp = coinRestService.getCoin(base, quote)
            coinCryptData.addcoinhistory(resp, base, quote)


except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
