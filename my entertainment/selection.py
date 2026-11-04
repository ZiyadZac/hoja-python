a = [8, 6, 7, 2,1,0]

for i in range(len(a) - 1):
    #print(i,'is i')
    min_pos = i
    for j in range(i + 1, len(a)):
        #print(j,"is j")
        if a[j] < a[min_pos]:
            min_pos = j
    temp = a[i]
    a[i] = a[min_pos]
    a[min_pos] = temp
    #print(a)

print(a)
