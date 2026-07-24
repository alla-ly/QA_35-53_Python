class Dog:
    def __init__(self, name):
        self.name = name #атрибут - имя

    def bark(self): # метод действия - поведение
        return f"{self.name} says:Woof!"

    def sleep(self): # состояния поведения
        return f"{self.name} is sleeping"

dog1 = Dog("Rex") #обьект строим на базе класса
dog2 = Dog("Max")

print(dog1.bark())
print(dog2.sleep())