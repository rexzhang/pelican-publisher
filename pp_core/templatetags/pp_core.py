from django import template


def pp_date(value):
    if value is None:
        return "-"

    return value.strftime("%Y-%m-%d %H:%S %Z")


register = template.Library()
register.filter("pp_date", pp_date)
