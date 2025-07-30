# Reset login state at startup (ONLY done here)
import json

#Import TruckBytes Standard UI options
from OurDisplay import *

#Import to validate email address 
import re

from tkinter import messagebox


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
    

def setup_ui():
    global txtPhoneNumbField, txtEmailAddyField

    #Create Entry For "Phone Number"
    txtPhoneNumbField = CTkTextbox(Window,
                                   width=250,
                                   height=40,
                                   font=('Arial',24))
    txtPhoneNumbField.place(x=360,y=143)

    #Create  for "Email Address"
    txtEmailAddyField = CTkTextbox(Window,
                                   width=250,
                                   height=40,
                                   font=('Arial',24))
    txtEmailAddyField.place(x=360,y=190)

    #Label of the page
    CTkLabel(Window,
             text="Customer Loyalty",
             font=('Arial', 32, "bold")).place(x=235,y=45)
    
    #Create Label For "Phone Number"
    CTkLabel(Window,
             text="Phone Number",
             font=('Arial',24)).place(x=150,y=145)

    #Create Label For "Email Address"
    CTkLabel(Window,
             text="Email Address",
             font=('Arial',24)).place(x=150,y=190)


    #Create button to Check Loyalty
    CTkButton(Window, font=('Arial', 24),
              text="Check Loyalty\nJoin Loyalty",
              width=300,
              height=80,command=check_loyality).place(x=222,y=270)


    #Create button to Skip Loyalty
    CTkButton(Window, font=('Arial', 24),
              text="Skip Loyalty\n Order Food",
              width=300,
              height=80,
              command=open_ordering_ui).place(x=222,y=415)



def show_user_entrys():
    ######  I could not get the ".get()" to work, not sure why.
    phone = txtPhoneNumbField.get("1.0", "end").strip()
    email = txtEmailAddyField.get("1.0", "end").strip()
    
    message = f"Sorry that does not match our records.\nYou entered:\n {phone}\n{email} \nWould You like to create Loyality account with this information?" #\n {phone}\n {email}"
    #message = f"That does not match our records.\nYou entered:  \nWould You like to create Loyality account with this information?" #\n {phone}\n {email}"
    result = messagebox.askquestion("First Time Loyality Signup", message)

    if result == "yes":
       
        #########################
        # SQL Create New Customer
        #########################

       yesMsg = f"You have been added"
       messagebox.showinfo("Created New Account", yesMsg)#, command=open_ordering_ui)
       #open_menu_builder_ui()
    ###ISSUE### ###  Hitting "OK" NEEDS to lead to the ordering page, currently it closes everything ##############
    #Does this need to be a different type of messagebox?


#Used to open OrderingPage.py with validation
def check_loyality():
    if validate_fields():
        show_user_entrys()
        
        ##############################
        #### ADD CODE TO QUERY DB ####
        ##############################

        #This subprocess allows you to specify a program to open a specific file
        subprocess.Popen(['python', 'OrderingPage.py'])
    
        #This closes the current page
        Window.destroy()







#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()

#Intantiate UI specific to this page
setup_ui()



#Create mainloop to run program
Window.mainloop()