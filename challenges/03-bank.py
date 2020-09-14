print("Welcome to Chase bank.")

balance = 5000

def deposit(balance):
    amount = input("Enter the amount you want to deposit: ")
    amount = int(amount)
    balance = balance + amount
    print(f"Your current balance is {balance}")
    finish(balance)

def withdraw(balance):
    amount = input("Enter the amount you want to withdraw: ")
    amount = int(amount)
    balance = balance - amount
    print(f"Your current balance is {balance}")
    finish(balance)

def finish(balance):
    finished = input("Are you finish? (yes or no)")
    if(finished == "yes"):
        print("Have a nice day!")
    elif(finished == "no"):
        doTransaction(balance)
    
def doTransaction(balance):
    print(f"Your current balance is {balance}")
    choice = input("What would you like to do? (deposit, withdraw, balance)")

    if(choice == "deposit"):
        deposit(balance)
    elif(choice == "withdraw"):
        withdraw(balance)
    elif(choice == "balance"):
        print(f"Your current balance is {balance}")

doTransaction(balance)

