""" Both Child and Parent Classes having same function names but the child class is 
overrides parent class when function called is known as Method Overriding. """
'or'
" Executing only sub class method in the palce of super class method. "

''' Example '''
class Parent:
    def study(self):
        print("Don't play games more time spend time more for your education to earn knowledge")
class child(Parent):
    def study(self):
        print("I don't want to study more i want to play more time")
a=child()
a.study()
b=Parent()
b.study()