#80 Find the subarray with the maximum sum.
a = [6, 8,10,-10,7,-7,10,0,-1,-9,10]
for i in range(1,len(a)):
    a[i]+=a[i-1]
print(a)
maax=a[-1]
ind=0
for i in range(len(a)-1,0,-1):
    if maax<=a[i]:
        maax = a[i]
        ind=i+1
b=a[:ind]
print(b)
    
