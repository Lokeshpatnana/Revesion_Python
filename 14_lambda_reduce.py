# A Lambda that returns products of elements of a list
from functools import *
a = [1,2,3,4,6,8,6,4,9,11]
b = reduce(lambda x,y:x+y,a)
c = reduce(lambda x,y:x-y,a)
print(b)
print(c)

x=[5,2,3]
y=reduce(lambda a,b:a+b,x)
z=reduce(lambda a,b:a-b,x)
print(y)
print(z)