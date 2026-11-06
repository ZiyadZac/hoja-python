#61 Merge two sorted arrays into a single sorted array.
a = [6, 8,-9,10,10,7,7,10,0,-1,-9,100]
b = [8, 6, 7,10,0,-1,-9]
a.sort()
b.sort()
c = a + b
c.sort()
print(c)
print()
#62 Merge two unsorted arrays and sort them.
a = [6, 8,-9,10,10,7,7,10,0,-1,-9,100]
b = [8, 6, 7,10,0,-1,-9]
c = a + b
c.sort()
print(c)
print()
#63 Find common elements between two arrays.
un1= set(a)
un2= set(b)
print(un1&un2)
print()
#64 Find unique elements present in one array but not the other.
print(un1-un2)
print()