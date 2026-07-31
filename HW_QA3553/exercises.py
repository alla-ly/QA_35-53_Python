import re

def is_valid_card_number(card):
    return bool(re.search(r"^(?:\d{4} \d{4} \d{4} \d{4}|\d{16})$", str(card).strip()))

print(is_valid_card_number("1234 5678 9101 1121"))
print(is_valid_card_number("1234567891011121"))
print(is_valid_card_number("0000 1111 2222 3333"))

print(is_valid_card_number("1234-5678-9101-1121"))
print(is_valid_card_number("1234 5678 9101"))
print(is_valid_card_number("12345 67891011121"))
print(is_valid_card_number("1234a567891011121"))
print("+"*15)

def is_valid_username(username):
    return bool(re.search(r"^[a-zA-Z]\w{3,15}$",str(username).strip()))

print(is_valid_username("alex_qa"))
print(is_valid_username("User123"))
print(is_valid_username("a_12"))

print(is_valid_username("123user"))
print(is_valid_username("_alex"))
print(is_valid_username("usr"))
print("3+++++++++++++++++++")

def is_valid_date(date):
    return bool(re.search(r"^(?:19|20)\d{2}-(?:0[1-9]|1[0-2])-(?:0[1-9]|[12]\d|3[01])$", str(date).strip()))

print(is_valid_date("2026-07-29"))
print(is_valid_date("1999-12-31"))
print(is_valid_date("2000-01-01"))

print(is_valid_date("2026-13-01"))
print(is_valid_date("2026-05-32"))
print(is_valid_date("2026-5-1"))
print("5******")

def is_valid_price(price):
    return bool(re.search(r"^(?:₪\s?|NIS\s?)?(?:[1-9]\d*|0)(?:\.\d{2})?(?:\s?₪|\s?NIS)?$", str(price).strip()))

print(is_valid_price("150"))
print(is_valid_price("15.90"))
print(is_valid_price("₪150"))
print(is_valid_price("150 ₪"))
print(is_valid_price("150 NIS"))

print(is_valid_price("015"))
print(is_valid_price("15.9"))
print(is_valid_price("15.999"))



