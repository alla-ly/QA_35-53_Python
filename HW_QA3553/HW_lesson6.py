##1
class Employee():
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary

    def get_info(self):
        return f"{self.name} works as {self.position} and earns {self.salary}"

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
        if self.quantity >= amount:
           self.quantity -= amount
        else:
            return "Not enough products"

laptop = Product("Laptop", 1500, 5)

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
class User():
    country = "Israel"

    def __init__(self, username, age):
        self.username = username
        self.age = age

    def get_info(self):
        return f"Name: {self.username} - {self.age} years old and lives in {self.country}"

user1 = User("Anna", 25)
user2 = User("David", 30)
user3 = User("Sarah", 22)

User.country = "Canada"

print(user1.get_info())
print(user2.get_info())
print(user3.get_info())





















