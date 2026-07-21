# with open("user.json", "r", encoding="utf-8") as file:
#     print(file.read)

#ошибка - когда неправильно написан КОД
#исключительная ситуация - не нашелся код и т.д

#exceptions:
# print("START PROGRAM")
# result1 = 10/0
# print(result1)
# print("END PROGRAM")

#  Traceback ТРЕЙС БЕК - красные строки в консоли - ошибка!!!
# читается снизу вверх

def div_int(a,b):
    return a/b
print("START PROGRAM")
res = div_int(10,0)
print(res)
print("END PROGRAM")
