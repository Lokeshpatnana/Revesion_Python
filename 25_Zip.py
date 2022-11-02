a1 = [10,20,30,40,50,60]
a2 = [1,2,3,4,5]
print(a1+a2)
b = list(zip(a1,a2))
print(b)

for x,y in zip(a1,a2):
    print(x,y)

for x,y in zip(a1,a2):
    print(x+y,x-y)

a=range(10,15)
b=range(12,13)
for x,y in zip(a,b):print(x+y,x-y)