from functools import reduce
nums=[1,111,2,3]
sum = reduce(lambda x,y:x+y,nums)
print(sum)