import json
from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Pay ₹{amount} in Cash.")

class UPIPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Scan the QR Code ₹{amount}.")

class CardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Swipe the CARD ₹{amount}.")

def view_bill(username):
        
        with open("orderdata.json", "r") as f:
            order = json.load(f)

        if not order:
            print("No order data found.")
            return

        print("\n ----- BILL -----\n")
        total_amount = 0

        for item in order:
            print(f"{item['item'].capitalize()} ({item['category'].capitalize()}) x {item['quantity']} = ₹{item['total_price']}")
            total_amount = total_amount + item["total_price"]


        print(f"Customer: {order[0]['username'].capitalize()}")
        print(f"Total Amount: ₹{total_amount}")

        print("\nSelect Payment Method:")
        print("1. Cash")
        print("2. UPI")
        print("3. Card")
        choice = input("Enter choice (1/2/3): ")

        if choice == "1":
            payment = CashPayment()
        elif choice == "2":
            payment = UPIPayment()
        elif choice == "3":
            payment = CardPayment()
        else:
            print("Invalid choice, defaulting to Cash.")
            payment = CashPayment()

        payment.pay(total_amount)
        
        print("Thank you for ordering!\n")
