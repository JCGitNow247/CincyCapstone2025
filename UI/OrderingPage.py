#Import TruckBytes Standard UI options
from OurDisplay import *

#pip3 install mariadb
import mariadb


#Variables to link to SQL
SQLTotal = "Your Total"
Item1 = "SQL Item1"
Item2 = "SQL Item2"
Item3 = "SQL Item3"
Item4 = "SQL Item4"
Item5 = "SQL Item5"
Item6 = "SQL Item6"
SQLSubMenuName= "SQL Sub Menu Name"


"""
Connecting to the DB section
"""
dictMenuItems = {}
intMenuItemIndex = 0

# Add SQL connection credentials for your SQL Server stuff
"""
I created a separate user from my root called 'truckbytesdev' with password 'tb001'
and granted permissions for database connections, highly recommended
"""
conn = mariadb.connect(

    host="localhost",
    user="truckbytesdev",
    password="tb001",
    database="dbTruckBytes"
)

cursor = conn.cursor()

cursor.execute('SELECT MenuItemID, MenuItemName FROM VMenuItems ORDER BY MenuType')

dictMenuItemsRows = cursor.fetchall()

for row in dictMenuItemsRows:

    MenuItemID = row[0]
    MenuItemName = row[1]

    dictMenuItems[intMenuItemIndex] = {

        "id": MenuItemID,
        "name": MenuItemName
    }

    intMenuItemIndex += 1


CurrentOrder = "$: "

"This needs to display which buttons were pushed"
SQLItemOrdered = "SQL Item Ordered"



def open_sub_menu(ItemID):
    PopUpMenu = Toplevel()
    #PopUpMenu.geometry("1200x1000")
    PopUpMenu.geometry("712x610+560+490")
    #PopUpMenu.title("This is the "+ SQLSubMenuName + " Submenu")
    PopUpMenu.title("This is the "+ SQLSubMenuName + " Submenu")
    PopUpMenu.minsize(width=300, height=300)
    #PopUpMenu.maxsize(width=350, height=315)


 

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
    cursor.execute('SELECT SubMenuItem FROM VSubMenuItems WHERE MenuItem = ?', (ItemID,))
    rows = cursor.fetchall()

    checkboxes = []
    for i, row in enumerate(rows):
        item_name = row[0]
        checkbox = CTkCheckBox(scroll_frame, text=item_name)
        
        row_num = i // 2   # Every two items, start a new row
        col_num = i % 2    # 0 or 1 (column 1 or column 2)

        checkbox.grid(row=row_num, column=col_num, padx=10, pady=5, sticky="w")
        checkboxes.append(checkbox)

    # Close button
    my_button = CTkButton(PopUpMenu, text="close", font=('Arial',20), width=200, height=50, command=PopUpMenu.destroy)
    my_button.place(x=75,y=250)

    # Update sub menu name
    cursor.execute('SELECT SubMenu FROM VSubMenuName WHERE MenuItem = ?', (ItemID,))
    #cursor.execute('SELECT SubMenu FROM VSubMenuName WHERE MenuItem = ?', ("This is the "+ItemID+" submenu",))

    row = cursor.fetchone()

    sub_menu_name = row[0]

    PopUpMenu.title("This is the "+sub_menu_name+ " submenu")



def CreateLabel():

    #Label of the page
    lblTitle = CTkLabel(Window, text="Welcome To The Ordering Page", font=('Arial', 32, 'bold'))
    lblTitle.place(x=98,y=40)

    #Label to Show What Has Been Ordered
    lblOrdered = CTkLabel(Window, text=SQLItemOrdered, font=('Arial',20))
    lblOrdered.place(x=708,y=125)

    #Label to display Total
    lblTotal = CTkLabel(Window, text=SQLTotal, font=('Arial',20))
    lblTotal.place(x=735,y=525)



def CreateButtons():
    #Button
    btnPlaceOrder = CTkButton(Window, text="Place Order", font=('Arial',20), width=200, height=50, command=open_credit_ui)
    btnPlaceOrder.place(x=735,y=45)

    btnSubmit = CTkButton(Window, text="Remove Last", font=('Arial',20), width=200, height=50)
    btnSubmit.place(x=735,y=445)

    # Iterative buttons dimensions
    button_width = 200
    button_height = 120
    y_padding = 25

    #scrollable frame for menu items
    scroll_frame = CTkScrollableFrame(Window, width=600, height=450)
    scroll_frame.place(x=50, y=100)

    # Iterative buttons placement
    x_positions = [0, 300]  # column 1 and column 2
    y_step = button_height + y_padding

    buttons = []  # Store buttons in case you want to reference or destroy them later

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



#Create mainloop to run program
Window.mainloop()