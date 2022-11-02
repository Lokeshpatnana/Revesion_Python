""" Objects are the instantiation of classes and also the way to use classes.
These are those entities that have attributes and behaviors which are defined inside the class.
In real-word, object examples are desktop, mobile, ac, freeze, etc.
When we create a class, then we only describe the blueprint for objects but memory is allocated when we create objects of classes. """

''' Example '''
class Employee:
    # class attribute
    company = "TCS"
    # constructor
    def __init__(self, name, age, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.salary = salary

# creating objects
emp1 = Employee("Lokesh",22, 50000)
emp2 = Employee("Hari", 22, 60000)

# accessing class attributes using __class__ method
# syntax is-- instance.__class__.attribute
print(f"{emp1.name} and {emp2.name} work for {emp1.__class__.company}")

# accessing instance attributes
# syntax is-- instance.instance_attribute
print(f"{emp1.name}'s age is {emp1.age} and salary is {emp1.salary}")
print(f"{emp2.name}'s age is {emp2.age} and salary is {emp2.salary}")