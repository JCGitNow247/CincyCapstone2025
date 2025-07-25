from OurDisplay import *
from customtkinter import CTkCheckBox
from tkinter import filedialog
import DatabaseUtility as DB
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

def display_food_image(img_path=None):
    """Load and display the company logo."""
    global truck_logo, imgLogo

    if img_path is None:
        img_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "FoodImage.png")

    if not os.path.exists(img_path):
        print(f"Warning: Could not find image at {img_path}")
        return

    original_logo = Image.open(img_path)
    resized_logo = original_logo.resize((250, 250), Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250, 250))

    if imgLogo is None:
        imgLogo = CTkLabel(Window, image=truck_logo, text="")
        imgLogo.place(x=683, y=115)
    else:
        imgLogo.configure(image=truck_logo)


def save_as_png():
      #This Prompts to save a filename, in the listed directory, as a specific file type - You must include an option for all files??
    file_path = filedialog.askopenfilename(
    title="Select Your Food Image",
    initialdir="images",
    filetypes=(
        ("Image Files", "*.png;*.jpg;*.jpeg"),
        ("PNG Files", "*.png"),
        ("JPEG Files", "*.jpg;*.jpeg"),
        ("All files", "*.*")
    )
    )


    if file_path:
        display_food_image(file_path)



def DisplayLabels():

    #Label of the page
    lblTitle = CTkLabel(Window, text="Menu Builder", font=('Arial', 32, 'bold'))
    lblTitle.place(x=235,y=20)

    #Create Label & Textbox for "Item Name"
    lblItemName = CTkLabel(Window, text="Item Name:", font=('Arial',24))
    lblItemName.place(x=60,y=90)

    #Create Label & Textbox for "Item Price"
    lblItemPrice = CTkLabel(Window, text="Item Price:", font=('Arial',24))
    lblItemPrice.place(x=60,y=220)

    lblAddDescription = CTkLabel(Window, font=('Arial', 24), text="Add Description")
    lblAddDescription.place(x=18,y=340)

    lblReqSubMenu = CTkLabel(Window, text="Requires\nSub Menu", font=('Arial',24))
    lblReqSubMenu.place(x=60,y=500)



def DisplayFields():

    global txtItemNameField, txtItemPriceField, txtItemDescriptionField

    txtItemNameField = CTkTextbox(Window, width=250, height=40, font=('Arial',24))
    txtItemNameField.place(x=200,y=90)

    txtItemPriceField = CTkTextbox(Window, width=250, height=40, font=('Arial',24))
    txtItemPriceField.place(x=200,y=220)

    txtItemDescriptionField = CTkTextbox(Window, width=250, height=150, font=('Arial',24))
    txtItemDescriptionField.place(x=200,y=345)



def DisplayButtons():
    btnAddImage = CTkButton(Window, font=('Arial', 24), text="Click To Add Image", width=200, height=50, command=save_as_png)
    btnAddImage.place(x=690,y=30)

    btnCreateNew = CTkButton(Window, font=('Arial', 24), text="Create New Item", width=200, height=50, command=clear_fields)
    btnCreateNew.place(x=690,y=525)



#CheckBox 
ChkBxIsTaxable = CTkCheckBox(Window, text= "Is This Item Taxable?",font= ('Arial', 24),    checkbox_height=25, checkbox_width=25)
ChkBxIsTaxable.place(x=200,y=270)



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
    
    cboMenu.place(x=200,y=140)
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

    cboAddSubMenu.place(x=200,y=510)  
    cboAddSubMenu.set('Prompt Existing Sub Menu?')


    #Display "Food.Image.png" file
    img_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "FoodImage.png")
    if os.path.exists(img_path):
        original_logo = Image.open(img_path)
        resized_logo = original_logo.resize((250, 250), Image.Resampling.LANCZOS)
        truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250, 250))
        imgLogo = CTkLabel(Window, image=truck_logo, text="")
        imgLogo.place(x=683, y=115)
    else:
        print(f"Warning: Could not find image at {img_path}")

    imgLogo = CTkLabel(Window,image=truck_logo, text="")
    imgLogo.place(x=683,y=115)


#Resets fields after creating a new item
def clear_fields():
    txtItemNameField.delete(0.0, 'end')
    txtItemPriceField.delete(0.0, 'end')
    txtItemDescriptionField.delete(0.0, 'end')

    ChkBxIsTaxable.deselect()
    cboAddSubMenu.set("Prompt Existing Sub Menu?")
    cboMenu.set('Add To Existing Menu')

    # Reset displayed image
    display_food_image()  
  



#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
DisplayComboBoxes()
DisplayLabels()
DisplayFields()
DisplayButtons()



#Create mainloop to run program
Window.mainloop()