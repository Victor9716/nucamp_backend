while True:
    print("1. Number One")
    print("2. Number Two")
    print("3. Break out of infinite loop")
    option = input("Pick out an option: ")
    if  option == '1':
        print("you chose 1")
    elif option == "2":
        print("You chose 2")
    elif option == "3":
        print("Leaving the loop!")
        break
    else:
        print("Invalid command")
print("You have left the loop")