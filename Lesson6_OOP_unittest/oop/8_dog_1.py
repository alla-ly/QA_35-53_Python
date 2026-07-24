class Dog:
    species = "Canis familiaris" #атрибут класса

    def __init__(self,name):# атрибут экземпляров
        self.name = name

dog1 = Dog("Bobby")
dog2 = Dog("Ocean")

print(dog1.species,dog1.name)
print(dog2.species,dog2.name)

Dog.species = "Wolf" #меняем атрибут класса

print(dog1.species,dog1.name)
print(dog2.species,dog2.name)