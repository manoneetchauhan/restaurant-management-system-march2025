import json
from menu.menu_rms import main_menu

userdata_file = "userdata.json"

def load_users():
    try:
        with open(userdata_file, "r") as f:
            return json.load(f)
    except:
        return []

def save_users(users):
    with open(userdata_file, "w") as f:
        json.dump(users, f, indent=4)

def signup():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")
    
    for user in users:
        if user['username'] == username:
            print("Username already exists!")
            return
    
    users.append({"username": username, "password": password})
    save_users(users)
    print("SignUp successful!")

def login():
    users = load_users()
    username = input("Username: ")
    password = input("Password: ")

    for user in users:
        if user['username'] == username and user['password'] == password:
            print("LogIn successful!")
            main_menu(username)
            return
    print("Invalid username or password!")
    return None
