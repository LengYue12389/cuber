from config import Config
from decimal import Decimal


def set_dnf_time(time):
    if time == Config.DNF_TIME:
        time = 'DNF '
    return time


def two_decimal(time):
    if time:
        return Decimal(time).quantize(Decimal("0.00"))
        # return round(time, 2)
