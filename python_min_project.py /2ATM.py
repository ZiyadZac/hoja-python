print("===== ATM =====")
print()

def show_menu():
    x=int(input("""1. Check Balance
2. Deposit
3. Withdraw
4. Exit
Enter a number(1,2,3,4) """))
    return x        

balance=5000
def deposit():
    global balance
    two=int(input("Amount to deposit:"))
    balance+=two
    return balance

def withdraw():
    global balance
    three=int(input("Amount to withdraw:"))
    if three>balance:
        print('Cannot withdraw more than balance')
    else:
        balance=balance-three
        print('Withdraw money-->',three)
        print('balance money-->',balance)

def check_balance():
    print('balance money-->',balance)

def full():
    num=0
    while num!=4:

     num=show_menu()
     if num==1:
        check_balance()
     elif num==2:
        deposit()
     elif num==3:
        withdraw()
     elif num==4:
        print("THANK YOU!!")

full()
