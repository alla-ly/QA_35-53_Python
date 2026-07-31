# 1-9 |10-99| 200-299
import re
print("1***************")
IS_POSITIVE_LESS_THAN_PATTERN = r"[1-9]|[1-9][0-9]|[12][0-9]{2}"
                    # pattern = r"^([1-9]|[1-9]\d|[12]\d\d)$"

def is_positive_less_than_300(value):
    return bool(re.search(IS_POSITIVE_LESS_THAN_PATTERN, value))

print(is_positive_less_than_300("1"))
print(is_positive_less_than_300("15"))
print(is_positive_less_than_300("99"))
print(is_positive_less_than_300("100"))
print(is_positive_less_than_300("299"))

print(is_positive_less_than_300("0"))
print(is_positive_less_than_300("300"))
print(is_positive_less_than_300("-5"))
print(is_positive_less_than_300("3.14"))
print(is_positive_less_than_300("abc"))
print("2***************")

# 1-99 |100-199| 200-249| 250-255
IS_NUMBER_FROM_1_TO_255_PATTERN = r"([1-9][0-9]?|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
                                # r"^([1-9]|[1-9]\d|1\d\d|2[0-4]\d|25[0-5])$"
def is_number_from_1_to_255(value):
    return bool(re.match(IS_NUMBER_FROM_1_TO_255_PATTERN, value))

print(is_number_from_1_to_255("1"))
print(is_number_from_1_to_255("255"))
print(is_number_from_1_to_255("100"))
print(is_number_from_1_to_255("0"))
print(is_number_from_1_to_255("256"))
print(is_number_from_1_to_255("025"))
print(is_number_from_1_to_255("-1"))
print(is_number_from_1_to_255("2.5"))
print("3***************")

IS_ISRAEL_MOBILE_PATTERN = r"(0|\+972)5[0-9](-?\d){7}"
                       # r"^(?:\+972-?|0)5[0-9](?:-?\d){7}$"

def is_israel_mobile(phone):
    return bool(re.fullmatch(IS_ISRAEL_MOBILE_PATTERN, phone))

print(is_israel_mobile("0541234567"))
print(is_israel_mobile("054-1234567"))
print(is_israel_mobile("+97254-123-4567"))
print(is_israel_mobile("058-12-34-567"))

print(is_israel_mobile("54-1234567"))
print(is_israel_mobile("054--12-4567"))
print(is_israel_mobile("+972054-123-4567"))
print(is_israel_mobile("97254-123-4567"))
print("4***************")
#00:00-23:59

IS_VALID_TIME_PATTERN = r"([0-9][0-9]|2[0-3]):([0-5][0-9])$"
                    # r"^(?:[01]\d|2[0-3]):[0-5]\d$"

def is_valid_time(time):
    return bool(re.fullmatch(IS_VALID_TIME_PATTERN, time))

print(is_valid_time("00:00"))
print(is_valid_time("09:30"))
print(is_valid_time("14:45"))
print(is_valid_time("23:59"))

print(is_valid_time("24:00"))
print(is_valid_time("12:60"))
print(is_valid_time("123:45"))
print(is_valid_time("12-30"))
print("5***************")

IS_ISRAEL_CAR_NUMBER_PATTERN = r"\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3}"
                        # r"^(?:\d{2}-\d{3}-\d{2}|\d{3}-\d{2}-\d{3})$
def is_israel_car_number(number):
    return bool(re.fullmatch(IS_ISRAEL_CAR_NUMBER_PATTERN, number))

print(is_israel_car_number("12-345-67"))
print(is_israel_car_number("99-999-99"))
print(is_israel_car_number("123-45-678"))
print(is_israel_car_number("456-78-901"))

print(is_israel_car_number("12345678"))
print(is_israel_car_number("12:345:67"))
print(is_israel_car_number("1-234-56"))
print(is_israel_car_number("1234-56-78"))