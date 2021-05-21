from lib.candle_data import get_one_minute_candles_from_coinbase


def get_candle_data(
    currency_pair: str,
    start_utc_datetime: str,
    end_utc_datetime: str
):
    """Return one minute candles for the currency pair.

    This is the API handler for the /candles endpoint.

    start/end_utc_datetime should be ISO 8601 formatted datetime strings, for example
    2014-11-06T10:34:47.123456Z.
    """
