class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def change_password(self, passsword):
        """Change the user's password."""
        self.password = passsword
        print("Your password has been changed to", self.password)

user1 = User("Jane", "jane@nucamp.co", "janepassword")
print(f"User Jane's password is {user1.password}")
user1.change_password("bestpassword")