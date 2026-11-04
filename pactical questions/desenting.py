a = [8, 6, 7,10,0,-1]
def bubble(a):
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j+1]<a[j]:
                a[j+1],a[j]=a[j],a[j+1]
    print(a)

bubble(a)

def selection(a):
    for i in range(len(a)-1):
        min_pos=i
        for j in range(i,len(a)):
            if a[j]<a[min_pos]:
             min_pos=j
        a[min_pos],a[i]=a[i],a[min_pos]
    print(a)
    return(a)

selection(a)

#desenting order
b=selection(a)
print(b[::-1])


