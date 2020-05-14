import psycopg2

from services.CoinRestService import CoinRestService
import utility.Constant as Constant


class CoinCryptData:

    def addcoinhistory(self, resp, base, quote):
        try:
            connection = psycopg2.connect(
                database=Constant.database,
                user=Constant.username,
                password=Constant.password,
                host=Constant.host,
                port=Constant.port

            )
            cursor = connection.cursor()
            cointIemParams = []

            query = "INSERT INTO at_ohlcv_history (" \
                    "time_period_start, time_period_end," \
                    "time_open, time_close,price_open," \
                    "price_high,price_low,price_close," \
                    "volume_traded,trades_count" \
                    ",base,quotes) " \
                    "VALUES (%s, %s, %s,%s, %s, %s,%s,%s, %s, %s, %s, %s)"

            for coinItem in resp.json():
                cointIemParams.append(
                    (
                        coinItem['time_period_start'],
                        coinItem['time_period_end'],
                        coinItem['time_open'],
                        coinItem['time_close'],
                        coinItem['price_open'],
                        coinItem['price_high'],
                        coinItem['price_low'],
                        coinItem['price_close'],
                        coinItem['volume_traded'],
                        coinItem['trades_count'],
                        base,
                        quote
                    )
                )

            if len(cointIemParams) > 0:
                cursor.executemany(query, cointIemParams)
                connection.commit()
                print(str.format("Done inserting {}", len(cointIemParams)))
            else:
                print("no data to insert")
        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)
        finally:
            if(connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")

    def getallcrypt(self):
        try:
            connection = psycopg2.connect(
                database=Constant.database,
                user=Constant.username,
                password=Constant.password,
                host=Constant.host,
                port=Constant.port
            )

            cursor = connection.cursor()
            cursor.execute("select asset_id from at_all_currencies")
            count = cursor.rowcount

            if count > 0:
                return cursor.fetchall()
            else:
                coinRestService = CoinRestService()
                cointAssests = coinRestService.getassets()
                cointAssetsParam = []
                for asset in cointAssests:
                    cointAssetsParam.append((
                        asset.asset_id,
                        asset.name,
                        asset.type_is_crypto,
                        asset.data_start,
                        asset.data_end,
                        asset.data_quote_start,
                        asset.data_quote_end,
                        asset.data_orderbook_start,
                        asset.data_orderbook_end,
                        asset.data_symbols_count,
                        asset.volume_1hrs_usd,
                        asset.volume_1day_usd,
                        asset.volume_1mth_usd,
                        asset.price_usd,
                    ))

                insert = "INSERT INTO public.at_all_currencies " \
                         "(asset_id, name, type_is_crypto, data_start" \
                         ", data_end, data_quote_start, " \
                         "data_quote_end,"\
                         "data_orderbook_start,"\
                         "data_orderbook_end, data_symbols_count" \
                         ", volume_1hrs_usd, volume_1day_usd, " \
                         "volume_1mth_usd, price_usd)"\
                         "VALUES (%s, %s, %s, %s, %s," \
                         " %s, %s, %s," \
                         " %s, %s, %s, %s, %s, %s)"

                print("======starting======")
                cursor.executemany(insert, cointAssetsParam)
                connection.commit()
                print("======done ====")
                return cursor.execute("select asset_id from at_all_currencies")

        except (Exception, psycopg2.Error) as error:
            print("Error while connecting to PostgreSQL", error)

        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")
