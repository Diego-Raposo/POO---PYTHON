class Vehicle:
    def __init__(self,MaxSpeed,Mileage):
        self.MaxSpeed = MaxSpeed 
        self.Mileage = Mileage 

car = Vehicle(200,5000) 
print(f'MaxSpeed: {car.MaxSpeed} km/h')
print(f'Mileage: {car.Mileage} km') 
