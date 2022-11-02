""" Methods are the functions that are defined inside the body of a class and associated with an object.
They are used to define the behaviors of an object. """

''' Example '''
class Employee:
    # class attribute
    company = "copyassignment.com"
    # constructor
    def __init__(self, name, age, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary
    # class method
    def myMethod1(self):
        print(f"Hi {self.name}!")
    def myMethod2(self, city):
        print(f"{self.name}, do you lives in {city}?")
    def MyMethod(self):
        print(f"{self.name},always addict for Money")

# creating objects
emp1 = Employee("Lokesh", 22, 50000)
emp2 = Employee("Hari", 22, 60000)
emp3 = Employee("SaiKishore", 22, 390000)

# calling methods
emp1.myMethod1()
emp1.myMethod2("Hyderabad")
emp1.MyMethod()
emp2.myMethod1()
emp2.myMethod2("Mysore")
emp3.myMethod1()
emp3.myMethod2("Hyderabad")