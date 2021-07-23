from datetime import datetime


def unix_timestamp_seconds_to_datetime(unix_timestamp_seconds: float) -> datetime:
    """Return a datetime object from a unix timestamp"""
    return datetime.fromtimestamp(unix_timestamp_seconds)


def datetime_to_unix_timestamp_seconds(dt: datetime) -> float:
    """Return the unix timestamp in seconds from a datetime object."""
    return dt.timestamp()


def utc_str_to_datetime(utc_str: str) -> datetime:
    """Return a datetime object from the UTC datetime string."""
    return datetime.strptime(utc_str, '%Y-%m-%dT%H:%M:%S.%f%z')


def datetime_to_utc_str(dt: datetime) -> str:
    """Return a UTC datetime string from a datetime object."""
    return dt.strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'
