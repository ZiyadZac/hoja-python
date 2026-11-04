

def display_questions():
    global i
    i=0
    print("""what is 3+6/2
    A) 4.5
    B) 4
    C) 6
    D) 5.5""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "C":
        i += 1

    print("""What will print("Hello World".lower()) output?
    A) HELLO WORLD
    B) hello world
    C) Hello world
    D) Hello World""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "B":
        i += 1

    print("""What is the index of the first item in a Python list?
    A) 1
    B) -1
    C) 0
    D) Last index""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "C":
        i += 1

    print("""Which keyword is used to define a custom function in Python?
    A) func
    B) define
    C) function
    D) def""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "D":
        i += 1

    print("""When opening a file to read its contents, which mode string should you pass to open()?
    A) "w"
    B) "r"
    C) "a"
    D) "x" """)
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "B":
        i += 1

    print("""What numbers are included in range(1, 5)?
    A) 1, 2, 3, 4, 5
    B) 1, 2, 3, 4
    C) 0, 1, 2, 3, 4
    D) 2, 3, 4, 5""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "B":
        i += 1

    print("""What data type is [1, "apple", 3.5]?
    A) Tuple
    B) Dictionary
    C) List
    D) String""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "C":
        i += 1

    print("""To generate a random integer between two numbers, which function do you use?
    A) random.choice()
    B) random.randint()
    C) random.shuffle()
    D) random.float()""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "B":
        i += 1

    print("""Why might a programmer use the global keyword inside a function?
    A) To make code run faster
    B) To import external packages
    C) To modify a variable defined outside that function
    D) To clear memory automatically""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "C":
        i += 1

    print("""What does the built-in len() function return when given a list?
    A) The sum of all numbers in the list
    B) The data type of the list
    C) The total number of items in the list
    D) The maximum value in the list""")
    ans = input("A, B, C, or D: ").capitalize().strip()
    if ans == "C":
        i += 1

display_questions()
print(f"\n===== QUIZ FINISHED =====")
print(f"Your Total Score: {i} / 10")

