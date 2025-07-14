#Import TruckBytes Standard UI options
from OurDisplay import *

# pip3 install pyodbc - used for connecting to an SQL Server
from pyodbc import *

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
MenuItems = {}
intMenuItemIndex = 0

# Add SQL connection credentials for your SQL Server stuff
conn = connect(

    'Driver={ODBC Driver 17 for SQL Server};'
    'SERVER=your_server;'
    'DATABASE=your_database;'
    'UID=your_UID;'
    'PWD=your_password'
)

cursor = conn.cursor()

cursor.execute('SELECT MenuItemName FROM VMenuItems')

rows = cursor.fetchall()

for row in rows:
    MenuItems[intMenuItemIndex] = row[0]
    intMenuItemIndex += 1


CurrentOrder = "$: "

"This needs to display which buttons were pushed"
SQLItemOrdered = "SQL Item Ordered"























#Do we need to create geometery based on number of items in the menu?

def open_sub_menu():
    PopUpMenu = Toplevel()
    PopUpMenu.geometry("1200x1000")
    PopUpMenu.title(SQLSubMenuName)
    PopUpMenu.minsize(width=300, height=200)
    PopUpMenu.maxsize(width=350, height=250)

    my_button = CTkButton(PopUpMenu, text="close", font=('Arial',20), width=200, height=50, command=PopUpMenu.destroy)
    my_button.place(x=135,y=145)



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

    # Iterative buttons dimensions
    button_width = 200
    button_height = 80
    y_padding = 25

    # Iterative buttons placement
    x_positions = [94, 388]  # column 1 and column 2
    y_start = 119
    y_step = button_height + y_padding

    buttons = []  # Store buttons in case you want to reference or destroy them later

    #Button
    btnPlaceOrder = CTkButton(Window, text="Place Order", font=('Arial',20), width=200, height=50, command=open_credit_ui)
    btnPlaceOrder.place(x=735,y=45)

    btnSubmit = CTkButton(Window, text="Remove Last", font=('Arial',20), width=200, height=50)
    btnSubmit.place(x=735,y=445)

    # Iterative MenuItems buttons
    for index, name in MenuItems.items():
        col = index % 2       # 0 or 1 (left/right column)
        row = index // 2      # increases every 2 items

        x = x_positions[col]
        y = y_start + (y_step * row)

        button = CTkButton(Window, font=('Arial', 20), text=name, width=button_width, height=button_height)
        
        button.place(x=x, y=y)
        buttons.append(button)



#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
CreateButtons()
CreateLabel()



#Create mainloop to run program
Window.mainloop()