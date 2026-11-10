#Today's Question: Remove elements smaller than a given value.
x=[5,8,3,2,9,7] 
val=4
for i in x:
    if i<val:
        x.remove(i)
print(x)