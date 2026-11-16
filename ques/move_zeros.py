#Today's Question:Move all zeros to the end of the list without changing the order of other elements.
list1 = [1,0,5,0,0, 8, 3, 0, 7,0]
count=0
for i in range(len(list1)):
    if i==0:
        count+=1
    for i in range(count):
        list1.remove(0)
    for i in range(count):
        list1.append(0)
    
print(list1)