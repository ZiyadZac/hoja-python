#Today's Ques: Count how many elements appear more than once.
x=[10,7,4,8,9,4,7,7,10,1,7,1]
#Out: 4
num=0
x2=set(x)
for i in x2:
    count=0
    for j in x:
        if j==i:
            count+=1
    if count>1:
        num+=1
    #print(i,count)
print(num)