from OurDisplay import *
from customtkinter import *
from tkinter import filedialog
import os

#SQL Variables
SQLItem1 = "SQL SubMenu1"
SQLItem2 = "SQL SubMenu2"
SQLItem3 = "SQL SubMenu3"

SQLSubMenu1 = "SQL Sub Menu1"
SQLSubMenu2 = "SQL Sub Menu2"
SQLSubMenu3 = "SQL Sub Menu3"





#May need to check this on linux.  This may only work on Windows
def save_as_png():
        #This Prompts to save a filename, in the listed directory, as a specific file type - You must include an option for all files??
        #result_file = filedialog.asksaveasfile(initialdir="images", filetypes=(("PNG Files", ".png"), ("all files", "*.*")))
        
        result_file = filedialog.asksaveasfilename(title="Save Your Company Logo", initialfile="Company_Logo.png", initialdir="images", filetypes=(("PNG Files", ".png"), ("all files", "*.*")))
        
        #result_label = Label(Window,text=result_file)
        result_label = CTkLabel(Window,text=result_file)

        #result_label.pack(pady=30)
        #result_label.place(x=200, y=200)
        result_label.pack()















def DisplayLabels():

  

    #Label of the page
    lblTitle = CTkLabel(Window, text="Business Builder", font=('Arial', 32, 'bold'))
    lblTitle.place(x=235,y=20)

    #Create Label & Textbox for "Company Name"
    CompanyName = CTkLabel(Window, text="Company\nName:", font=('Arial',24))
    CompanyName.place(x=60,y=90)

    #Create Label & Textbox for "Item Price"
    lblItemPrice = CTkLabel(Window, text="Item Price:", font=('Arial',24))
    lblItemPrice.place(x=60,y=220)

    lblLocation = CTkLabel(Window, font=('Arial', 24), text="Current\nLocation")
    lblLocation.place(x=18,y=340)

  


def DisplayFields():

    global txtCompanyNameField, txtItemPriceField, txtLocationField

    txtCompanyNameField = CTkTextbox(Window, width=250,height=40)
    txtCompanyNameField.place(x=200,y=90)

    txtItemPriceField = CTkTextbox(Window, width=250,height=40)
    txtItemPriceField.place(x=200,y=220)

    txtLocationField = CTkTextbox(Window, width=250,height=150)
    txtLocationField.place(x=200,y=345)










def DisplayButtons():
    btnAddImage = CTkButton(Window, font=('Arial', 24), text="Click To Add Image", width=200, height=50, command=save_as_png)
    btnAddImage.place(x=690,y=30)

    btnCreateNew = CTkButton(Window, font=('Arial', 24), text="Create New Item", width=200, height=50, command=clear_fields)
    btnCreateNew.place(x=690,y=525)






#### I may need to move this up so the drop down menu does not fall off screen.
def DisplayComboBoxes():

  
 

    #Display "Food.Image.png" file
    img_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "their.logo.png")
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



def clear_fields():
 
    txtItemPriceField.delete(0.0, 'end')
   
    ChkBxIsTaxable.deselect()

    pass




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
