x=input('enter ' )
x=x.replace(' ','')
for i in x:
  z=x.count(i)
  if z==1:
    print("first non repeating element is",i)
    break