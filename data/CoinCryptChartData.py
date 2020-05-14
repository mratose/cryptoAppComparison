import psycopg2
import utility.Constant as Constant


def get_drop_down_data():
    try:
        connection = psycopg2.connect(user=Constant.username,
                                      password=Constant.password,
                                      host=Constant.host,
                                      port=Constant.port,
                                      database=Constant.database)
        cursor = connection.cursor()
        select_query = "select asset_id from public.at_all_currencies " \
                       "where asset_id in ('BTC', 'ETH', 'XRP', 'LTC') "

        cursor.execute(select_query)
        print("Selecting çrytocurrency from all_assets")

        row = cursor.fetchall()
        all_assets = []
        for rows in row:
            all_assets.append(rows[0])
        return all_assets
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def get_chart_details(base_crypto):
    try:
        connection = psycopg2.connect(user=Constant.username,
                                      password=Constant.password,
                                      host=Constant.host,
                                      port=Constant.port,
                                      database=Constant.database)
        cursor = connection.cursor()

        select_query = "select asset_id, name, data_start,data_end" \
                       ", price_usd," \
                       "time_period_end, price_open," \
                       "price_high, price_low, price_close, volume_traded" \
                       ", trades_count, quotes " \
                       "from avw_chart_details " \
                       "where asset_id = %s "

        cursor.execute(select_query, (base_crypto,))
        print("Selecting chart details using cursor.fetchall")

        row = cursor.fetchall()
        all_assets = []
        for asset in row:
            print(asset)
            all_assets.append(asset[:])
        return all_assets
    except (Exception, psycopg2.Error) as error:
        print("Error while fetching data from PostgreSQL", error)

    finally:
        # closing database connection.
        if (connection):
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")
