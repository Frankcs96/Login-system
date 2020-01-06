import Database
import sys

running = True


def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    users = Database.get_accounts()
    if users is not None:
        for accounts in users:
            if accounts.get("username") == username and accounts.get("password") == password:
                print("Welcome", username)
                sys.exit()

    print("Wrong account try again or create a new account")


def register():
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    Database.create_account(username, password)


while running:
    print("Welcome to World Of Pycraft!")
    print("Choose an option: ")
    print("1. Log in")
    print("2. Create account")
    print("3. Exit")
    userOption = int(input())
    if userOption == 1:
        login()
    if userOption == 2:
        register()

    if userOption == 3:
        running = False
