# A Lambda function that returns even numbers from a list
c = [12,5,3,4,15,5,36,749,69,445,33,45,10]
# list1 = [int(x) for x in input().split()]
a= list(filter(lambda x:(x%2 == 0),c))
b= list(filter(lambda x:(x%2 !=0),c))
print(a)
print(b)