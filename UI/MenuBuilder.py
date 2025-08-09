from OurDisplay import *
from customtkinter import CTkCheckBox
from tkinter import filedialog
from MenuItem import MenuItem
import DatabaseUtility as DB
import tkinter as tk
from tkinter import messagebox
import os


#SQL Variables
SQLItem1 = "SQL SubMenu1"
SQLItem2 = "SQL SubMenu2"
SQLItem3 = "SQL SubMenu3"

SQLSubMenu1 = "intSubMenuID1"
SQLSubMenu2 = "intSubMenuID2"
SQLSubMenu3 = "intSubMenuID3"


truck_logo = None
imgLogo = None



def setup_ui():

    global txtItemNameField, txtItemPriceField, txtItemDescriptionField

    txtItemNameField = CTkTextbox(Window,
                                  font=font1,
                                  width=250,
                                  height=40)
    txtItemNameField.place(x=200,y=125)

    txtItemPriceField = CTkTextbox(Window,
                                   font=font1,
                                    width=250,
                                    height=40)
    txtItemPriceField.place(x=200,y=300)

    txtItemDescriptionField = CTkTextbox(Window,
                                         font=font1,
                                         width=250,
                                         height=150)
    txtItemDescriptionField.place(x=648,y=130)


    #Label of the page
    CTkLabel(Window,
            font=titleFont,
            text="Menu Builder",
            ).place(x=235,y=45)

    #Create Label for "Item Name"
    CTkLabel(Window, font=font1,
             text="Item Name:"
             ).place(x=60,y=125)

    #Create Label for "Item Price"
    CTkLabel(Window,
            font=font1,
            text="Item Price:"
            ).place(x=60,y=300)

    CTkLabel(Window,
            font=font1,
            text="Add Description:"
            ).place(x=685,y=90) #x=670

    CTkLabel(Window,
            font=font1,
            text="Add Sub Menu To Item:"
            ).place(x=650,y=300)

    btnCreateNew = CTkButton(Window,
                             font=titleFont,
                             text="Create New Item",
                             width=300,
                             height=80, 
                             command=create_item)
    btnCreateNew.place(x=623,y=440)

    CTkButton(Window,
            font=font1,
            text="Return To\nMangement Page",
            width=80,
            height=80,
            command=open_Mgmt_ui
            ).place(x=218,y=445)


#CheckBox 
checkbox_var = tk.IntVar()

ChkBxIsTaxable = CTkCheckBox(Window,
                             font=font1,
                             text= "Is This Item Taxable?",
                             variable=checkbox_var,
                             checkbox_height=25,
                             checkbox_width=25)
ChkBxIsTaxable.place(x=200,y=360)



#### I may need to move this up so the drop down menu does not fall off screen.
def DisplayComboBoxes():

    global cboMenu, cboAddSubMenu

    Menus = DB.get_menus()

    menu_names = [item["name"] for item in Menus.values()]

    cboMenu = CTkComboBox(Window,
                        values=menu_names,
                        font=('Arial', 18),
                        justify="center", 
                        width=250, 
                        height=40)
    
    cboMenu.place(x=200,y=175) ##################################################################
    cboMenu.set('Add To Existing Menu')

    SubMenus = DB.get_sub_menus()

    sub_menu_names = ["None"]
    sub_menu_names += [item["name"] for item in SubMenus.values()]

    cboAddSubMenu = CTkComboBox(Window,
                            values=sub_menu_names, 
                            font=('Arial', 14),
                            justify="center",
                            width=250, 
                            height=40)

    cboAddSubMenu.place(x=648,y=340)  
    cboAddSubMenu.set('Prompt Existing Sub Menu')



def create_item():
    name = txtItemNameField.get("0.0", "end-1c").strip()
    description = txtItemDescriptionField.get("0.0", "end-1c").strip()
    price_text = txtItemPriceField.get("0.0", "end-1c").strip()
    menu_type = cboMenu.get()

    if check_field_error(name, message="Enter menu item name") == True: return
    if check_field_error(description, message="Enter menu item description") == True: return
    if check_field_error(price_text, message="Enter menu item price") == True: return
    if check_field_error(menu_type, message="Select a menu type") == True: return

    menu_item = MenuItem()
    menu_item.set_name(name)
    menu_item.set_image("NULL")
    typeID = DB.get_menu_id(cboMenu.get())
    menu_item.set_typeID(typeID)
    menu_item.set_description(txtItemDescriptionField.get("0.0", "end-1c"))

    try:
        price = float(txtItemPriceField.get("0.0", "end-1c"))
        if price < 0:
            raise ValueError
        menu_item.set_price(price)
    except ValueError:
        print("Invalid Price")
        return

    sub_menuID = DB.get_sub_menu_id(cboAddSubMenu.get())
    if sub_menuID == None:
        sub_menuID = "Null"
    menu_item.set_sub_menuID(sub_menuID)

    if ChkBxIsTaxable.get() == 1:
        taxable = "Y"
    else:
        taxable = "N"
    menu_item.set_taxable(taxable)

    DB.insert_menu_item(menu_item)

    clear_fields()



def check_field_error(control, message):

    error_flag = False

    if not control:
        messagebox.showerror("Missing Field", message)
        error_flag = True

    return error_flag



#Resets fields after creating a new item
def clear_fields():
    txtItemNameField.delete(0.0, 'end')
    txtItemPriceField.delete(0.0, 'end')
    txtItemDescriptionField.delete(0.0, 'end')
    ChkBxIsTaxable.deselect()
    cboAddSubMenu.set("Add To Existing Sub Menu?")
    cboMenu.set('Add To Existing Menu')



#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
DisplayComboBoxes()
setup_ui()



#Create mainloop to run program
Window.mainloop()