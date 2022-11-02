def fact(a):
    if a==0:
        return 1
    else:
        b = a*fact(a-1)
        return b
c= abs(int(input("Enter Any Number:")))
print(f"{c}!=",fact(c))

""" 2nd way """
import math
print(math.factorial(5))