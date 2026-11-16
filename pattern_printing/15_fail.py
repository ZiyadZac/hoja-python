j=0
f=6
for i in range(5,-8,-2):
    i=abs(i)
    print(" "*j,"*"," "*i,"*")
    j+=2
    if j>f:
        j-=2
        f-=3



print("HI")