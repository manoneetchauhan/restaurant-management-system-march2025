import json

booking_file = "bookings.json"

table_limits = {
    "Single Seat": 5,
    "Double Seats": 5,
    "Triple Seats": 5,
    "Four Seats": 5
}

people_to_table = {
    1: "Single Seat",
    2: "Double Seats",
    3: "Triple Seats",
    4: "Four Seats"
}

with open(booking_file, "w") as f:
        json.dump([], f)

def book_table(username):
    print("\n--- Table Booking ---")
    date = input("Enter date: ")
    time = input("Enter time: ")
    num_people = input("Enter number of people: ")

    if num_people not in people_to_table:
        print("\nInvalid number of people. Only 1 to 4 allowed.")
        return
    
    with open(booking_file, "r") as f:
        bookings = json.load(f)
        bookings = []

    new_booking = {
        "username": username,
        "date": date,
        "time": time,
        "people": num_people
    }

    bookings.append(new_booking)

    with open(booking_file, "w") as f:
        json.dump(bookings, f, indent=4)

    print(f"\n Table booked successfully for {username} on {date} at {time} for {num_people} people.")
