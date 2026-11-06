x = [1, 29, 38, 0, -1, 27]
min_val=x[0]
for i in range(len(x)):
    min_val=x[i]
    for j in x[i:]:
        if j<min_val:
            min_val=j
    temp=x[i]
    n=x.index(min_val)
    x[i]=min_val
    x[n]=temp    

print(x)
