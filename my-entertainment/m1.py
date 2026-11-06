x=int(input("enter a number "))
num=[]
for i in range(x+1):
    num.append(i)

import random as rnd
rnd.shuffle(num)
print(num)

print()
num=sorted(num)
print()
print(num)