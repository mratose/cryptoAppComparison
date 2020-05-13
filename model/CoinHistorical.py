class CoinHistorical:
    def __init__(self, time_period_start, time_period_end,time_open,time_close,
                 price_open, price_high,price_close,volume_traded,trades_count):
        self.time_period_start = time_period_start
        self.time_period_end = time_period_end
        self.time_open = time_open
        self.time_close = time_close
        self.price_open = price_open
        self.price_high = price_high
        self.price_close = price_close
        self.volume_traded = volume_traded
        self.trades_count = trades_count


