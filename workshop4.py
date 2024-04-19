class User:
    def __init__(self, name, pin, password):
        self.name = name
        self.pin = pin
        self.password = password

    def validate_password(self, password):
        return self.password == password

        """ Driver Code for Task 1 """
# if __name__ == "__main__":
#         # instantiate an object from the User Class
#         user1 = User("Bob", "1234567890", "mypass")
#         #  print details of the user
#         print(f"Name:  {user1.name}, Pin: {user1.pin}, Password: {user1.password}")
       
        """ Driver Code for Task 2 """
    def change_name(self, new_name):
        self.name = new_name

    def change_pin(self, new_pin):
        self.pin = new_pin

    def change_password(self, new_password):
        self.password = new_password
# if __name__ == "__main__":
#         # instantiate an object from the User Class
#         user1 = User("Bob", "1234567890", "mypass")
#         #  print details of the user
#         print(f"Name:  {user1.name}, Pin: {user1.pin}, Password: {user1.password}")
#         # Change values using methods
#         user1.change_name("Robert")
#         user1.change_pin("0987654321")
#         user1.change_password("newpass")
#         print(f"New Name:  {user1.name}, New Pin: {user1.pin}, New Password: {user1.password}")

    # bankUser class inherit from user class
class BankUser(User):
    def __init__(self, name, pin, password, balance=0):
        super().__init__(name, pin, password)
        self.balance = 0
        
        
    def show_balance(self):
        print("Balance: ", self.balance)
        
    def deposit(self, amount):
        self.balance += amount
            

    def withdrawal(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Balance!")
        
    def transfer_money(self, recpient, amount, pin):
             if self.pin == pin and amount <= self.balance:
                self.balance -= amount
                recpient.balance += amount
                return True
             return  False
         
    def request_money(self, recipient, amount, recipient_pin, password):
            if recipient_pin == recipient_pin and recipient.validate_password(password) and amount <= recipient.balance:
                self.balance -= amount
                recipient.balance += amount
                return True
            return False
# Driver code for task 5
if __name__ == "__main__":
        
        bank_user = BankUser("Alice", "1234567890", "password", 1000)
        recipient = BankUser("Bob", "5767", "pass", 500)
        second_user = BankUser("Victor", "2468", "pwd", 0)
        
        print(f"Name: {bank_user.name}, Pin: {bank_user.pin}, Password: {bank_user.password}, Balance: {bank_user.balance}")
            
# Testing transfer money
#         print(bank_user.transfer_money(recipient, 300, "1234567890")) # should return True
#         print(bank_user.balance) # should show 700
#         print(recipient.balance) # should show 800

#         print(bank_user.transfer_money(recipient, 1000, "9999")) # should return false
#         print(recipient.request_money(bank_user, 200, "5767", "pass"))  # Should return True

# # Testing request_money
#         print(recipient.request_money(bank_user, 200, "5767", "pass")) #should return true
#         print(bank_user.balance) # should show 900
#         print(recipient.balance) # should be 300

#         print(recipient.request_money(bank_user, 400,"1234", "wrongpass")) # shoould return false
        
# Additional Task 5 Instructions
        # second_user = BankUser("Victor", "2468", "pwd", 0)
        second_user.deposit(5000)
        print(second_user.balance) # should display 5000</s
        second_user.transfer_money(bank_user, 500, "pwd") # transfer 500 to bank_user
        print(second_user) # balance 4500
        print(bank_user.balance) # balance is 1400 
        if second_user.transfer_money(bank_user, 500, "pwd"):
            second_user.request_money(bank_user, 200, "2468", "pwd") 
        print(second_user.balance)
        print(bank_user.balance)      
    

#       # Driver code for task 4
# bank_user =  BankUser("Alice", "1234567890","password")
# bank_user.show_balance()
# bank_user.deposit(1000)
# bank_user.show_balance()
# bank_user.withdrawal(500)
# bank_user.show_balance()
# Testing the add_account method