# A Lambda function that returns a bigger number
a= lambda x,y:x if x>y else y
x,y = [int(c) for c in input("Enter any two numbers:").split()]
print(a(x,y))

x=[int(s) for s in input("Enter Number:").split()]
print("Bigger Number is:",max(x))
print("Smaller Number is :",min(x))

a=15,35,11
print(max(a))
print(min(a))