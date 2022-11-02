""" All the classes having different names but having the same function names 
can inheriting the properities of single parent class is called Polymorphism. """
'or'
""" 
Poly+morphs --> many + forms
If something exists in various forms is called Polymorphism.
If an Operator (or) method performs various tasks,it is called Polymorphism.
 """

''' Example '''
class Animal:
    def Noise(self):
        pass
class dog(Animal):
    def Noise(self):
        print("woof woof woof")
class cat(Animal):
    def Noise(self):
        print("Meoow Meoow Meoow")
class monkey(Animal):
    def Noise(self):
        print("Urr Urrr Urrrr")
class tiger(Animal):
    def Noise(self):
        print("growl growl growl")
a=cat()
a.Noise()
b=dog()
b.Noise()
c=monkey()
c.Noise()
d=tiger()
d.Noise()