# Instance Methods: Best for operations on instances of the class (objects) 
# 
# Class Methods: Allows operations related to the class itself
#                Take (cls) as the first parameter, which represents the class itself
#                Best for class-level data or require access to the class itself
#
# Static Methods: A method that belong to a class rather than any object from that class (instance)
#                 Usually used for general utility functions that do not need access to clase data
#
# Magic Methods: Dunder methods (double underscore) __init__, __str__, __eq__
#                They are automatically called by many of Python's built-in operations.
#                They allow devolopers to define or customize the behavior of objects

class Employee:
    valid_positions = ["Manager", "Cashier", "Cook"]

    def __init__(self, name, position):
        self.name = name
        if position in Employee.valid_positions:
            self.position = position
            Employee.valid_positions.remove(position)
        
    def get_details(self):
        return f"{self.name} as a {self.position}"
    
    @staticmethod
    def is_valid_position(position):
        return position in Employee.valid_positions
    
def static_method():
    employee1 = Employee("Mohamed", "Manager")
    print(Employee.is_valid_position("Manager"))


class Student:
    num_students = 0 
    total_gpa = 0

    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa
        Student.num_students += 1
        Student.total_gpa += gpa
    
    # Instance Method
    def get_details(self):
        return f"Student name: {self.name}, GPA: {self.gpa}"
    
    @classmethod
    def get_num_students(cls):
        return cls.num_students

    @classmethod
    def get_average_gpa(cls):
        return f"{cls.total_gpa / cls.num_students:.2f}"

def class_method():
    student1 = Student(name = "Mohamed", gpa = 3.5)
    student2 = Student(name = "Ahmed", gpa = 2.5)
    student3 = Student(name = "Mostafa", gpa = 4)
    student4 = Student(name = "Ayman", gpa = 3.7)
    print(f"Number of students = {Student.get_num_students()}")
    print(f"Average GPA = {Student.get_average_gpa()}")

class Book:
    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"{self.title} by {self.author}."
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages
    
    def __add__(self, other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    
    def __getitem__(self, keyword):
        if keyword == "title":
            return self.title
        elif keyword == "author":
            return self.author
        elif keyword == "pages":
            return self.num_pages
        else:
            return f"Key {keyword} was not found."

def magic_method():
    book1 = Book("Harry Potter", "J.K. Rowling", 500)
    book2 = Book("The Hobbit", "J.R.R. Tolkein", 450)
    print(book1)
    print(book1 == book2)
    print(book1 < book2)
    print(book1 > book2)
    print(book1 + book2)
    print("Rowling" in book1)
    print(book2["author"])

magic_method()