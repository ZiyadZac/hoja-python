x = [5,8,3,9,2,10]
small= x[0]
large= x[0]
for i in x:
    if i<small:
        small=i
for i in x:
    if i>large:
        large=i
print(large-small)