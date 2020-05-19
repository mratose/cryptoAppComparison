class CoinAsset:
    def __init__(self, asset_id, name, type_is_crypto, data_start,
                 data_end, data_quote_start, data_quote_end, data_orderbook_start, data_orderbook_end,
                 data_trade_start, data_trade_end, data_symbols_count, volume_1hrs_usd,
                 volume_1day_usd, volume_1mth_usd, price_usd):

        self.asset_id = asset_id
        self.name = name
        self.type_is_crypto = type_is_crypto
        self.data_start = data_start
        self.data_end = data_end
        self.data_quote_start = data_quote_start
        self.data_quote_end = data_quote_end
        self.data_orderbook_start = data_orderbook_start
        self.data_orderbook_end = data_orderbook_end
        self.data_trade_start = data_trade_start
        self.data_trade_end = data_trade_end
        self.data_symbols_count = data_symbols_count
        self.volume_1hrs_usd = volume_1hrs_usd
        self.volume_1day_usd = volume_1day_usd
        self.volume_1mth_usd = volume_1mth_usd
        self.price_usd = price_usd


