from our_display import *
from customtkinter import CTkCheckBox




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
    txtItemNameField = CTkTextbox(Window, width=250,height=40)
    txtItemNameField.place(x=200,y=90)


    txtItemPriceField = CTkTextbox(Window, width=250,height=40)
    txtItemPriceField.place(x=200,y=220)

    txtItemDescriptionField = CTkTextbox(Window, width=250,height=150)
    txtItemDescriptionField.place(x=200,y=345)
    #txtItemDescriptionField.insert(0,"Enter Description Here")





def DisplayButtons():

    btnAddImage = CTkButton(Window, font=('Arial', 24), text="Click To Add Image", width=200, height=50)
    btnAddImage.place(x=690,y=30)

    btnCreateNew = CTkButton(Window, font=('Arial', 24), text="Create New Item", width=200, height=50)
    btnCreateNew.place(x=690,y=525)






SQLItem1 = "SQL item1"
SQLItem2 = "SQL item2"
SQLItem3 = "SQL item3"

SQLSubMenu1 = "SQL Sub Menu1"
SQLSubMenu2 = "SQL Sub Menu2"
SQLSubMenu3 = "SQL Sub Menu3"



#### I may need to move this up so the drop down menu does not fall off screen.
def DisplayComboBoxes():

    cboMenu = CTkComboBox(Window, values=[
        SQLItem1,
        SQLItem2,
        SQLItem3],
        font=('Arial', 24),
     
        justify="center", 
        width=250, 
        height=40)
    
    cboMenu.place(x=200,y=140)
    cboMenu.set('Add To Menu')


    cboAddSubMenu = CTkComboBox(Window,
        values=[
        SQLSubMenu1,
        SQLSubMenu2,
        SQLSubMenu3], 
        font=('Arial', 24),
        justify="center",
        width=250, 
        height=40)

    cboAddSubMenu.place(x=200,y=510)  
    cboAddSubMenu.set('Link Sub Menu')






    #Display "Food.Image.png" file
    original_logo = Image.open("images/our.logos/FoodImage.png")
    resized_logo = original_logo.resize((250,250),Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250,250))

    imgLogo = CTkLabel(Window,image=truck_logo, text="")
    imgLogo.place(x=683,y=115)































ChkBxIsTaxable = CTkCheckBox(Window, text= "Is This Item Taxable?",font= ('Arial', 24),    checkbox_height=25, checkbox_width=25)
ChkBxIsTaxable.place(x=200,y=270)





Create_Window()
Create_Menubar()

DisplayComboBoxes()
DisplayLabels()
DisplayFields()
DisplayButtons()


#Create mainloop to run program
Window.mainloop()
