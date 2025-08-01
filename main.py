from user.user_rms import signup, login
from menu.menu_rms import main_menu

def main():
    while True:
        print("\n**** Welcome to Marvel Restaurant ****")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            signup()
        elif choice == "2":
            username = login()
            if username:
                main_menu(username)
        elif choice == "3":
            print("EXIT!")
            break
        else:
            print("Invalid choice! Try again.")

main()