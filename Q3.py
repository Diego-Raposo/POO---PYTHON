class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Child(Vehicle):
    pass

car = Child("School Volvo", 180, 12)
print(f'Vehicle Name: {car.name} Speed: {car.max_speed} km/h Mileage: {car.mileage}')