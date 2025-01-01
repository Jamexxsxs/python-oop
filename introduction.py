# Creating a simple class
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Toyota", "Camry")
print(f"My car is a {my_car.make} {my_car.model}")

