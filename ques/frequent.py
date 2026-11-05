#Today's Ques: Find the most frequent element.
x=[10,7,4,8,9,4,7,7,10,1,7,1]
x1=set(x)
#print(x1)
maax = 0
for i in x1:
    if maax < x.count(i):
        maax = x.count(i)
        #print(i,maax)
        num = i
print(num)

x=[10,7,4,8,9,4,7,7,10,1,7,1]
x1=set(x)

x=[10,7,4,8,9,4,7,7,10,1,7,1]
x1=set(x)

for i in x1:
    freq=0
    for num in x:
        if num==i:
            freq+=1
    print('freq of',i,"is",freq)

maax_f=0

for i in x1:
    freq2=0
    for num in x:
        if num==i:
            freq2+=1
        if freq2 > maax_f:
            maax_f=freq2
            num_f=i

print(num_f)