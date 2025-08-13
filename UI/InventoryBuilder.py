from OurDisplay import *
import DatabaseUtility as DB

card_index = 0
food_type_map = {}
sub_menu_map = {}

# ---------- STEP 1: Create Input Fields at Top ----------
def create_input_fields():
    global entry_name, entry_amount, entry_purchase_price, entry_sell_price, cbo_food_type, cbo_sub_menus

    CTkLabel(Window, text="Name", font=('Arial', 14)).place(x=30, y=20)
    CTkLabel(Window, text="Amount", font=('Arial', 14)).place(x=180, y=20)
    CTkLabel(Window, text="Purchase $", font=('Arial', 14)).place(x=280, y=20)
    CTkLabel(Window, text="Sell $", font=('Arial', 14)).place(x=380, y=20)
    CTkLabel(Window, text="Type", font=('Arial', 14)).place(x=480, y=20)
    CTkLabel(Window, text="Sub Menu", font=('Arial', 14)).place(x=640, y=20)

    entry_name = CTkEntry(Window, width=120)
    entry_amount = CTkEntry(Window, width=70)
    entry_purchase_price = CTkEntry(Window, width=70)
    entry_sell_price = CTkEntry(Window, width=70)

    entry_name.place(x=30, y=50)
    entry_amount.place(x=180, y=50)
    entry_purchase_price.place(x=280, y=50)
    entry_sell_price.place(x=380, y=50)

    # Dropdown for food type
    global food_type_map
    food_type_map = DB.get_food_types()  # {1: 'Dairy', 2: 'Meat', ...}
    cbo_food_type = CTkComboBox(Window, values=list(food_type_map.values()), width=130)
    cbo_food_type.place(x=480, y=50)
    cbo_food_type.set("Select Type")

    # Dropdown for SubMenu link
    global sub_menu_map
    sub_menu_map = DB.get_sub_menus()
    sub_menu_names = ["None"]
    sub_menu_names += [item["name"] for item in sub_menu_map.values()]
    cbo_sub_menus = CTkComboBox(Window, values=sub_menu_names, width=150)
    cbo_sub_menus.place(x=640, y=50)
    cbo_sub_menus.set("Link Sub Menu")

    # Add button
    CTkButton(Window, text="Add Food", command=submit_food_item).place(x=820, y=50)


    CTkButton(Window,
        font=('Arial', 14),
        text="Return To Mangemant Page",
        command=open_Mgmt_ui
        ).place(x=770, y=568)

# ---------- STEP 2: Submit a New Food ----------
def submit_food_item():
    global card_index

    name = entry_name.get()
    amount = entry_amount.get()
    purchase_price = entry_purchase_price.get()
    sell_price = entry_sell_price.get()
    type_name = cbo_food_type.get()
    sub_menu_name = cbo_sub_menus.get()

    if not all([name, amount, purchase_price, sell_price, type_name, sub_menu_name]) or type_name == "Select Type" or sub_menu_name == "Link Sub Menu":
        
        ### Need to add a popup here to warn if not a valid entry
        print("Please fill all fields.")
        return

    try:
        amount = float(amount)
        purchase_price = float(purchase_price)
        sell_price = float(sell_price)
        type_id = {v: k for k, v in food_type_map.items()}[type_name]
        sub_menu_id = DB.get_sub_menu_id(sub_menu_name)
    except Exception as e:
        print("Invalid input:", e)
        return

    food_id = DB.insert_food(name, amount, purchase_price, sell_price, type_id, sub_menu_id)
    food_data = DB.get_food_by_id(food_id)

    messagebox.showinfo("Action Complete", f"{name} has been added to the inventory")

    if food_data:
        display_food_card(food_data, card_index, scroll_frame)
        card_index += 1

    clear_fields()


def clear_fields():

    entry_name.delete(0,'end')
    entry_amount.delete(0,'end')
    entry_purchase_price.delete(0,'end')
    entry_sell_price.delete(0,'end')

    cbo_food_type.set("Select Type")
    cbo_sub_menus.set("Link Sub Menu")


# ---------- STEP 3: Display a Single Food Card ----------
def display_food_card(data, index, parent_frame):
    card = CTkFrame(
        parent_frame,
        width=920,
        height=120, 
        corner_radius=15, 
        border_width=2, 
        border_color="black")
    card.grid(row=index, column=0, padx=20, pady=10, sticky="w")

    # ID label
    CTkLabel(card, 
             text=f"ID: {data['id']}", 
             font=('Arial', 12, 'bold')).place(x=20, y=20)

    # Entry fields
    entry_name = CTkEntry(card, width=120)
    entry_name.insert(0, data['name'])
    entry_name.place(x=20, y=50)

    entry_amount = CTkEntry(card, width=70)
    entry_amount.insert(0, str(data['amount']))
    entry_amount.place(x=160, y=50)

    entry_purchase = CTkEntry(card, width=70)
    entry_purchase.insert(0, str(data['purchase']))
    entry_purchase.place(x=250, y=50)

    entry_sell = CTkEntry(card, width=70)
    entry_sell.insert(0, str(data['sell']))
    entry_sell.place(x=340, y=50)

    # ComboBox for Food Type
    type_name = food_type_map.get(data['type_id'], "Unknown")
    entry_type = CTkComboBox(card, values=list(food_type_map.values()), width=130)
    entry_type.set(type_name)
    entry_type.place(x=430, y=50)

    # Combobox for SubMenu
    food_id = data['id']
    sub_menu_name = DB.get_food_card_sub_menu(food_id)
    if sub_menu_name == None:
        sub_menu_name = "None"
    sub_menu_names = ["None"]
    sub_menu_names += [item["name"] for item in sub_menu_map.values()]
    entry_sub_menu = CTkComboBox(card, values=sub_menu_names, width=150)
    entry_sub_menu.set(sub_menu_name)
    entry_sub_menu.place(x=580, y=50)

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
            DB.update_food_sub_menu(data['id'], entry_sub_menu.get())
            print(f"Food ID {data['id']} updated.")
        except Exception as e:
            print("Update failed:", e)

        messagebox.showinfo("Update Complete", f" Item {data['id']}: {data['name']}\nhas been updated")

    CTkButton(card, text="Update", command=update_action).place(x=750, y=30)

    # Delete button
    def delete_action():
        DB.delete_food_by_id(data['id'])
        refresh_cards()

    CTkButton(card, text="Delete", fg_color="red", command=delete_action).place(x=750, y=60)


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
scroll_frame = CTkScrollableFrame(Window, width=950, height=450)
scroll_frame.place(x=25, y=100)

# Load and display all food cards on page load
all_foods = DB.get_all_foods()
for i, food in enumerate(all_foods):
    display_food_card(food, i, scroll_frame)
    card_index += 1

Window.mainloop()
