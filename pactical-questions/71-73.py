#71 Compute the prefix sum of an array.
a=[1,3,5,7,9]
for i in range(1,len(a)):
    a[i]+=a[i-1]
print(a)
print()
#72 Compute the suffix sum of an array.
b=[2,4,6,8]
for i in range(len(b)-1,0,-1):
    b[i-1]+=b[i]
print(b)
#73 Find the running sum of an array.