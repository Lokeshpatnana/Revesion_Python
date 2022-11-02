""" A function is having default values in the arguments 
but during the function called we pass other (or) new values it is called Method Overloading. """
'or'
""" Same method perfoming morethan one task. """

''' Example '''
class Lokesh:
    def sum(self,a=2,b=3,c=5):
        print("Sum is:",a+b+c)
x=Lokesh()
x.sum()
x.sum(6,8,4)
x.sum(c=3,a=10)