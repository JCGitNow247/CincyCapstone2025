#Import TruckBytes Standard UI options
from OurDisplay import *
import re


#Variable placeholders to link to db
tipOpt1= 15
tipOpt2= "18%"
tipOpt3= "20%"


# Get cost passed from OrderingPage.py or fallback to 0.00
try:
    cost = float(sys.argv[1])
except (IndexError, ValueError):
    cost = 0.00


total_with_tip = cost
lblTotal = None 



def apply_tip(percentage):
    """Apply a tip percentage to the base cost and update label."""
    global total_with_tip


    tip_amount = cost * percentage
    total_with_tip = cost + tip_amount
    lblTotal.configure(text=f"{total_with_tip:.2f}")



def CreateFields():
    #Must be global to validate
    global CustomerNameField, CardNumberField, ZipCodeField, SecurityCodeField, Expiration_DateField

    
    #Accept Entry for "Customer Name"
    CustomerNameField = CTkTextbox(Window,
                               width=250,
                               height=40,
                               font=('Arial',24))
    CustomerNameField.place(x=61,y=90)
    CustomerNameField.focus_set()
    
    #Accept Entry for "Card Number"
    CardNumberField = CTkTextbox(Window,
                                  width=250,
                                  height=40,
                                  font=('Arial',24))
    CardNumberField.place(x=372,y=90)

    #Accept Entry For "Expiration Date"
    Expiration_DateField = CTkTextbox(Window,
                                       width=100,
                                       height=40,
                                       font=('Arial',24))
    Expiration_DateField.place(x=61,y=200)

    #Accept Entry For "Security Code"
    SecurityCodeField = CTkTextbox(Window,
                                    width=100,
                                    height=40,
                                    font=('Arial',24))
    SecurityCodeField.place(x=211,y=200)

    #Accept Entry For "Zip Code"
    ZipCodeField = CTkTextbox(Window,
                               width=100,
                               height=40,
                               font=('Arial',24))
    ZipCodeField.place(x=372,y=200)
  

def setup_ui():
    global bthTipOption1, bthTipOption2, bthTipOption3
    font1 = ('Arial',24)
    font2 = ('Arial',14)








    #Create Labels
    CTkLabel(Window,
             font=font1,
             text="Name On Card"
             ).place(x=61,y=50)
    
    CTkLabel(Window, 
             font=font1,
             text="Card Number"
             ).place(x=372,y=50)
    
    CTkLabel(Window,
             font=font2,
             text="Expiration Date",
             ).place(x=61,y=155)
    
    CTkLabel(Window,
             font=font2,
             text="Security Code"
             ).place(x=211,y=155)
    
    CTkLabel(Window,
             font=font1,
             text="Zip Code"
             ).place(x=372,y=155)
    
    CTkLabel(Window,
             font=font1,
             text="Total: $"   
             ).place(x=72,y=455)
    
    
    #Number from Ordering Page
    CTkLabel(Window,
             font=font1,
             text=f"{cost:.2f}"
             ).place(x=150,y=455)

    CTkLabel(Window,
            font=font1,
            text=f"{total_with_tip:.2f}"
            ).place(x=150, y=455)


    #Buttons
    bthTipOption1 = CTkButton(Window,
                              font=font1,
                              text=tipOpt1,
                              width=120,
                              height=80
                              ).place(x=81,y=320)
    
    bthTipOption2 = CTkButton(Window,
                              font=font1,
                              text=tipOpt2,
                              width=120,
                              height=80
                              ).place(x=282,y=320)
    
    bthTipOption3 = CTkButton(Window,
                              font=font1,
                              text=tipOpt3,
                              width=120,
                              height=80
                              ).place(x=482,y=320)


    CTkButton(Window,
              font=font1,
              text="Pay",
              width=200,
              height=80,
              command=validate_fields
              ).place(x=292,y=450) #open_loyalty_ui).place(x=292,y=450)




# User Input Validation
def validate_fields():
    card_number = CardNumberField.get("1.0", "end").strip()
    zip_code = ZipCodeField.get("1.0", "end").strip()
    security_code = SecurityCodeField.get("1.0", "end").strip()
    expiration_date = Expiration_DateField.get("1.0", "end").strip()
    name_on_card = CustomerNameField.get("1.0", "end").strip()

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



#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()

#Intantiate UI specific to this page
CreateFields()
setup_ui()



#Create mainloop to run program
Window.mainloop()