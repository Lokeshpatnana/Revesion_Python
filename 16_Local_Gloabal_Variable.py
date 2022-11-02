# Example on Local And Global Variable
a=12
def num():
    b=45
    a=36
    print("Local Variable:",a)
    print("Local Variable:",b)
    print("Global Variable:",a)
print("Global Variable:",a)
num()
print("Global Variable:",a)

# To Print global variable in a function then we call gloabal in function
x=41
def number():
    global x
    x=21
    print(x)
# print(x)
number()
# print(x)