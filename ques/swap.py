nums=[4,8,2,6,7]
first=nums[0]
for i in range(len(nums)):
  if i == 0:
    nums[0]=nums[-1]
  elif i == len(nums)-1:
    nums[-1]=first
  
print(nums)