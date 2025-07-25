#Import TruckBytes Standard UI options
from OurDisplay import *

#Import database utilities
import DatabaseUtility as DB

from OrderItem import OrderItem

#Variables to link to SQL
SQLTotal = "Your Total"
SQLSubMenuName= "SQL Sub Menu Name"

CurrentOrder = "$: "

"This needs to display which buttons were pushed"
SQLItemOrdered = "SQL Item Ordered"

OrderItemsList = []
OrderDisplay = None

def open_sub_menu(ItemID):

    MenuItemType = DB.get_menu_item_type(ItemID)
    if MenuItemType == "Sides":
        add_side_item(ItemID)
        return

    PopUpMenu = Toplevel()
    PopUpMenu.geometry("712x610+560+490")
    PopUpMenu.title("This is the "+ SQLSubMenuName + " Submenu")
    PopUpMenu.resizable(False, False)

    # Force layout update to get correct width and height
    PopUpMenu.update_idletasks()
    Window.update_idletasks()

    # Get sizes
    main_width = Window.winfo_width()
    main_height = Window.winfo_height()
    main_x = Window.winfo_x()
    main_y = Window.winfo_y()

    popup_width = PopUpMenu.winfo_width()
    popup_height = PopUpMenu.winfo_height()

    # Calculate centered position relative to main window
    x = main_x + (main_width // 2) - (popup_width // 2)
    y = main_y + (main_height // 2) - (popup_height // 2)

    PopUpMenu.geometry(f"+{x}+{y}")

    # Scrollable frame for checkboxes
    scroll_frame = CTkScrollableFrame(PopUpMenu, width=300, height=60)
    scroll_frame.place(x=15, y=20)

    # Fetch submenu items
    SubMenuRows = DB.get_sub_menu_items(ItemID)

    checkboxes = []
    for i, row in enumerate(SubMenuRows):
        item_id = row[0]
        item_name = row[1]
        checkbox = CTkCheckBox(scroll_frame, text=item_name)
        checkbox.item_id = item_id
        checkbox.item_name = item_name
        
        row_num = i // 2   # Every two items, start a new row
        col_num = i % 2    # 0 or 1 (column 1 or column 2)

        checkbox.grid(row=row_num, column=col_num, padx=10, pady=5, sticky="w")
        checkboxes.append(checkbox)

    #Add Item button
    add_item = CTkButton(PopUpMenu, text="Add Item", font=('Arial',20), width=200, height=50, command=lambda: add_selected_items(PopUpMenu, checkboxes, ItemID))
    add_item.place(x=75,y=250)

    # Close button
    my_button = CTkButton(PopUpMenu, text="close", font=('Arial',20), width=200, height=50, command=PopUpMenu.destroy)
    my_button.place(x=75,y=320)

    # Update sub menu name
    sub_menu_name = DB.get_sub_menu_name(ItemID)

    PopUpMenu.title("This is the "+sub_menu_name+ " menu")


def add_side_item(ItemID):
    global OrderDisplay

    order_item = OrderItem()
    order_item.set_id(ItemID)
    order_item.set_name(DB.get_menu_item_name(ItemID))

    OrderItemsList.append(order_item)

    if OrderDisplay:
        OrderDisplay.configure(state="normal")
        OrderDisplay.insert("end", f"{order_item.get_name()}\n", "bold")
        OrderDisplay.insert("end", "\n")
        OrderDisplay.configure(state="disabled")



def add_selected_items(PopUpMenu, checkboxes, ItemID):

    global OrderDisplay
    
    order_item = OrderItem()
    order_item.set_id(ItemID)
    order_item.set_name(DB.get_menu_item_name(ItemID))

    id = order_item.get_id()
    name = order_item.get_name()

    for checkbox in checkboxes:
        if checkbox.get():
            order_item.add_food_item(checkbox.item_id, checkbox.item_name)

    print(f"Menu Item ID: {id}, Menu Item Name: {name}")

    for item in order_item.m_aFoodItems:
        print(f"Food ID: {item['id']}, Name: {item['name']}")

    OrderItemsList.append(order_item)

    if OrderDisplay:
        OrderDisplay.configure(state="normal")
        OrderDisplay.insert("end", f"{order_item.get_name()}\n", "bold")

        for food in order_item.m_aFoodItems:
            OrderDisplay.insert("end", f"   {food['name']}\n")
        OrderDisplay.insert("end", "\n")

        OrderDisplay.configure(state="disabled")

    PopUpMenu.destroy()







def remove_last_item():
    global OrderItemsList, OrderDisplay

    if OrderItemsList:
        OrderItemsList.pop()  # Remove the last order item

        # Clear and re-display remaining items
        OrderDisplay.configure(state="normal")
        OrderDisplay.delete("1.0", "end")

        for order_item in OrderItemsList:
            OrderDisplay.insert("end", f"{order_item.get_name()}\n", "bold")
            for food in order_item.m_aFoodItems:
                OrderDisplay.insert("end", f"   {food['name']}\n")
            OrderDisplay.insert("end", "\n")

        OrderDisplay.configure(state="disabled")










def CreateTextBox():
    global OrderDisplay
    OrderDisplay = CTkTextbox(Window, font=('Arial', 20), width=300, height=300)
    OrderDisplay.configure(state="disabled")
    OrderDisplay.place(x=700,y=125)

    # Create a bold font
    bold_font = tkfont.Font(family="Arial", size=15, weight="bold")
    OrderDisplay._textbox.tag_configure("bold", font=bold_font)


def CreateLabel():
    CTkLabel(Window, text="Welcome To The Ordering Page", font=('Arial', 32, 'bold')).place(x=108,y=40)
    CTkLabel(Window, text=SQLItemOrdered, font=('Arial',20)).place(x=708,y=125)
    CTkLabel(Window, text=SQLTotal, font=('Arial',20)).place(x=735,y=525)

def CreateButtons():
    CTkButton(Window, text="Place Order", font=('Arial',20), width=200, height=50, command=open_credit_ui).place(x=735,y=45)
    CTkButton(Window, text="Remove Last", font=('Arial',20), width=200, height=50, command=remove_last_item).place(x=735,y=445)



    # Iterative buttons dimensions
    button_width = 200
    button_height = 120
    y_padding = 25

    #scrollable frame for menu items
    scroll_frame = CTkScrollableFrame(Window, width=470, height=450)
    scroll_frame.place(x=106, y=100)

    # Iterative buttons placement
    x_positions = [0, 300]  # column 1 and column 2
    y_step = button_height + y_padding

    buttons = []  # Store buttons in case you want to reference or destroy them later

    # Get menu items
    dictMenuItems = DB.get_menu_items()

    # Iterative dictMenuItems buttons
    for index, item in dictMenuItems.items():
        col = index % 2       # 0 or 1 (left/right column)
        row = index // 2      # increases every 2 items

        ItemID = item["id"]
        ItemName = item["name"]

        x = x_positions[col]
        y = row * y_step

        button = CTkButton(scroll_frame, font=('Arial', 20), text=ItemName, width=button_width, height=button_height, command=lambda i=ItemID: open_sub_menu(i))
        
        button.grid(row=row, column=col, padx=15, pady=15)
        buttons.append(button)



#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
CreateButtons()
CreateLabel()
CreateTextBox()



#Create mainloop to run program
Window.mainloop()