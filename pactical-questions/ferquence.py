a = [8,6,8]
un = set(a)
for i in un:
   print(i,"appears",a.count(i),"time")

max_count=0
for i in un:
   freq=a.count(i)
   if freq > max_count:
      max_count=a.count(i)
      num = i
print('most frequent element is',num)


for i in un:
   freq=a.count(i)
   if freq < max_count:
      max_count=a.count(i)
      num=i

print('least frequent element is',num)


   
