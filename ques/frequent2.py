x=[10,7,4,8,9,4,7,7,10,1,7,1]
dicct={}
maax=0
for num in x:
    if num in dicct:
        dicct[num]+=1
    else:
        dicct[num]=1
for num in dicct:
    if dicct[num]>maax:
        maax=dicct[num]
        maax_num=num
print(maax_num)