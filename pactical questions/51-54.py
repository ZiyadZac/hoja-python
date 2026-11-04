a = [6, 8,-9,10,10,7,7,10,0,-1,-9]

x=int(input('enter a number '))
#51 Remove all occurrences of a given element.
if x in a:
  for i in range(a.count(x)):
   a.remove(x)
  print(a)

#52 Remove even numbers from an array.
for num in a[:]:
  if num % 2 == 0:
    a.remove(num)
print(a)
a = [6, 8,-9,10,10,7,7,10,0,-1,-9]
#53 Remove odd numbers from an array.
for num in a[:]:
  if num % 2 != 0:
    a.remove(num)
print(a)

#54 Remove elements smaller than a given value.
z=int(input('enter a number '))
for num in a[:]:
  if num < z:
    a.remove(num)
print(a)