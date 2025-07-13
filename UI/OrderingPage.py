#Import TruckBytes Standard UI options
from OurDisplay import *



#Variables to link to SQL

SQLTotal = "Your Total"
Item1 = "SQL Item1"
Item2 = "SQL Item2"
Item3 = "SQL Item3"
Item4 = "SQL Item4"
Item5 = "SQL Item5"
Item6 = "SQL Item6"
SQLSubMenuName= "SQL Sub Menu Name"













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
    #Button
    btnPlaceOrder = CTkButton(Window, text="Place Order", font=('Arial',20), width=200, height=50, command=open_credit_ui)
    btnPlaceOrder.place(x=735,y=45)

    btnSubmit = CTkButton(Window, text="Remove Last", font=('Arial',20), width=200, height=50)
    btnSubmit.place(x=735,y=445)

    btnItem1 = CTkButton(Window, font=('Arial', 20), text=Item1, width=200, height=80)
    btnItem1.place(x=94,y=119)

    btnItem2 = CTkButton(Window, font=('Arial', 20), text=Item2, width=200, height=80)
    btnItem2.place(x=94,y=268)

    btnItem3 = CTkButton(Window, font=('Arial', 20), text=Item3, width=200, height=80)
    btnItem3.place(x=94,y=415)

    btnItem4 = CTkButton(Window, font=('Arial', 20), text=Item4, width=200, height=80)
    btnItem4.place(x=388,y=119)

    btnItem5 = CTkButton(Window, font=('Arial', 20), text=Item5, width=200, height=80)
    btnItem5.place(x=388,y=268)

    btnItem6 = CTkButton(Window, font=('Arial', 20), text=Item6, width=200, height=80, command= open_sub_menu)
    btnItem6.place(x=388,y=415)



#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
CreateButtons()
CreateLabel()



#Create mainloop to run program
Window.mainloop()