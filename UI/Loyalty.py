# Reset login state at startup (ONLY done here)
import json

#Import TruckBytes Standard UI options
from OurDisplay import *

#Import to validate email address 
import re

#User input validation
def validate_fields():

    phone = txtPhoneNumbField.get("1.0", "end").strip()
    email = txtEmailAddyField.get("1.0", "end").strip()

    if not (phone.isdigit() and len(phone) == 10):
        messagebox.showerror("Invalid Phone Number", "Phone number must be 10 digits.")
        return False


    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
       messagebox.showerror("Invalid Email", "Please enter a valid email address.")
       return False
    
    return True



def CreateLabels():
    #Label of the page
    CTkLabel(Window, text="Customer Loyalty", font=('Arial', 32, "bold")).place(x=235,y=45)
    
    #Create Label For "Phone Number"
    CTkLabel(Window, text="Phone Number", font=('Arial',24)).place(x=150,y=145)

    #Create Label For "Email Address"
    CTkLabel(Window, text="Email Address", font=('Arial',24)).place(x=150,y=190)



def CreateFields():
    global txtPhoneNumbField, txtEmailAddyField

    #Create Entry For "Phone Number"
    txtPhoneNumbField = CTkTextbox(Window, width=250,height=40, font=('Arial',24)).place(x=360,y=143)

    #Create  for "Email Address"
    txtEmailAddyField = CTkTextbox(Window, width=250,height=40, font=('Arial',24)).place(x=360,y=190)



def CreateButtons():

    #CTkButton(Window, font=('Arial', 24), text="Check Loyalty", width=300, height=80, command=open_ordering_w_v_ui).place(x=222,y=270)

    #This SKIPS Validation = Will Be Removed in Final. Use above code to validate
    #Create button to Check Loyalty
    CTkButton(Window, font=('Arial', 24), text="Check Loyalty", width=300, height=80).place(x=222,y=270)
    #Create button to Skip Loyalty
    CTkButton(Window, font=('Arial', 24), text="Skip Loyalty\n Order Food", width=300, height=80, command=open_ordering_ui).place(x=222,y=415)



#Used to open OrderingPage.py
def open_ordering_ui():
    #This subprocess allows you to specify a program to open a specific file
    subprocess.Popen(['python', 'UI/OrderingPage.py'])
    #This closes the current page
    Window.destroy()



#Used to open OrderingPage.py with validation
def open_ordering_w_v_ui():
    if validate_fields():
        #This subprocess allows you to specify a program to open a specific file
        subprocess.Popen(['python', 'OrderingPage.py'])
        #This closes the current page
        Window.destroy()



#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()

#Intantiate UI specific to this page
CreateFields()
CreateLabels()
CreateButtons()



#Create mainloop to run program
Window.mainloop()