# Nested Class: A class defined within another class
#               class Outer
#                   class Inner
#
# Benefits: Allows you to logically group classes that are closely related
#           Encapsulates private details that aren't relevent outside of the outer class
#           Keeps the namespace clean; reduces the possibility of naming conflicts

class Company:
    class Employee:
        def __init__(self, name, position):
            self.name = name
            self.position = position
        
        def get_details(self):
            return f"{self.name} as a {self.position}"
    
    def __init__(self, company_name):
        self.company_name = company_name
        self.employees = [] # list of objects

    def add_employee(self, name, position):
        new_employee = self.Employee(name, position)
        self.employees.append(new_employee)
    
    def list_employees(self):
        return [employee.get_details() for employee in self.employees]

def main():
    company1 = Company(company_name = "Krusty Krab")
    company1.add_employee("Mohamed", "Manager")
    company1.add_employee("Ahmed", "Worker")
    for employee in company1.list_employees():
        print(employee)

main()