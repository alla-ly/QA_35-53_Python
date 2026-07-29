import re


def has_digit(password):
    return bool(re.search(r"\d", password))

print(has_digit("qwerty"))
print(has_digit("Qwerty123"))
print()

# *-0 или более раз
print(re.search(r"ab*c","ac"))
print(re.search(r"ab*c","abc"))
print(re.search(r"ab*c","abbbbbc"))

# +- 1 или более раз
print(re.search(r"ab+c","ac"))
print(re.search(r"ab+c","abc"))
print(re.search(r"ab+c","abbbbbc"))

# ? - 0 либо 1 раз
print(re.search(r"colou?r", "color"))
print(re.search(r"colou?r", "colour"))
print(re.search(r"colou?r", "colouur"))

#{} - точное количество  - квантификатор
print(re.search(r"\d{3}", "12"))
print(re.search(r"\d{3}", "1566562"))
print()

# от 2 до 4 должно быть в строке
print(re.search(r"\d{2,4}", "1s23a456"))
print(re.search(r"\d{2,4}", "1"))