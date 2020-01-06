import json
import os

accounts = []


def get_accounts():
    if os.path.exists("./accounts.json"):
        with open("accounts.json", 'r') as f:
            data = json.load(f)
            return data

    else:
        with open("accounts.json", "w") as f:
            f.write(str(accounts))


def create_account(username, password):
    users = get_accounts()
    exists = False
    if users is not None:
        for account in users:
            if account.get("username") == username:
                exists = True

        if not exists:
            new_user = {"username": username, "password": password}
            users.append(new_user)
            with open("accounts.json", "w") as f:
                f.write(json.dumps(users))
                print("Account created!.")
        else:
            print("User Already exists please try with another username")

    else:
        print("No file for database found creating... try to register again")
