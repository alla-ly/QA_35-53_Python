books = {
    'Harry Potter':'J.K.Rowling',
    'To kill a mockingbird':'Harper Lee'
}

books1 = {
    'Harry Potter',
    'To kill a mockingbird'
}
print(books1)

response = {
    'status':'success',
     'user':{"id":1, 'name':'Maria'}
}

print(response['user']['name'])

#isinstans - принадлежит ли обьект опред.типу

data = [1,22,3]
print(isinstance(data,list))

value = 10
print(isinstance(value,(int,float)))
print(type(value))

#клас Дикт-кийс dict_keys
team_ages = {
    "Alex":23,
    "Viki":42,
    "Petr":52,
    "Den":32,
    "Olga":26
}
print(team_ages.keys())
print(team_ages.values())

#Zip преобразуэт срисок в кортежи
team_names = ["Alex","Viki","Petr","Den","Olga"]
team_numbers = [23,43,25,52,32]
team_ages = {name:age for name, age in zip(team_names,team_numbers)}
print(team_ages)



























