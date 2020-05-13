import requests
import urllib3

from model.CoinAsset import CoinAsset
import utility.Constant as Constant


class CoinRestService:
    def getCoin(self, base, quote):

        resp = requests.get(Constant.historicalAPI+'/{}/{}/latest?period_id=2YRS'.format(base, quote),
                            headers=
                            {
                                'Content-Type': 'application/json',
                                'X-CoinAPI-Key': '28A88AD6-15A7-458C-BA71-0B9AD731BCB0',
                            }
                            )

        if resp.status_code != 200:
            # This means something went wrong.
            raise format(resp.status_code)
        else:
            # print("got values  "+ resp.json())
            return resp

    def getAssets(self):
        resp = requests.get(Constant.allAssetsAPI,
                    headers=
                        {
                            'Content-Type': 'application/json',
                            'X-CoinAPI-Key': '28A88AD6-15A7-458C-BA71-0B9AD731BCB0',
                        }
                    )
        if resp.status_code != 200:
            raise format(resp.status_code)
        else:
            assets = []

            name = None
            type_is_crypto = None
            data_start = None
            data_end = None
            data_quote_start = None
            data_quote_end = None
            data_orderbook_start = None
            data_orderbook_end = None
            data_trade_start = None
            data_trade_end = None
            data_symbols_count = None
            volume_1hrs_usd = None,
            volume_1day_usd = None
            volume_1mth_usd = None
            price_usd = None

            for asset in resp.json():
                #print('-----------------///--------------')
                asset_id = asset['asset_id']

                if 'name' in asset:
                    name = asset['name']
                if 'type_is_crypto' in asset:
                    type_is_crypto = asset['type_is_crypto']
                if 'data_end' in asset:
                    data_end = asset['data_end']
                if 'data_start' in asset:
                    data_start = asset['data_start']
                if 'data_quote_start' in asset:
                    data_quote_start = asset['data_quote_start']
                if 'data_quote_end' in asset:
                    data_quote_end = asset['data_quote_end']
                if 'data_orderbook_start' in asset:
                    data_orderbook_start =asset['data_orderbook_start']
                if 'data_orderbook_end' in asset:
                    data_orderbook_end = asset['data_orderbook_end']
                if 'data_trade_start' in asset:
                    data_trade_start = asset['data_trade_start']
                if 'data_trade_end' in asset:
                    data_trade_end = asset['data_trade_end']
                if 'data_symbols_count' in asset:
                    data_symbols_count = asset['data_symbols_count']
                if 'volume_1hrs_usd' in asset:
                    volume_1hrs_usd = asset['volume_1hrs_usd']
                if 'volume_1day_usd' in asset:
                    volume_1day_usd = asset['volume_1day_usd']
                if 'volume_1mth_usd' in asset:
                    volume_1mth_usd = asset['volume_1mth_usd']
                if 'price_usd' in asset:
                    price_usd = asset['price_usd']

                c = CoinAsset(asset_id, name, type_is_crypto, data_start,
                 data_end, data_quote_start, data_quote_end, data_orderbook_start, data_orderbook_end,
                 data_trade_start, data_trade_end, data_symbols_count, volume_1hrs_usd,
                 volume_1day_usd,volume_1mth_usd, price_usd)

                assets.append(c)

        return assets


#c = CoinRestService()

#c.getAssets()