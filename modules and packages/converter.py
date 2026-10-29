x=int(input("Enter the distance:"))
y=input("km/miles: ").lower()
y=y.replace(" ","")
if y=="km":
    print("Distance in miles:",x*0.62)
elif y=="miles":
    print("Distance in km:",x*1.61)
else:
    print("Invalid input")
