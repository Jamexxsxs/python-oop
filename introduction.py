# Creating a simple class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Camry")
print(f"My car is a {my_car.make} {my_car.model}")

# Basic Class with Instance Variables
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog1 = Dog("Buddy", "Golden Retriever")
print(f"{dog1.name} is a {dog1.breed}")

# Class with Method
class Person:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print(f"Hello, my name is {self.name}")

person1 = Person("Alice")
person1.greet()