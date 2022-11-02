""" Local Scope
Value can be accessed inside the function only. """
"""
def ram():
    a = 5;b=66;c=89
    print(a+b*c)
ram()
"""
""" Global scope of a variable,can be accessed by anyone """
"""
a = 68
def sita():
    b =34
    c= 54;a=5
    print(a)
    print(b)
    print(c)
print(a)
sita()
print(a)
"""

""" global is the keyword,which is need to be specified if we want to use the local variable as global variable. """
"""
a=55
def loki():
    c=86
    global a,b
    a=5
    b=8
    print(b)
    print(c)
print(a)
loki()
print(a)
print(b)
print(a)
"""

""" Count the length of the string without using built-in function """
"""
def len(a):
    c = 0
    for i in a:
        c+=1
    return c
print(len('Lokesh'))
"""

""" A Person having multiple names """
"""
def ssc():
    School = 'STPS'
    print(f"My School Name is {School}")
    inter()
def inter():
    inter = 'GGJC'
    print(f"My Intermediate clg is {inter}")
def degree():
    BSC = 'RKJDC'
    print(f"MY Degree clg is {BSC}")
    ssc()
degree()
"""