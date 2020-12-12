import time
from abc import ABCMeta

from rest_framework import serializers


def get_min_price(keys):
    return keys.saleprice


def get_price_order_product(val):
    return val.get('product_detail').saleprice * val.get('amount')


class TimestampField(serializers.Field, metaclass=ABCMeta):
    def to_representation(self, value):
        return int(time.mktime(value.timetuple()))
