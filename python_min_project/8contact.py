def show_menu():
    x=int(input("""1. Input name
2.Search contact
3.Delete_contact
4.Exit
Enter a number(1,2,3,4) """))
    return x   

def add_contact():
    cont={}
    naam=input("enter name: ").lower().capitalize()
    num=input('enter number:')
    cont[naam]=num
    return cont
def search_contact(cont):
    x=input("search name: ").lower().capitalize()
    if x in cont:
        print("number is",cont[x])
    else:
        print("not found")
def delete_contact(cont):
    x=input("name to be deleted: ").lower().capitalize()
    if x in cont:
        del cont[x]
    else:
        print("not found")

def full():
    num=0
    while num!=4:

     num=show_menu()
     if num==1:
        cont=add_contact()
     elif num==2:
        search_contact(cont)
     elif num==3:
        delete_contact(cont)
     elif num==4:
        print("THANK YOU!!")

full()

            
