from our_display import *


Create_Window()
Create_Menubar()
Display_Logos23()


def CreateLabels():
    #Label of the page
    lblTitle = CTkLabel(Window, text="Customer Loyalty", font=('Arial', 32))
    lblTitle.place(x=235,y=45)
    
    #Create Label & Textbox For "Phone Number"
    lblPhoneNumb = CTkLabel(Window, text="Phone Number", font=('Arial',24))
    lblPhoneNumb.place(x=150,y=150)

    #Create Label For "Email Address"
    lblEmailAddy = CTkLabel(Window, text="Email Address", font=('Arial',24))
    lblEmailAddy.place(x=150,y=195)


def CreateFields():
    #Create Textbox For "Phone Number"
    txtPhoneNumbField = CTkTextbox(Window, width=250,height=40)
    txtPhoneNumbField.place(x=360,y=148)
    #Create Textbox for "Email Address"
    txtEmailAddyField = CTkTextbox(Window, width=250,height=40)
    txtEmailAddyField.place(x=360,y=195)




def CreateButtons():
    btnCheckLoyal = CTkButton(Window, font=('Arial', 24), text="Check Loyalty", width=300, height=80)
    btnCheckLoyal.place(x=222,y=270)

    btnMenuBuilder = CTkButton(Window, font=('Arial', 24), text="Skip Loyalty\n Order Food", width=300, height=80)
    btnMenuBuilder.place(x=222,y=415)


CreateLabels()
CreateFields()
CreateButtons()



#Create mainloop to run program
Window.mainloop()
