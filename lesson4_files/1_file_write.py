with open("greeting.txt","w",encoding="utf-8") as file:
    file.write("Hello, automated tests!\n")
    file.write("Second line")

#file = open(......) - было
#file.close()

# "r" -read - прочитать файл
# "w" -write - создает или полностью переписывает файл
# "a" - append - добавляет не стирая файл
# "r+" - read & write
# "rb", "wb" - pdf,screenshots

def log_test_result(test_name,status):
    with open("test_run.log", "a",encoding="utf-8") as log_file:
        log_file.write(f"{test_name}:{status}\n")

log_test_result("test_login","PASSED")
log_test_result("test_registration","FAILED")
log_test_result("test_logout","PASSED")

# МЕТОД ВЫЧИТАНИЯ
