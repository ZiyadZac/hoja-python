x=input('enter ' )#110
z=''
for i in x:
  if i not in z:
    z+=i
for i in z:
  print(f"{i} appears {x.count(i)} times")
