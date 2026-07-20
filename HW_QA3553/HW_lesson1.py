#1
def print_string_reverse(s):
    if s is None or s == "" or s.isspace():
        print("Wrong string")
    else:
        reversed_string = s[::-1]
        print(reversed_string)

print_string_reverse('Good morning!')

#2
def is_isr_phone_number(phone):
    if phone is None:
        return None
    phone = phone.strip()

    if phone == "":
        return None

    if len(phone) == 10 and phone[0] == '0' and phone.isdigit():
        return True
    else:
        return False

print(is_isr_phone_number("0521234567"))
print(is_isr_phone_number("521234567"))
print(is_isr_phone_number("05212345a7"))
print(is_isr_phone_number(""))
print(is_isr_phone_number("   "))
print(is_isr_phone_number(None))

#3
def print_substring_reverse(s, start, finish):
    if s is None:
        print("Wrong args")
        return
    s = s.strip()
    if s == "":
        print("Wrong args")
        return
    if start < 0 or finish >= len(s) or start > finish:
        print("Wrong args")
        return

    left = s[:start]
    middle = s[start:finish+1][::-1]
    right = s[finish+1:]

    result = left + middle + right
    print(result)

print_substring_reverse("Shalom", 1, 3)
print_substring_reverse("", 1, 3)
print_substring_reverse("abc", 5, 6)
print_substring_reverse("abc", 2, 1)
print_substring_reverse(None, 0, 1)

#4
def get_words_reverse(s):
    if not s or s.strip() == "":
        return None
    return " ".join(s.split()[::-1])

print(get_words_reverse("Hello my nice world"))
print(get_words_reverse(""))
print(get_words_reverse("   "))
print(get_words_reverse(None))