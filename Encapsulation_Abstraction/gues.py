#Ques: Find the first element that appears more than once

#x=[1,2,3,4,3,5,6,6]
x=[1,2,3,4,32,5,6,6]
z={}
for i in x:
    if i not in z:
        z[i]=1
    else:
        z[i]+=1
for key,value in z.items():
    if value>1:
        print(key)
        break

