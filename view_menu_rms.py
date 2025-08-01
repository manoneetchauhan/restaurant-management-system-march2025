
from view_menu.menudata import menu

def view_menu():

    print("---MENU---")
    for category, items in menu.items():
        print(f"\n{category}:")
        for item, price in items.items():
            print(f" {item}: ₹ {price}")