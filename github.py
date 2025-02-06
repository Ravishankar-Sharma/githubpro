import tkinter as tk
from tkinter import messagebox
import random
from PIL import Image, ImageTk
import os


# Data storage
name = []
phno = []
add = []
checkin = []
checkout = []
room = []
price = []
rc = []
p = []
roomno = []
custid = []
day = []
i = 0

# Create the main window
root = tk.Tk()
root.title("Hotel JaLsA ChhhH")
root.geometry("800x800")


def set_background(frame):
    frame.configure(bg="#2E3B55")
    for widget in frame.winfo_children():
        widget.configure(bg="#2E3B55", fg="white")


def add_scrollable_frame(frame):
    canvas = tk.Canvas(frame, bg="#2E3B55")
    scroll_y = tk.Scrollbar(frame, orient="vertical", command=canvas.yview)
    canvas.configure(yscrollcommand=scroll_y.set)

    scrollable_frame = tk.Frame(canvas, bg="#2E3B55")
    scrollable_frame.bind(
        "<Configure>",
        lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
    )

    canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
    canvas.grid(row=0, column=0, sticky="nsew")
    scroll_y.grid(row=0, column=1, sticky="ns")

    return scrollable_frame


def back_to_home():
    for widget in root.winfo_children():
        widget.destroy()
    create_home()


def create_home():
    home_frame = tk.Frame(root, bg="#2E3B55")
    home_frame.pack(padx=20, pady=20, fill="both", expand=True)

    # Load background image using relative path
    try:
        bg_image = Image.open("images/luxury-hotel-wallpaper-preview.jpg")
        bg_image = bg_image.resize((800, 800), Image.Resampling.LANCZOS)
        bg_image = ImageTk.PhotoImage(bg_image)

        bg_label = tk.Label(home_frame, image=bg_image)
        bg_label.image = bg_image
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except FileNotFoundError:
        print("Background image not found. Please add an image in the 'images' folder.")

    title = tk.Label(home_frame, text="WELCOME TO HOTEL JalsA ChhhH", font=("Helvetica", 24, "bold"), fg="white", bg="#2E3B55")
    title.pack(pady=20)

    # Buttons for navigation
    booking_btn = tk.Button(home_frame, text="Booking", width=20, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat", command=booking_screen)
    booking_btn.pack(pady=10)

    rooms_info_btn = tk.Button(home_frame, text="Rooms Info", width=20, font=("Arial", 14), bg="#2196F3", fg="white", relief="flat", command=rooms_info_screen)
    rooms_info_btn.pack(pady=10)

    restaurant_btn = tk.Button(home_frame, text="Room Service (Menu)", width=20, font=("Arial", 14), bg="#FFC107", fg="white", relief="flat", command=restaurant_screen)
    restaurant_btn.pack(pady=10)

    payment_btn = tk.Button(home_frame, text="Payment", width=20, font=("Arial", 14), bg="#FF5722", fg="white", relief="flat", command=payment_screen)
    payment_btn.pack(pady=10)

    record_btn = tk.Button(home_frame, text="Record", width=20, font=("Arial", 14), bg="#9C27B0", fg="white", relief="flat", command=record_screen)
    record_btn.pack(pady=10)

    exit_btn = tk.Button(home_frame, text="Exit", width=20, font=("Arial", 14), bg="#F44336", fg="white", relief="flat", command=root.quit)
    exit_btn.pack(pady=10)


def booking_screen():
    booking_frame = tk.Frame(root, bg="#2E3B55")
    booking_frame.pack(padx=20, pady=20, fill="both", expand=True)

    scrollable_frame = add_scrollable_frame(booking_frame)

    def submit_booking():
        global i
        customer_name = name_entry.get()
        customer_phone = phone_entry.get()
        customer_address = address_entry.get()

        if customer_name == "" or customer_phone == "" or customer_address == "":
            messagebox.showerror("Error", "Name, Phone No., and Address cannot be empty!")
            return

        name.append(customer_name)
        phno.append(customer_phone)
        add.append(customer_address)

        checkin_date = checkin_entry.get()
        checkout_date = checkout_entry.get()
        checkin.append(checkin_date)
        checkout.append(checkout_date)

        room_type = room_type_var.get()
        if room_type == "Standard Non-AC":
            price.append(3500)
        elif room_type == "Standard AC":
            price.append(4000)
        elif room_type == "3-Bed Non-AC":
            price.append(4500)
        elif room_type == "3-Bed AC":
            price.append(5000)

        room_no = random.randrange(300, 360)
        customer_id = random.randrange(10, 50)

        roomno.append(room_no)
        custid.append(customer_id)

        messagebox.showinfo("Success", f"Room booked successfully! Room No: {room_no}, Customer ID: {customer_id}")
        i += 1
        back_to_home()


    title_label = tk.Label(scrollable_frame, text="BOOKING ROOMS", font=("Helvetica", 18, "bold"), fg="white", bg="#2E3B55")
    title_label.pack(pady=10)

    name_label = tk.Label(scrollable_frame, text="Name:", font=("Arial", 14), fg="white", bg="#2E3B55")
    name_label.pack(pady=5)
    name_entry = tk.Entry(scrollable_frame, font=("Arial", 14))
    name_entry.pack(pady=5)

    phone_label = tk.Label(scrollable_frame, text="Phone No.:", font=("Arial", 14), fg="white", bg="#2E3B55")
    phone_label.pack(pady=5)
    phone_entry = tk.Entry(scrollable_frame, font=("Arial", 14))
    phone_entry.pack(pady=5)

    address_label = tk.Label(scrollable_frame, text="Address:", font=("Arial", 14), fg="white", bg="#2E3B55")
    address_label.pack(pady=5)
    address_entry = tk.Entry(scrollable_frame, font=("Arial", 14))
    address_entry.pack(pady=5)

    checkin_label = tk.Label(scrollable_frame, text="Check-In Date (DD/MM/YYYY):", font=("Arial", 14), fg="white", bg="#2E3B55")
    checkin_label.pack(pady=5)
    checkin_entry = tk.Entry(scrollable_frame, font=("Arial", 14))
    checkin_entry.pack(pady=5)

    checkout_label = tk.Label(scrollable_frame, text="Check-Out Date (DD/MM/YYYY):", font=("Arial", 14), fg="white", bg="#2E3B55")
    checkout_label.pack(pady=5)
    checkout_entry = tk.Entry(scrollable_frame, font=("Arial", 14))
    checkout_entry.pack(pady=5)

    room_type_var = tk.StringVar()
    room_type_var.set("Standard Non-AC")

    room_type_label = tk.Label(scrollable_frame, text="Room Type:", font=("Arial", 14), fg="white", bg="#2E3B55")
    room_type_label.pack(pady=5)
    room_type_menu = tk.OptionMenu(scrollable_frame, room_type_var, "Standard Non-AC", "Standard AC", "3-Bed Non-AC", "3-Bed AC")
    room_type_menu.pack(pady=5)

    submit_button = tk.Button(scrollable_frame, text="Submit Booking", width=20, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat", command=submit_booking)
    submit_button.pack(pady=10)

    back_button = tk.Button(scrollable_frame, text="Back", width=20, font=("Arial", 14), bg="#FF5722", fg="white", relief="flat", command=back_to_home)
    back_button.pack(pady=10)


# Rooms Info Screen
def rooms_info_screen():
    info_frame = tk.Frame(root, bg="#2E3B55")
    info_frame.pack(padx=20, pady=20, fill="both", expand=True)

    scrollable_frame = add_scrollable_frame(info_frame)

    title_label = tk.Label(scrollable_frame, text="ROOMS INFO", font=("Helvetica", 18, "bold"), fg="white", bg="#2E3B55")
    title_label.pack(pady=10)

    room_info = [
        ("Standard Non-AC", "1 Double Bed, Television, Telephone, Coffee table, Balcony, Attached Washroom"),
        ("Standard AC", "1 Double Bed, Television, Telephone, Coffee table, Balcony, Attached Washroom + AC"),
        ("3-Bed Non-AC", "1 Double Bed + 1 Single Bed, Television, Telephone, Coffee table, Balcony, Attached Washroom"),
        ("3-Bed AC", "1 Double Bed + 1 Single Bed, Television, Telephone, Coffee table, Balcony, Attached Washroom + AC")
    ]

    for room_type, description in room_info:
        room_label = tk.Label(scrollable_frame, text=f"{room_type}: {description}", font=("Arial", 14), fg="white", bg="#2E3B55")
        room_label.pack(pady=5)

    back_button = tk.Button(scrollable_frame, text="Back", width=20, font=("Arial", 14), bg="#FF5722", fg="white", relief="flat", command=back_to_home)
    back_button.pack(pady=10)


def restaurant_screen():
    restaurant_frame = tk.Frame(root, bg="#2E3B55")
    restaurant_frame.pack(padx=20, pady=20, fill="both", expand=True)

    scrollable_frame = add_scrollable_frame(restaurant_frame)

    title_label = tk.Label(scrollable_frame, text="ROOM SERVICE (MENU)", font=("Helvetica", 18, "bold"), fg="white", bg="#2E3B55")
    title_label.pack(pady=10)

    menu_items = {
        "Regular Tea": 20,
        "Masala Tea": 25,
        "Coffee": 25,
        "Cold Drink": 25,
        "Bread Butter": 30,
        "Bread Jam": 30,
        "Veg. Sandwich": 50,
        "Non-Veg. Sandwich": 60
    }

    item_var = tk.StringVar()
    item_var.set("Regular Tea")

    item_label = tk.Label(scrollable_frame, text="Select Item:", font=("Arial", 14), fg="white", bg="#2E3B55")
    item_label.pack(pady=5)

    item_menu = tk.OptionMenu(scrollable_frame, item_var, *menu_items.keys())
    item_menu.pack(pady=5)

    quantity_label = tk.Label(scrollable_frame, text="Enter Quantity:", font=("Arial", 14), fg="white", bg="#2E3B55")
    quantity_label.pack(pady=5)

    quantity_entry = tk.Entry(scrollable_frame, font=("Arial", 14))
    quantity_entry.pack(pady=5)

    def place_order():
        item = item_var.get()
        quantity = quantity_entry.get()
        if not quantity.isdigit() or int(quantity) <= 0:
            messagebox.showerror("Error", "Please enter a valid quantity!")
            return

        total_price = menu_items[item] * int(quantity)
        messagebox.showinfo("Order Placed", f"Your order for {item} x{quantity} has been placed. Total amount: ₹{total_price}")

    order_button = tk.Button(scrollable_frame, text="Place Order", width=20, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat", command=place_order)
    order_button.pack(pady=10)

    back_button = tk.Button(scrollable_frame, text="Back", width=20, font=("Arial", 14), bg="#FF5722", fg="white", relief="flat", command=back_to_home)
    back_button.pack(pady=10)


def payment_screen():
    payment_frame = tk.Frame(root, bg="#2E3B55")
    payment_frame.pack(padx=20, pady=20, fill="both", expand=True)

    scrollable_frame = add_scrollable_frame(payment_frame)

    title_label = tk.Label(scrollable_frame, text="PAYMENT", font=("Helvetica", 18, "bold"), fg="white", bg="#2E3B55")
    title_label.pack(pady=10)

    def make_payment():
        amount = float(payment_entry.get())
        if amount <= 0:
            messagebox.showerror("Error", "Amount must be greater than zero!")
            return
        messagebox.showinfo("Payment Successful", f"₹{amount} has been successfully paid.")
        back_to_home()

    amount_label = tk.Label(scrollable_frame, text="Enter Payment Amount (₹):", font=("Arial", 14), fg="white", bg="#2E3B55")
    amount_label.pack(pady=5)

    payment_entry = tk.Entry(scrollable_frame, font=("Arial", 14))
    payment_entry.pack(pady=5)

    pay_button = tk.Button(scrollable_frame, text="Make Payment", width=20, font=("Arial", 14), bg="#4CAF50", fg="white", relief="flat", command=make_payment)
    pay_button.pack(pady=10)

    back_button = tk.Button(scrollable_frame, text="Back", width=20, font=("Arial", 14), bg="#FF5722", fg="white", relief="flat", command=back_to_home)
    back_button.pack(pady=10)


def record_screen():
    record_frame = tk.Frame(root, bg="#2E3B55")
    record_frame.pack(padx=20, pady=20, fill="both", expand=True)

    scrollable_frame = add_scrollable_frame(record_frame)

    title_label = tk.Label(scrollable_frame, text="RECORDS", font=("Helvetica", 18, "bold"), fg="white", bg="#2E3B55")
    title_label.pack(pady=10)

    for i in range(len(name)):
        record_text = f"Customer Name: {name[i]}, Room No: {roomno[i]}, Customer ID: {custid[i]}, Check-In: {checkin[i]}, Check-Out: {checkout[i]}"
        record_label = tk.Label(scrollable_frame, text=record_text, font=("Arial", 12), fg="white", bg="#2E3B55")
        record_label.pack(pady=5)

    back_button = tk.Button(scrollable_frame, text="Back", width=20, font=("Arial", 14), bg="#FF5722", fg="white", relief="flat", command=back_to_home)
    back_button.pack(pady=10)


if __name__ == "__main__":
    create_home()
    root.mainloop()
