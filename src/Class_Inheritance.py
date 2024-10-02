# Inheritance: Allows a class to inherit attributes and methods from another class
#              Helps withe code reusability and extensibility
#              class Child/Sub(Parent/Super) 

# Multiple Inheritance: Inherit from more than one parent class
#                       C(A, B)

# Multilevel Inheritance: Inherit from a parent which inherits from another parent
#                         C(B) <- B(A) <- A

class Animal:
    def __init__(self, name, color, type):
        self.type = type
        self.name =  name
        self.color = color
    
    def describe(self):
        return f"{self.type}'s name: {self.name}, Color: {self.color}."

class Prey(Animal):
    def flee(self):
        return f"{self.type}s flee."
        
class Predator(Animal):
    def hunt(self):
        return f"{self.type}s can hunt."

class Dog(Predator):
    def __init__(self, name, color):
        super().__init__(name, color, "dog")
    
    def bark(self):
        return f"{self.name} is barking."

class Fish(Prey, Predator):
    def __init__(self, name, color):
        super().__init__(name, color, "fish")
    
    def swim(self):
        return f"{self.name} is swiming."

def main():
    dog1 = Dog(name="boby", color = "gray")
    print(dog1.describe())
    print(dog1.hunt())
    print(dog1.bark())
    fish1 = Fish(name="nemo", color = "blue")
    print(fish1.describe())
    print(fish1.hunt())
    print(fish1.flee())
    print(fish1.swim())

main()    