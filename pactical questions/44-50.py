a = [6, 8,-9,10,10,7,7,10,0,-1,-9]

#44 Count how many elements appear more than once.
un = set(a)#44
for i in un:
   if a.count(i)>1:
      print(i,"appears more than once")

#45 Find the first element that appears more than once.
for i in a:
   if a.count(i)>1:
      print(i,"is the first element that appears more than once")
      break

#46 Check if all elements are unique.
if len(un)==len(a):
   print('all elements are unique')
else:
   print('all elements are not unique')

#47 Count how many elements appear exactly twice.
for i in un:
   if a.count(i)==2:
      print(i,"appears exactly twice")