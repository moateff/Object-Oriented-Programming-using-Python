# Super(): Function used in a child class to call methods from a parent class (superclass).
#          Allows you to extend the functionality of inherited methods

class A:
    def __init__(self):
        print("A is the super")

class B:
    def __init__(self):
        print("B is the super")

class C(B, A):
    def __init__(self):
        super().__init__()


class Shape:
    def __init__(self, type, color, is_filled):
        self.type = type
        self.color = color 
        self.is_filled = is_filled
    
    def describe(self):
        return f"It is {self.color} {self.type} and it is {"filled" if self.is_filled else "not filled"}."
    
class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__("circle", color, is_filled)
        self.radius = radius
    
    def area(self):
        return f"{3.14 * self.radius ** 2} cm2"

class Square(Shape):
    def __init__(self, color, is_filled, side):
        super().__init__("square", color, is_filled)
        self.side = side

    def area(self):
        return f"{self.side ** 2} cm2"

def main():
    c = C()
    circle1 = Circle(color = "red", is_filled = True, radius = 7)
    print(circle1.describe())
    print(f"Area = {circle1.area()}")
    square1 = Square(color = "blue", is_filled = False, side = 5)
    print(square1.describe())
    print(f"Area = {square1.area()}")

main()

