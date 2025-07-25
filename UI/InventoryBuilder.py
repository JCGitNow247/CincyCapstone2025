from OurDisplay import *
import DatabaseUtility as DB

card_index = 0
food_type_map = {}

# ---------- STEP 1: Create Input Fields at Top ----------
def create_input_fields():
    global entry_name, entry_amount, entry_purchase_price, entry_sell_price, cbo_food_type

    CTkLabel(Window, text="Name", font=('Arial', 14)).place(x=30, y=20)
    CTkLabel(Window, text="Amount", font=('Arial', 14)).place(x=230, y=20)
    CTkLabel(Window, text="Purchase $", font=('Arial', 14)).place(x=380, y=20)
    CTkLabel(Window, text="Sell $", font=('Arial', 14)).place(x=530, y=20)
    CTkLabel(Window, text="Type", font=('Arial', 14)).place(x=680, y=20)

    entry_name = CTkEntry(Window, width=150)
    entry_amount = CTkEntry(Window, width=100)
    entry_purchase_price = CTkEntry(Window, width=100)
    entry_sell_price = CTkEntry(Window, width=100)

    entry_name.place(x=30, y=50)
    entry_amount.place(x=230, y=50)
    entry_purchase_price.place(x=380, y=50)
    entry_sell_price.place(x=530, y=50)

    # Dropdown for food type
    global food_type_map
    food_type_map = DB.get_food_types()  # {1: 'Dairy', 2: 'Meat', ...}
    cbo_food_type = CTkComboBox(Window, values=list(food_type_map.values()), width=150)
    cbo_food_type.place(x=680, y=50)
    cbo_food_type.set("Select Type")

    # Add button
    CTkButton(Window, text="Add Food", command=submit_food_item).place(x=875, y=50)


# ---------- STEP 2: Submit a New Food ----------
def submit_food_item():
    global card_index

    name = entry_name.get()
    amount = entry_amount.get()
    purchase_price = entry_purchase_price.get()
    sell_price = entry_sell_price.get()
    type_name = cbo_food_type.get()

    if not all([name, amount, purchase_price, sell_price, type_name]) or type_name == "Select Type":
        print("Please fill all fields.")
        return

    try:
        amount = float(amount)
        purchase_price = float(purchase_price)
        sell_price = float(sell_price)
        type_id = {v: k for k, v in food_type_map.items()}[type_name]
    except Exception as e:
        print("Invalid input:", e)
        return

    food_id = DB.insert_food(name, amount, purchase_price, sell_price, type_id)
    food_data = DB.get_food_by_id(food_id)

    if food_data:
        display_food_card(food_data, card_index, scroll_frame)
        card_index += 1


# ---------- STEP 3: Display a Single Food Card ----------
def display_food_card(data, index, parent_frame):
    card = CTkFrame(parent_frame, width=1000, height=160, corner_radius=15)
    card.grid(row=index, column=0, padx=20, pady=10, sticky="w")

    # Entry fields
    entry_name = CTkEntry(card, width=150)
    entry_name.insert(0, data['name'])
    entry_name.place(x=20, y=30)

    entry_amount = CTkEntry(card, width=100)
    entry_amount.insert(0, str(data['amount']))
    entry_amount.place(x=200, y=30)

    entry_purchase = CTkEntry(card, width=100)
    entry_purchase.insert(0, str(data['purchase']))
    entry_purchase.place(x=320, y=30)

    entry_sell = CTkEntry(card, width=100)
    entry_sell.insert(0, str(data['sell']))
    entry_sell.place(x=440, y=30)

    # ComboBox for Food Type
    type_name = food_type_map.get(data['type_id'], "Unknown")
    entry_type = CTkComboBox(card, values=list(food_type_map.values()), width=150)
    entry_type.set(type_name)
    entry_type.place(x=560, y=30)

    # Delete button
    def delete_action():
        DB.delete_food_by_id(data['id'])
        refresh_cards()

    CTkButton(card, text="Delete", fg_color="red", command=delete_action).place(x=740, y=60)

    # Update Button
    def update_action():
        try:
            updated_data = {
                "name": entry_name.get(),
                "amount": float(entry_amount.get()),
                "purchase": float(entry_purchase.get()),
                "sell": float(entry_sell.get()),
                "type_id": {v: k for k, v in food_type_map.items()}[entry_type.get()]
            }
            DB.update_food_item(data['id'], updated_data)
            print(f"Food ID {data['id']} updated.")
        except Exception as e:
            print("Update failed:", e)

    CTkButton(card, text="Update", command=update_action).place(x=740, y=30)
    CTkLabel(card, text=f"ID: {data['id']}", font=('Arial', 12, 'bold')).place(x=20, y=0)


# ---------- REFRESH FOOD CARDS ----------
def refresh_cards():
    for widget in scroll_frame.winfo_children():
        widget.destroy()

    all_foods = DB.get_all_foods()
    for i, food in enumerate(all_foods):
        display_food_card(food, i, scroll_frame)


# ---------- MAIN PROGRAM ----------
Create_Window()
Create_Menubar()
create_input_fields()

# Scrollable frame for food cards
scroll_frame = CTkScrollableFrame(Window, width=900, height=450)
scroll_frame.place(x=50, y=100)

# Load and display all food cards on page load
all_foods = DB.get_all_foods()
for i, food in enumerate(all_foods):
    display_food_card(food, i, scroll_frame)
    card_index += 1

Window.mainloop()
