j=4
for i in range(1,6):
    print(" "*j,"* "*i)
    j-=1

for i in range(4,-1,-1):
    print(" "*i,'* '*5)

k=1
for i in range(4,-1,-1):
    print(" "*i,"*"*k)
    k+=2

k=9
for i in range(4):
    print(" "*i,"*"*k)
    k-=2
