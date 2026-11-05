item={}
def add_item():
    x=''
    while x!='exit':
        x=input("""
Enter the item name: 
else enter exit.     """).lower().strip()
        if x!="exit":
           b=float(input("Enter quantity: "))
           item[x]=b
    print()
    return item
def calculate_total(dicct):
    i=0
    store={'milk':25,'rice':100,'water':20,'snacks':10}
    for x in dicct:
        if x in store:
            print("Item-->",x)
            print("Prise->",dicct[x],'*',store[x])
            print()
            i=i+dicct[x]*store[x]
    print()
    print("Total without GST->",i)
    return i
def calculate_gst(total):
    print("Total with GST->",total+total*0.05)


cart_items = add_item()
total=calculate_total(cart_items)
calculate_gst(total)
