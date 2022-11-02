""" One or Morethan one child classes can be inheriting the 
properities of single parent class is called as Hierarchicla Inheritance. """
'or'
""" In hierarchical inheritance from a single base class, we can inherit multiple derived classes. 
There is no restriction on the number of derived classes. """

class Parent:
    food = "Yes"
    Enjoy = "Yes"
    Alcohol = "No"
    def money(self):
        print("I fixed deposited all my savings in bank account for my childrens future wealth.")
class Lokesh(Parent):
    def study(self):
        print("Studying good but no job yet?")
    def love(self):
        print("Love failure because of no job")
    def current(self):
        print("Searching for job")
class Sandhya(Parent):
    def marriage(self):
        print("Completed 3 years ago")
    def childrens(self):
        print("One children with beautiful life with oh so sexy husband")
    def study(self):
        print("No study yet, I stopped it few years ago")
a = Lokesh()
print(a.Alcohol)
print(a.Enjoy)
print(a.food)
a.current()
a.love()
a.money()
a.study()

b = Sandhya()
print(b.Alcohol)
print(b.Enjoy)
print(b.food)
b.childrens()
b.marriage()
b.money()
b.study()