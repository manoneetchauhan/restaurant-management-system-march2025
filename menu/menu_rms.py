from view_menu.view_menu_rms import view_menu
from table.table_booking import book_table
from order.myorder import take_order
from bill.generate_bill import view_bill

def main_menu(username):
    while True:
        print(f"Main Menu (Welcome, {username})")
        print("1. View Menu")
        print("2. Booking Table")
        print("3. My Order")
        print("4. Bill")
        print("5. Logout")
        choice = input("Enter your choice: ")

        if choice == '1':
            view_menu()
        elif choice == '2':
            book_table(username)
        elif choice == '3':
            take_order(username)
        elif choice == '4':     
            view_bill(username)
        elif choice == '5':
            print("Logged out.")
            break
        else:
            print("Invalid choice!")