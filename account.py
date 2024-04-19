def show_balance(balance):
    print("Your Current balance is: $", balance)

def deposit(balance):
    amount = float(input("Enter the amount to deposit: "))
    balance = amount +  balance
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount to withdraw: "))
    if amount >=  balance :
        print("Insufficient funds")
        return balance
    else:
        balance -= amount
        return balance

def logout(name):
    print("Goodbye", name)