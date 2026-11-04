import os

# Function to load balance from a file when the program starts
def load_balance():
    if os.path.exists("balance.txt"):
        with open("balance.txt", "r") as file:
            return float(file.read())
    else:
        return 5000.0  # Default starting balance if file doesn't exist

# Function to save balance to the file whenever it changes
def save_balance(amount):
    with open("balance.txt", "w") as file:
        file.write(str(amount))

# Load your balance at the very beginning
balance = load_balance()

print("===== ATM =====")
print(f"Current Loaded Balance: {balance}\n")

def show_menu():
    x = int(input("""1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter a number (1,2,3,4): """))
    return x        

def deposit():
    global balance
    two = int(input("Amount to deposit: "))
    balance += two
    save_balance(balance)  # <--- Save to file immediately!
    print('Updated balance saved successfully.')
    return balance

def withdraw():
    global balance
    three = int(input("Amount to withdraw: "))
    if three > balance:
        print('Cannot withdraw more than balance')
    else:
        balance -= three
        save_balance(balance)  # <--- Save to file immediately!
        print('Withdraw money-->', three)
        print('balance money-->', balance)

def check_balance():
    print('balance money-->', balance)

def full():
    num = 0
    while num != 4:
        num = show_menu()
        if num == 1:
            check_balance()
        elif num == 2:
            deposit()
        elif num == 3:
            withdraw()
        elif num == 4:
            print("THANK YOU!!")

full()