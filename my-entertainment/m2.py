a = [8, 6, 7, 2,1,0]
val=a[0]
for i in range(len(a)-1):
    min_pos=i
    for j in range(i,len(a)):
        if a[j]<a[i]:
            a[i],a[j]=a[j],a[i]

print(a)