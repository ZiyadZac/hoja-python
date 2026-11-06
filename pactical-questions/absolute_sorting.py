a = [8, 6, 7,10,0,-1,-9]
for i in range(len(a)-1,0,-1):
    for j in range(i):
        if abs(a[j+1])<abs(a[j]):
            a[j+1],a[j]=a[j],a[j+1]
print(a)
