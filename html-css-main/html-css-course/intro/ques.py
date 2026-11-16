#Today's question: Check if a given list contains only numbers.

#x=["7", "0", "python", "6", "sql"]
x=["7", "5", "2", "8"]
z=True
for i in x:
  try:
    f=int(i)
  except ValueError:
    z=False
print(z)


