#1
from HW_QA3553.HW_lesson6 import bicycle


class Employee:
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_into(self):
        return f"{self.name} works as {self.position} and {self.salary} "

employee1 = Employee("Anna", "QA Engineer", 7000)
employee2 = Employee("Bob", "Developer", 10000)

print(employee1.get_info())
print(employee2.get_info())

print()
#2
class Product():
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def buy(self, amount):
        if amount >self.quantity:
            return "Not enough products"
        self.quantity -= amount

laptop = Product("Laptop", 1200, 5)

print(laptop.buy(2))
print("Remaining balance after purchase 2 шт.:", laptop.quantity)
print(laptop.buy(10))
print("The balance has not changed.:", laptop.quantity)
print()

#3
class Vehicle():
    def move(self):
        return "Vehicle is moving"

class Car(Vehicle):
    def move(self):
        return "Car is driving!"

class Bicycle(Vehicle):
    def move(self):
        return "Bicycle is riding!"

vehicle = Vehicle()
car = Car()
bicycle = Bicycle()

print(vehicle.move())
print(car.move())
print(bicycle.move())
print()

#4
class User:
    country = "Israel"

    def __init__(self, username, age):
        self.username = username
        self.age = age

user1 = User("Inna", 38)
user2 = User("Tom", 25)
user3 = User("Kate", 28)

print(user1.country, user2.country, user3.country)

User.country = "Canada"
print(user1.country, user2.country, user3.country)




