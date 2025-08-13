#Import TruckBytes Standard UI options
from OurDisplay import *

#Import database utilities
import DatabaseUtility as DB

import subprocess
import tkinter as tk

from OrderItem import OrderItem

# get customerID passed from Loyalty.py or fallback to 0
try:
    customerID = int(sys.argv[1])
except (IndexError, ValueError):
    customerID = 0
print(customerID)

#Variables to link to SQL
lblOrderTotal = None
SQLTotal = 0  ### This should be an aggregate of

SQLSubMenuName= "SQL Sub Menu Name"
CurrentOrder = "$: "

"This needs to display which buttons were pushed"
SQLItemOrdered = ""

OrderItemsList = []
OrderDisplay = None



# Iterative buttons dimensions
button_width = 200
button_height = 120
y_padding = 25






def open_credit_ui():

    orderID = DB.build_order(OrderItemsList, SQLTotal, customerID)

    """Open CreditCard.py and pass the current total as an argument."""
    subprocess.Popen(['python', 'UI/CreditCard.py', str(SQLTotal), str(orderID), str(customerID)])
    Window.destroy()


def open_sub_menu_delayed(ItemID):
    Window.after(200, lambda: open_sub_menu(ItemID))


def open_sub_menu(ItemID):

    PopUpMenu = Toplevel()
    PopUpMenu.transient(Window)

    MenuItemType = DB.get_menu_item_type(ItemID)

    is_drink = MenuItemType == "Drink"
    has_subMenu = DB.get_sub_menu_name(ItemID)

    if has_subMenu is None:
        has_subMenu = False
    else:
        has_subMenu = True

    checkboxes = []
    
    scale = Window.tk.call('tk', 'scaling')

    base_width = Window.winfo_width()
    base_height = Window.winfo_height()

    scaled_width = int(base_width * scale * .3)
    scaled_height = int(base_height * scale * .5)

    # Get sizes
    main_x = Window.winfo_x()
    main_y = Window.winfo_y()
    main_width = Window.winfo_width()
    main_height = Window.winfo_height()

    # Calculate centered position relative to main window
    x = main_x + (main_width // 2) - (scaled_width // 2)
    y = main_y + (main_height // 2) - (scaled_height // 2)

    PopUpMenu.geometry(f"{scaled_width}x{scaled_height}+{x}+{y}") 
    PopUpMenu.resizable(False, False)


    #Gets the Menu Item Description
    MenuItemDescription = DB.get_menu_item_description(ItemID)
    Description = CTkLabel(PopUpMenu,
                           width=360,
                           height=10,
                           text=MenuItemDescription)
    if has_subMenu:
        Description.place(x=15,y=15)
    else:
        Description.place(x=15, y=40)

    if has_subMenu:
        # Scrollable frame for checkboxes
        scroll_frame = CTkScrollableFrame(PopUpMenu, width=360, height=60)
        scroll_frame.place(x=15, y=45)


        # Fetch submenu items
        SubMenuRows = DB.get_sub_menu_items(ItemID)

        for i, row in enumerate(SubMenuRows):
            item_id = row[0]
            item_name = row[1]
            portion_price = row[2]

            if is_drink:
                checkbox = CTkCheckBox(scroll_frame, text=f"{item_name}")
            else:
                checkbox = CTkCheckBox(scroll_frame, text=f"(${portion_price}) {item_name}")
            checkbox.item_id = item_id
            checkbox.item_name = item_name
            checkbox.portion_price = portion_price
            
            row_num = i // 2   # Every two items, start a new row
            col_num = i % 2    # 0 or 1 (column 1 or column 2)

            checkbox.grid(row=row_num,
                        column=col_num,
                        padx=10,
                        pady=5, 
                        sticky="w")
            checkboxes.append(checkbox)
    else:
        pass
        #PopUpMenu.geometry(f"400x200+{x}+{y}")

    #Add Item button
    add_item = CTkButton(PopUpMenu,
                         text="Add Item",
                         font=font1,
                         width=button_width,
                         height=80,
                         command=lambda: add_selected_items(PopUpMenu, checkboxes, is_drink, ItemID))
    # if has_subMenu:
    #     add_item.place(x=180,y=295)
    # else:
    #     add_item.place(x=180,y=100)

    add_item.place(x=180,y=295)

    # Close button
    my_button = CTkButton(PopUpMenu,
                          text="Cancel",
                          font=font1,
                          width=80,
                          height=80,
                          command=PopUpMenu.destroy)
    # if has_subMenu:
    #     my_button.place(x=55,y=295)
    # else:
    #     my_button.place(x=55,y=100)

    my_button.place(x=55,y=295)

    # Update sub menu name
    if has_subMenu:
        sub_menu_name = DB.get_sub_menu_name(ItemID)
        PopUpMenu.title("This Is The "+sub_menu_name+ " Menu")

    PopUpMenu.grab_set()
    PopUpMenu.focus_force()
    PopUpMenu.transient(Window)



def add_side_item(ItemID):
    global OrderDisplay, SQLTotal

    order_item = OrderItem()
    order_item.set_id(ItemID)
    order_item.set_name(DB.get_menu_item_name(ItemID))
    order_item.set_price(DB.get_menu_item_price(ItemID))

    OrderItemsList.append(order_item)

    if OrderDisplay:
        OrderDisplay.configure(state="normal")
        OrderDisplay.insert("end", f"{order_item.get_name()}  ${order_item.get_price():.2f}\n", "bold")
        OrderDisplay.insert("end", "\n")
        OrderDisplay.configure(state="disabled")

    SQLTotal += order_item.get_price()
    update_order_total(SQLTotal)



def add_selected_items(PopUpMenu, checkboxes, is_drink, ItemID):

    global OrderDisplay, SQLTotal, lblOrderTotal
    
    order_item = OrderItem()
    order_item.set_id(ItemID)
    order_item.set_name(DB.get_menu_item_name(ItemID))

    item_price = 0

    for checkbox in checkboxes:
        if checkbox.get():
            order_item.add_food_item(checkbox.item_id, checkbox.item_name)
            if not is_drink:
                item_price += checkbox.portion_price

    if is_drink:
        for checkbox in checkboxes:
            if checkbox.get():
                item_price += DB.get_menu_item_price(ItemID)
    else:
        item_price += DB.get_menu_item_price(ItemID)

    order_item.set_price(item_price)

    OrderItemsList.append(order_item)

    if OrderDisplay:
        OrderDisplay.configure(state="normal")
        OrderDisplay.insert("end", f"{order_item.get_name()}  ${order_item.get_price():.2f}\n", "bold")

        for food in order_item.m_aFoodItems:
            OrderDisplay.insert("end", f"   {food['name']}\n")
        OrderDisplay.insert("end", "\n")

        OrderDisplay.configure(state="disabled")

    SQLTotal += order_item.get_price()

    update_order_total(SQLTotal)

    PopUpMenu.destroy()



def remove_last_item():
    global OrderItemsList, OrderDisplay, SQLTotal, lblOrderTotal

    if OrderItemsList:
        last_item = OrderItemsList.pop()  # Remove the last order item

        SQLTotal -= last_item.get_price()
        update_order_total(SQLTotal)
        
        # Clear and re-display remaining items
        OrderDisplay.configure(state="normal")
        OrderDisplay.delete("1.0", "end")

        for order_item in OrderItemsList:
            OrderDisplay.insert("end", f"{order_item.get_name()}  ${order_item.get_price():.2f}\n", "bold")
            for food in order_item.m_aFoodItems:
                OrderDisplay.insert("end", f"   {food['name']}\n")
            OrderDisplay.insert("end", "\n")
        OrderDisplay.configure(state="disabled")




def update_order_total(SQLTotal):
    global lblOrderTotal

    lblOrderTotal.configure(text=f"Your Total: ${SQLTotal:.2f}")




def create_basic_ui():

    global lblOrderTotal

    CTkLabel(Window,
             text="Welcome To The Ordering Page",
             font=titleFont
             ).place(x=108,y=40)
    

    lblOrderTotal = CTkLabel(Window,
             text=f"Your Total: ${SQLTotal:.2f}",
             font=('Arial',20))
    lblOrderTotal.place(x=735,y=525)


    global OrderDisplay
    OrderDisplay = CTkTextbox(Window,
                              font=('Arial', 20),
                              width=210,
                              height=300)
    OrderDisplay.configure(state="disabled")
    OrderDisplay.place(x=730,y=125)

    # Create a bold font
    bold_font = tkfont.Font(family="Arial", size=15, weight="bold")
    OrderDisplay._textbox.tag_configure("bold", font=bold_font)


    CTkButton(Window, text="Place Order",
              font=('Arial',24),
              width= button_width,
              height=50,
              command=open_credit_ui
              ).place(x=735,y=45)
    
    CTkButton(Window,
              text="Remove Last",
              font=('Arial',24),
              width= button_width,
              height=50,
              command=remove_last_item
              ).place(x=735,y=445)



    #scrollable frame for menu items
    scroll_frame = CTkScrollableFrame(Window,
                                      width=470,
                                      height=450)
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

        button = CTkButton(scroll_frame, font=('Arial', 20),
                           text=ItemName,
                           width=button_width,
                           height=button_height,
                           command=lambda i=ItemID: open_sub_menu(i))
        
        button.grid(row=row, column=col, padx=15, pady=15)
        buttons.append(button)



#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
create_basic_ui()




#Create mainloop to run program
Window.mainloop()