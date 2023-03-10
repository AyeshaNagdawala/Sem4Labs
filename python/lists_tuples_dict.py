
a=[1,5,6,3,7]
print(a)

print("After append")
a.append(9)
print(a)

print("After popping : popping removes last element")
a.pop()
print(a)

print("After removing : remove removes any mentioned element")
a.remove(5)
print(a)

a.append(9)
a.append(4)
print(a)

print("After sorting")
a.sort()
print(a)

print(a[2])
print("Counts the number of time a mentioned number has occured in the list")
print(a.count(6))
print(a.count(5))

a.reverse()
print(a)
a.reverse()
print(a)

length=len(a)
print(length)

maximum=max(a)
print(maximum)

minimum=min(a)
print(minimum)

del a[3]
print(a)

print(a[-1])
# print 7 in a
print(7 in a)
print(8 in a)
print(a*2)
print(2*a)
b=[1,6,3,'a',2,'bat']
print(a+b)
c = (1,2,3,4)
d = (1,2,3,5)
print(c+d)
print(2*c)

print(len(c))
maxi=max(c)
mini=min(c)
print(maxi)
print(mini)
e=(1,5,8,9,2)
# e.sort()
f=list(e)
f.sort()
print(f)
g=tuple(f)
print(g)
# print("Sort won't support string and int comparison.")
# b=[1,6,3,'a',2,'bat']
# b.sort()
# print(b)
# print(a::-1)

dict = {'name':'ayesha','age':19,'contact':'7208662871','gender':'female'}
print("dictionary",dict)
print("keys",dict.keys())
print("values",dict.values())
print("items",dict.items())
print(len(dict))
del dict['age']
print(len(dict))
print(dict['gender'])
