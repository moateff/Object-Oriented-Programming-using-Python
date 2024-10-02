# Class Variables: Shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created from that class

class Student:
    class_year = 2025
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

    def describe(self):
        return f"Student name: {self.name}, age: {self.age}"

def main():
    student1 = Student(name = "Mohamed", age = 22)
    student2 = Student(name = "Ahmed", age = 23)
    print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
    print(student1.describe())
    print(student2.describe())

main()
