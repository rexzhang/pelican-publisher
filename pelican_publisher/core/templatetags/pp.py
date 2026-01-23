from django import template
from django.utils.timezone import localtime


def _date(value, format: str) -> str:
    if value is None:
        return "-"

    return localtime(value).strftime(format)


def date_full(value):
    return _date(value, "%Y-%m-%d %H:%S %Z")


def date_long(value):
    return _date(value, "%Y-%m-%d %H:%S")


register = template.Library()
register.filter("date_full", date_full)
register.filter("date_long", date_long)
