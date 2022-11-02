def greet():
    print("Hello")
greet()

def greet(n):
    print("Hello "+n)
greet('Lokesh')
greet('Sai')
greet('Ram')

def greet(*names):
    print('Hey '+names[2])
greet('Lokesh','Seetha','Parvathi','Krishna')

def details(n,a):
    print('Hey '+n+'! where is '+a)
details('Ram', 'Seetha')
details('Lokesh', 'Amma')

def details(n,a):
    print('Hey '+n+'! Your age is '+a)
n=input("Enter Your Name:")
a=input("Enter Your Age:")
details(n, a)

def form(name,age,ph):
    print('Hey '+name+'! your age is '+age+' and your mobile number is:'+ph+'.')
name=input("Enter Your Name:")
age=input("Enter Your Age:")
ph=input("Enter Your Mobile Number:")
form(name, age, ph)

def a(g,h):
    return g*h
print(a(3, 6))

def v(a,b):
    return a-b,a*b,a/b
a=int(input("Enter Any Number:"))
b=int(input("Enter one more Number:"))
print(v(a, b))