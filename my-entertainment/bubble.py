a=[1,2,3,3,22,2,0,-11]


for i in range(len(a)-1,0,-1):
    for j in range(i):
        if a[j+1]<a[j]:
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp 
print(a)