import datetime as dt #2
print(dt.datetime.now())
print(dt.date.today())

import random as rnd #3
list1=[]
for i in range(100+1):
  list1.append(i)
print(rnd.randint(0,100))
print(rnd.choice(list1))
rnd.shuffle(list1)
print(list1)

import statistics as st #4
print(st.mean(list1))
print(st.median(list1))
print(st.mode(list1))
