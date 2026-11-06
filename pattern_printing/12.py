for i in range(6):
    print("*"*i)
    if i==5:
        for i in range(4,0,-1):
            print("*"*i)

print("nnnnn")

i=1
m=4
for j in range(5,0,-1):
    print(' '*j,"*"*i)
    i+=1
    if j==1:
        for sp in range(2,6):
            print(" "*sp,"*"*m)
            m-=1
