# with open("user.json", "r", encoding="utf-8") as file:
#     print(file.read)

#ошибка - когда неправильно написан КОД
#исключительная ситуация - не нашелся код и т.д

#exceptions:

# print("START PROGRAM")
# result1 = 10/0
# print(result1)
# print("END PROGRAM")

#  Traceback ТРЕЙСБЕК - красные строки в консоли - ошибка!!!
# читается снизу вверх

# def div_int(a,b):
#     return a/b
# print("START PROGRAM")
# res = div_int(10,0)
# print(res)
# print("END PROGRAM")
print("****************")
# трай - try - помещается в потенциально опасный код
#  аксепт - exept -
print("START PROGRAM")
try:
    result = 10/0
    print(result)
except Exception as e:
    print("An error occurred: ",e)
print("END PROGRAM")
print("*********************")

print("START PROGRAM")
try:
    result = 10/2
    print(result)
except Exception as e:
    print("An error occurred: ",e)
print("END PROGRAM")
print()

def is_number(text):
    try:
        float(text)
        return True
    except (TypeError, ValueError):
        return False

print(is_number("314"))
print(is_number("3.14"))
print(is_number("3,14"))
print(is_number("Hello"))
print(is_number("None"))
print()

#else/finally
try:
    value = int("25")
except ValueError:
    print("The is not a number")
else:
    print("The transformation was successful: ", value)
finally:
    print("this block is always executed")
print()

try:
    value = int("fghfgh")
except ValueError:
    print("The is not a number")
else:
    print("The transformation was successful: ", value)
finally:
    print("this block is always executed")












