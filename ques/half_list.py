a=[6,7,2,9,1]
b=[]
if len(a) % 2 == 0:
      x =(len(a) // 2)
      for i in range(x):
               b.append(a[i])

else:
     x = (len(a) // 2)
     for i in range(x+1):
        b.append(a[i])
      
print(b)
#a=[6,7,2,9,1]
#b=[10,7,4,8,9,4]
