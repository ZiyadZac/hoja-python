x = [5,8,3,9,2,10]
z=0
for i in range(len(x)):
    if  i%2!=0:
        z+=x[i]
print(z) 
for i in x:
    if i%2==0:
        ind = x.index(i)
        x[ind]=0

print(x)