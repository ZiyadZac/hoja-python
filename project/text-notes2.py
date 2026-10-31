def write_note():
    note = input("Enter your note: ")
    # Using 'with' automatically handles file.close() safely
    with open("notes.txt", "a") as file:
        file.write(note + "\n")
    print("Note saved successfully!")

def read_notes():
    try:
        with open("notes.txt", "r") as file:
            print("\n--- YOUR NOTES ---")
            print(file.read())
    except FileNotFoundError:
        print("No notes found yet! Write one first.")

def main():
    while True:
        print("1 -> Write a new note")
        print("2 -> Read the notes")
        print("3 -> Exit")
        
        ch = input("Enter (1, 2, or 3): ")
        if ch == "1":
            write_note()
        elif ch == "2":
            read_notes()
        elif ch == "3":
            print("Good bye <3")
            break  # Exit the loop
        else:
            print("Try again!")

main()