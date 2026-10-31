x = [1, 29, 38, 0, -1, 27]
for ind in range(len(x)):
    for i in x:
        if x[ind]<i:
            z=x.index(i)
            x[z],x[ind]=x[ind],x[z]
print(x)