""" A Single child can inheriting the properities of a single parent is called as Single level Inheritance.
{A Single inheritance,only one child can be inherited from parent class not more than one class can be used ofr inheritance.} """

class Animal:
    Livingthing = True
    def eat():
        print("Eating")
    def sleep():
        print("Sleeping")
class dog(Animal):
    def eat():
        print("It is ate only Pedigree")
    def sleep():
        print("It is always sleeping behind me")
    def play():
        print("It's not playing good when i am not at home")
print(dog().Livingthing)
print(Animal().Livingthing)
dog.eat()
dog.sleep()
dog.play()
Animal.eat()
Animal.sleep()
Animal.play()



''' Example '''
class Parent:
     def __init__(self , fname, fage):
          self.firstname = fname
          self.age = fage
     def view(self):
         print(self.firstname , self.age)
class Child(Parent):
     def __init__(self , fname , fage):
          Parent.__init__(self, fname, fage)
          self.lastname = "Machine Learning"
     def view(self):
          print(self.firstname ," came ",  self.age , " years ago. Today, python is the base for" , self.lastname)
object = Child("Python" , '28')
object.view()



''' Example '''
class Base:
     def __init__(self , fname, fage):
          self.firstname = fname
          self.age = fage
     def view(self):
         print(self.firstname , self.age)
class Child(Base):
     def __init__(self , fname , fage):
          Base.__init__(self, fname, fage)
          self.lastname = "Machine Learning"
     def view(self):
          print(self.firstname ," is ",  self.age , " years old and he is a pro in " , self.lastname)
object = Child("Raj" , '21')
object.view()
