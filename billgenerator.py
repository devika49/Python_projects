import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

# Data
itemp = {'Soap': 30, 'Rice': 50, 'Oil': 175, 'Bread': 26.5, 'Jam': 20}
ordered_items = []

# Functions
def add_item():
    try:
        item_name = item_choice.get().capitalize()
        quantity = int(quantity_entry.get())
        if item_name not in itemp or quantity <= 0:
            raise ValueError

        item_price = itemp[item_name]
        total_price = item_price * quantity

        ordered_items.append((item_name, item_price, quantity, total_price))
        update_bill()

        # Clear the input fields after adding the item
        item_choice.delete(0, tk.END)
        quantity_entry.delete(0, tk.END)

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid item name and quantity.")

def update_bill():
    bill_text.config(state=tk.NORMAL)
    bill_text.delete('1.0', tk.END)
    bill_text.insert(tk.END, "Retail Bill System\n","center")
    bill_text.insert(tk.END, "...............................................\n")
    bill_text.insert(tk.END, "Name\tPrice\tQuantity\tTotal\n","left")
    bill_text.insert(tk.END, "...............................................\n")

    total_amount = 0
    for item_name, item_price, quantity, total_price in ordered_items:
        bill_text.insert(tk.END, f"{item_name}\t{item_price}\t{quantity}\t{total_price}\n")
        total_amount += total_price

    bill_text.insert(tk.END, "...............................................\n")
    bill_text.insert(tk.END, f"Total Amount: {total_amount}\n")
    bill_text.config(state=tk.DISABLED)

def clear_order():
    ordered_items.clear()
    update_bill()

# GUI Setup
root = tk.Tk()
root.title("Retail Bill System")
root.geometry("700x600")
root.resizable(False, False)

# Load background image
background_image = Image.open("./background.jpg")
background_photo = ImageTk.PhotoImage(background_image)

# Create a canvas
canvas = tk.Canvas(root, width=700, height=900)
canvas.pack(fill="both", expand=True)

# Set the background image on the canvas
canvas.create_image(0, 0, image=background_photo, anchor="nw")

# Sidebar for available items
sidebar = tk.Frame(canvas, width=200)
sidebar.place(x=0, y=0, relheight=1)

sidebar_label = tk.Label(sidebar, text="Available Items", font=("Arial", 16, "bold"), pady=10)
sidebar_label.pack()

for item_name, price in itemp.items():
    item_label = tk.Label(sidebar, text=f"{item_name} - Rs.{price}", font=("Arial", 14),anchor='w')
    item_label.pack(fill='x')

# Main content frame
main_frame = tk.Frame(canvas, bg='#f0f0f0')
main_frame.place(x=200, y=0, relwidth=0.75, relheight=1)

header = tk.Label(main_frame, text="Retail Bill System", font=("Arial", 24, "bold"), bg='#f0f0f0', pady=20)
header.pack()

frame = tk.Frame(main_frame, bg='#f0f0f0')
frame.pack(pady=10)

item_label = tk.Label(frame, text="Enter the item:", font=("Arial", 14), bg='#f0f0f0')
item_label.grid(row=0, column=0, pady=5, sticky='e')

item_choice = tk.Entry(frame, font=("Arial", 14))
item_choice.grid(row=0, column=1, pady=5)

quantity_label = tk.Label(frame, text="Enter quantity:", font=("Arial", 14), bg='#f0f0f0')
quantity_label.grid(row=1, column=0, pady=5, sticky='e')

quantity_entry = tk.Entry(frame, font=("Arial", 14))
quantity_entry.grid(row=1, column=1, pady=5)

add_button = tk.Button(frame, text="Add Item", font=("Arial", 14), bg='#4CAF50', fg='white', command=add_item)
add_button.grid(row=2, column=0, columnspan=2, pady=10)

clear_button = tk.Button(frame, text="Clear Order", font=("Arial", 14), bg='#f44336', fg='white', command=clear_order)
clear_button.grid(row=3, column=0, columnspan=2, pady=10)

bill_text = tk.Text(main_frame, height=15, width=50, font=("Arial", 12))
bill_text.pack(pady=10)
bill_text.config(state=tk.DISABLED)

# Place the frames on the canvas
canvas.create_window(0, 0, anchor='nw', window=sidebar)
canvas.create_window(200, 0, anchor='nw', window=main_frame)

# Main loop
root.mainloop()
