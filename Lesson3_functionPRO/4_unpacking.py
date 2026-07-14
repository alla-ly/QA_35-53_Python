def login(username,password):
    print(username,password)

data = ["admin","12345"]
login(data[0],data[1])

login(*data)

user = {
    "username":"admin",
    "password":"12345"
}
login(**user)

# user = { - сколько функция приняла, столько и полей. Здесь 2 функции и 3 поля -ОШИБКА!!
#     "username": "admin",
#     "password": "12345",
#     "remember_me":True
# }
#
# login(**user)



