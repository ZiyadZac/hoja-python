#Today's Question: Sort an array without using built-in function.
inp =[4,9,6,1,2,0,1,4,5,3]
#out=[0,1,1,2,3,4,4,5,6,9]
for i in range(len(inp)):
  for j in range(i+1,len(inp)):
    if inp[j]<inp[i]:
      inp[j],inp[i]=inp[i],inp[j]
print(inp)