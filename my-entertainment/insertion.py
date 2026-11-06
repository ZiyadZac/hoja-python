a = [8, 6, 7, 2,1,0]

for i in range(len(a)-1):
    while a[i]<a[i] and i>0:
        a[i],a[i-1]=a[i-1],a[i]
        i+=1
        print(a)

print(a)