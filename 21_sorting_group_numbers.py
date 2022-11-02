def fun(lis):
    lis.sort()
    for i in lis:print(i,end=" ")
print("Enter Numbers:")
a = [int(x) for x in input().split()]
fun(a)


"2nd way"
lo = [int(x) for x in input().split()]
lo.sort(reverse=True)
print(*lo)