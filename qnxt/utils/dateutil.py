from datetime import datetime, date
from typing import Union


def dateformat(as_of: Union[date, datetime, str]):
    """Pass either a datetime/date object or a string in ISO format to set the class' asOfDate parameter.
    This parameter only affects the get_details method"""
    if isinstance(as_of, datetime):
        as_of = as_of.date().strftime(fmt='%Y-%m-%d')
    elif isinstance(as_of, date):
        as_of = as_of.strftime(fmt='%Y-%m-%d')

    return as_of
