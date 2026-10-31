try:
    with open("note.txt", "r") as file:
        print(file.read())
except FileNotFoundError:
    print("file does not exist!")
   

