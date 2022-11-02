''' Pre-defined Functions '''

a=[1,5,63.4,3,36.25]
a.sort()
print(a)
print(sorted([21,35,15,34,98,1,37,165]))
print(sorted((1,35,61,24,12,33,2)))
print(sorted(['a','z','B','c','A','Z','O','o']))
print(ord('o'))
print(chr(106))

''' all() '''
print(all([True,1,2]))
print(all([True,False,1,2]))
print(all([True,'',1,2,3]))
print(all([True,' ',1,2,3]))
print(all([True,' ',1,2,None]))
print(all((True," ",1,2)))
print(all((True,True,None," ",1,2,3)))

''' any() '''
print(any([True,1,2,'',False,None]))
print(any((False,"",None)))
print(any((False,None," ",1)))

''' bool() '''
print(bool(False))
print(bool(True))
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Bool Lokesh"))
print(bool(None))
print(bool(" "))


''' eval() '''
print("eval=",eval("5+3.6-4"))
a=eval("5.3+3.9-5")
b=eval("5-63+99")
print(a,type(a))
print(b,type(b))

''' sum() '''
print("Sum=",sum([1,2,3,4,5]))
print("Sum=",sum((10,20,30,40,50)))

''' reversed-List '''
for i in reversed([1,2,3,4,5]):
    print(i)

''' reversed-Tuple '''
for i in reversed((10,20,30,40,50)):
    print(i)

''' enumerate() ''' '{# Here we can easy to specify index positions of list or tuple or dict or set.}'
a=['bread','milk','Python']
b=enumerate(a)
print(type(b))
print(dict(b))
print(list(b))
print(tuple(b))
print(set(b))

d=['bread','milk','Pyhton']
c=enumerate(d,-10)
print(list(c))