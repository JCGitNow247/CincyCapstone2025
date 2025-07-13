#Import TruckBytes Standard UI options
from OurDisplay import *
import re


#Variable placeholders to link to db
tipOpt1= "15%"
tipOpt2= "18%"
tipOpt3= "20%"



def CreateLabels():
    #Create Label for "Customer Name"
    lblCustomerName = CTkLabel(Window, text="Name On Card", font=('Arial',24),)
    lblCustomerName.place(x=61,y=50)

    #Create Label "Card Number"
    lblCardNumber = CTkLabel(Window, text="Card Number", font=('Arial',24))
    lblCardNumber.place(x=372,y=50)

    #Create Label For "Expiration Date"
    lblExperation_Date = CTkLabel(Window, text="Expiration Date", font=('Arial',14))
    lblExperation_Date.place(x=61,y=180)

    #Create Label For "Zip Code"
    lblZipCode = CTkLabel(Window, text="Zip Code", font=('Arial',24))
    lblZipCode.place(x=372,y=180)

    #Create Label For "Security Code"
    lblSecurityCode = CTkLabel(Window, text="Security Code", font=('Arial',14))
    lblSecurityCode.place(x=211,y=180)



def CreateFields():
    global txtCustomerName, txtCardNumberField, txtZipCodeField, txtSecurityCodeField, txtExpiration_DateField

    #Create Textbox for "Customer Name"
    txtCustomerName = CTkTextbox(Window, width=250,height=40, font=('Arial',24))
    txtCustomerName.place(x=61,y=90)
    txtCustomerName.focus_set()
    
    #Create Textbox for "Card Number"
    txtCardNumberField = CTkTextbox(Window, width=250,height=40, font=('Arial',24))
    txtCardNumberField.place(x=372,y=90)

    #Create Textbox For "Expiration Date"
    txtExpiration_DateField = CTkTextbox(Window, width=100,height=40, font=('Arial',24))
    txtExpiration_DateField.place(x=61,y=240)

    #Create Textbox For "Zip Code"
    txtZipCodeField = CTkTextbox(Window, width=100,height=40, font=('Arial',24))
    txtZipCodeField.place(x=372,y=240)
    #txtZipCodeField.insert("0.0","00000")

    #Create Textbox For "Security Code"
    txtSecurityCodeField = CTkTextbox(Window, width=100,height=40, font=('Arial',24))
    txtSecurityCodeField.place(x=211,y=240)



# User Input Validation
def validate_fields():
    card_number = txtCardNumberField.get("1.0", "end").strip()
    zip_code = txtZipCodeField.get("1.0", "end").strip()
    security_code = txtSecurityCodeField.get("1.0", "end").strip()
    expiration_date = txtExpiration_DateField.get("1.0", "end").strip()
    name_on_card = txtCustomerName.get("1.0", "end").strip()

    name_regex = r"^[A-Za-z\s\-']{2,50}$"
    if not re.match(name_regex, name_on_card):
        messagebox.showerror("Invalid Name", "Please enter a valid name (letters, spaces, hyphens, apostrophes only).")
        return False
    
    if not (card_number.isdigit() and len(card_number) == 16):
        messagebox.showerror("Invalid Card", "Card number must be 16 digits.")
        return False

    if not (expiration_date.isdigit() and len(expiration_date) == 4):
        messagebox.showerror("Invalid Code", "Expiration Date must be 555 digits.")
        return False

    if not (security_code.isdigit() and len(security_code) == 3):
        messagebox.showerror("Invalid Code", "Security Code must be 3 digits.")
        return False

    if not (zip_code.isdigit() and len(zip_code) == 5):
        messagebox.showerror("Invalid Zip", "Zip Code must be 5 digits.")
        return False
    
    return True



def CreateButtons():

    bthTipOption1 = CTkButton(Window, font=('Arial', 24), text=tipOpt1, width=80, height=80)
    bthTipOption1.place(x=111,y=360)

    bthTipOption2 = CTkButton(Window, font=('Arial', 24), text=tipOpt2, width=80, height=80)
    bthTipOption2.place(x=301,y=360)

    bthTipOption3 = CTkButton(Window, font=('Arial', 24), text=tipOpt3, width=80, height=80)
    bthTipOption3.place(x=493,y=360)

    
     #WILL BE REMOVED IN FINAL || SKIPS Validation
    bthTPayNow = CTkButton(Window, font=('Arial', 24), text="Pay", width=200, height=80)
    #This command= is imported from OrderingPage.py
    #bthTPayNow = CTkButton(Window, font=('Arial', 24), text="Pay", width=200, height=80, command=open_loyality_ui)
    bthTPayNow.place(x=241,y=490)



#Use to open Loyalty.py
def open_loyality_ui():
   if validate_fields():
        #import subprocess
        subprocess.Popen(['python', 'loyalty.py'])
        Window.destroy()



#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos23()

#Intantiate UI specific to this page
CreateFields()
CreateLabels()
CreateButtons()



#Create mainloop to run program
Window.mainloop()