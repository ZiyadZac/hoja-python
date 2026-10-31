def write_note():
    x=input("enter the note ")
    file=open("notes.txt","a") 
    file.write()
    file.close()

def read_notes():
    file=open("notes.txt","r") 
    print(file.read())
    file.close()

def main():
    print('1->Write a new note' \
    '2->Read the note' \
    '3->Exit')
    ch=input('Enter(1 or 2 or 3)')
    if ch=="1":
        write_note()
    elif ch=="2" :
        read_notes()
    elif ch=='3':
        print("Good bye<3")
    else:
        print("try again")
 
main()