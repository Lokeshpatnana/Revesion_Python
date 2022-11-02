# Positional arguments demo
def combine(a1,a2):
    b=a1+a2
    print("The Total String is:",b)
combine('Lokesh','Learning Python')
a1,a2 = [x for x in input().split(',')]
combine(a1,a2)