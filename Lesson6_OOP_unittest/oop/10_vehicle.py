class Vehicle: #родитель-класс
    def __init__(self,brand):
        self.brand = brand

class ElectricCar(Vehicle): #наследник
    def __init__(self,brand,battery_capacity):
        super().__init__(brand)
        self.battery_capacity = battery_capacity

# super() -конструктор родительского класса- сохрани бренд и добавь свое