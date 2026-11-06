for i in range(1,6):
    z=str(i)
    print(z*i)
print("___------____")
num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end="")
        num += 1
    print()
print("___------____")
num = 1
for i in range(1,6):
    for j in range(i):
        print(num,end="")
    num += 1
    print()


