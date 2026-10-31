x = [1, 29, 38, 0, -1, 27]
new=[]
min=x[0]
for i in x:
    for mm in range(len(x)):
      if i < min:
        min = i
        
    new.append(min)   

print(min)  
print(new)

