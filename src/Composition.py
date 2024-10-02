# Composition: The composed object directly owns its components, wwhich cannot exist independently
#              "owns-a" relationship

class Engine:
    def __init__(self, horse_power):
        self.horse_power = horse_power

class Wheel:
    def __init__(self, size):
        self.size = size

class Car:
    def __init__(self, model, horse_power, wheel_size):
        self.model = model 
        self.engine = Engine(horse_power) # engine attribute is a class itself
        self.wheels = [Wheel(wheel_size) for wheel in range(4)]
    
    def describe(self):
        return f"{self.model} car, its engine power is {self.engine.horse_power} hp and the wheel size is {self.wheels[0].size} inches"

def main():
    car1 = Car(model = "Ford Mustang", horse_power = 670, wheel_size = 19)
    print(car1.describe())

main()