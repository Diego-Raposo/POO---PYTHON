"""Define a property that must have the 
same value for every class instance (object)"""

class Vehicle:
    color = "White"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

car = Bus("Ferrari", 250, 30)
print(f'Color: {car.color}, Name: {car.name}, Max speed: {car.max_speed} km/h, Mileage: {car.mileage} km')


car2 = Car("Tesla", 200, 50)
print(f'Color: {car2.color}, Name: {car2.name}, Max speed: {car2.max_speed} km/h, Mileage: {car2.mileage} km')