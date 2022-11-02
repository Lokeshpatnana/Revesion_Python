""" Same operator performing morethan one task. """
'or'
""" Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
For example operator + is used to add two integers as well as join two strings and merge two lists. 
It is achievable because ‘+’ operator is overloaded by int class and str class. 
You might have noticed that the same built-in operator or function 
shows different behavior for objects of different classes, this is called Operator Overloading.  """

''' Example '''
a=15
b=36
print(a+b)

c="lokesh"
d="patnana"
print(c+d)

e=[1,2,3]
f=[4,5,6]
print(e+f)
print(e[:]+f[:])