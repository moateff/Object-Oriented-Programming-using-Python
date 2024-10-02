# Abstract Class: A class that cannot be instantiated on its own, Meant to be subclassed
#                 They can contain abstract methods, which are declared but have no implementation
#
# Abstract Class Benefits: 1. Prevents instantiation of the class itself
#                          2. Requires children to use inherited abstract methods 

from abc import ABC, abstractmethod

class Vehical(ABC):
    @abstractmethod
    def go(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehical):
    def __init__(self, model, color, for_sale):
        self.model = model
        self.color = color
        self.for_sale = for_sale

    def go(self):
        return f"{self.model} starts moving."

    def stop(self):
        return f"{self.model} stopped."

def main():
    car1 = Car(model = "Chevrolet", color = "red", for_sale = False)
    print(car1.go())
    print(car1.stop())

main()