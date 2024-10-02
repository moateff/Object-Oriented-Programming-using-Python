# @property: Decorator used to define a method as a property (it can be accessed like an attribute)
#
# Benefits: Add additional logic when read, write, or delete attributes
#           Gives you getter, setter, and deleter methods

class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return f"{self._width:.1f} cm"
    
    @property
    def height(self):
        return f"{self._height:.1f} cm"
    
    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("Width must be greater than zero")

    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("Height must be greater than zero")

    @width.deleter
    def width(self):
        del self._width
        print("Width has been deleted")

    @height.deleter
    def height(self):
        del self._Height
        print("Height has been deleted")

def main():
    rectangle1 = Rectangle(3, 4)
    print(f"Width = {rectangle1.width}, Height = {rectangle1.height}")
    rectangle1.width = 5
    rectangle1.height = 7
    print(f"Width = {rectangle1.width}, Height = {rectangle1.height}")
    del rectangle1.width
    # print(f"Width = {rectangle1.width}, Height = {rectangle1.height}")

main()