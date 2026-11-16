#* * * * *
for i in range(5):
    if i==0 or i==4:
        print("* * * * *")
    else :
        print("*       *")

for i in range(6):
    if i==0 or i==2 or i==3 or i==5:
        print("  *   * ")
    else :
        print("* * * * *")
j=0
for i in range(5):
    
    if i==0:
        print("*")
    elif i==4:
        print("* * *")
    else:
        print(f'*{' '*j}*')
        j+=1
    