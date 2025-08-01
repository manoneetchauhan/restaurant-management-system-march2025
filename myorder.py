import json
from view_menu.menudata import menu

def take_order(username):
    print(f"\n--- Welcome {username}, here is the Menu ---")

    order = []

    while True:
        print("\nAvailable Categories:")
        for category in menu:
            print(f"- {category.capitalize()}")

        category = input("\nEnter category: ").strip().lower()

        if category not in menu:
            print("Invalid category selected.")
            continue

        print(f"\nAvailable items in {category.capitalize()}:")

        item_lookup = {}
        for item_name, price in menu[category].items():
            print(f"- {item_name}: ₹{price}")
            item_lookup[item_name.lower()] = item_name

        item_input = input("\nEnter item name to order: ").strip().lower()
        if item_input not in item_lookup:
            print("Invalid item selected.")
            continue

        actual_item = item_lookup[item_input]
        base_price = menu[category][actual_item]

        portion = input("Do you want full or half portion? (full/half): ").strip().lower()
        if portion not in ["full", "half"]:
            print("Invalid portion type. Defaulting to full.")
            portion = "full"

        try:
            quantity = int(input("Enter quantity: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        price_per_item = base_price if portion == "full" else base_price / 2
        total_price = price_per_item * quantity

        order.append({
            "username": username,
            "category": category,
            "item": actual_item,
            "portion": portion,
            "quantity": quantity,
            "price_per_item": price_per_item,
            "total_price": total_price
        })

        print(f"{actual_item} ({portion}) x {quantity} = ₹{total_price:.2f}")

        more = input("\nDo you want to add more items? (yes/no): ").strip().lower()
        if more != "yes":
            break

    with open("orderdata.json", "w") as f:
        json.dump(order, f, indent=4)

    print("\nYour order has been saved! Thank you for ordering.")
