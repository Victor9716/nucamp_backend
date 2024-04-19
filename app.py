from banking_pkg.account import show_balance, deposit, withdraw, logout

def atm_menu(name):
    print("")
    print("          === Automated Teller Machine ===          ")
    print("User: " + name)
    print("------------------------------------------")
    print("| 1.    Balance     | 2.    Deposit      |")
    print("------------------------------------------")
    print("------------------------------------------")
    print("| 3.    Withdraw    | 4.    Logout       |")
    print("------------------------------------------")

print("    === Automated Teller Machine ===    ")
name  = input("Enter your name: ")
pin = input("Enter  your PIN:   ")
balance = 0
print("Welcome, " + name + "! Your initial balance is $" + str(balance) + ".")

while True:
    name_to_validate = input("Enter name to Login: ")
    pin_to_validate = input("Enter PIN:           ")

    if name_to_validate == name and pin_to_validate== pin:
        print("Login Successful")
        break
    else:
        print("Invalid Credentials!")
# ATM menu

while True:
    atm_menu(name)
    option = input("Choose an option: ")

    if option == "1":
        show_balance(balance)
    elif option == "2":
        balance = deposit(balance)
        show_balance(balance)
    elif option == "3":
        new_balance = withdraw(balance)
        if new_balance == balance:
            print("Insufficient funds.")
        else:
            balance = new_balance
            show_balance(balance)
    elif option == "4":
        logout(name)
        break
    else:
        print("Invalid Option! Please try again.")


