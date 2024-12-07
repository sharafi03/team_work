import re
from dataclasses import replace


def id_validator(id):
    if 0 <= id:
        return True
    else:
        return False


def price_validator(price):
    if 0 <= price:
        return True
    else:
        return False


def date_validator(date):
    date =date.replace("/", "-")
    date =date.replace(".", "-")
    if re.match(r'\d{4}-\d\d?-\d\d?', date):
        return True
    else:
        return False



def person_validator(person):
    if re.match(r'[a-zA-Z\s]{2,50}', person):
        return True
    else:
        return False
# def payment_validator(payment_type):
#     if ("receive"|"pay_back") in payment_type:
#         return True
#     else:
#         return False


