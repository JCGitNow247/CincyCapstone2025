#Import TruckBytes Standard UI options
from OurDisplay import *
import re

import DatabaseUtility as DB

def setup_ui():
    global txtUsernameField, txtPasswordField

    txtUsernameField = CTkTextbox(Window, width=200, height=1)
    txtUsernameField.place(x=412, y=170)

    txtPasswordField = CTkEntry(Window, width=200, height=1, show="*")
    txtPasswordField.place(x=412, y=215)

    CTkLabel(Window, text="Employee Login", font=('Arial', 32)).place(x=400, y=50)
    CTkLabel(Window, text="Last Name:", font=('Arial', 20)).place(x=240, y=170)
    CTkLabel(Window, text="Password:", font=('Arial', 20)).place(x=240, y=215)
    
    CTkButton(Window, text="Login", width=200, height=40, command=open_ordering_ui).place(x=412, y=270)



def show_invalid_msg():
    # This function displays messagebox Titlebar & then message
    messagebox.showinfo("Invalid Password", "Invalid Password\nPlease Try Again")
   
    pop_button= Button(Window,text="", command=show_invalid_msg)
    pop_button.pack(padx=30, pady=45)
    
    

#Validate user inputs
def validate_fields():
    employee_name = txtUsernameField.get("1.0", "end").strip()
    password = txtPasswordField.get().strip()
 

    name_regex = r"^[A-Za-z\s\-']{2,50}$"
    if not re.match(name_regex, employee_name):
        messagebox.showerror("Invalid Name", "Please enter a valid name")
        return False
    
    if not (password.isdigit() and len(password) > 2):
        messagebox.showerror("Invalid Password", "Password must be at least 2 digits.")

        #Because the password was rejected, the password is removed
        txtPasswordField.delete(0, 'end')
        return False
  
    return True



def open_ordering_ui():
    if validate_fields():
        #import subprocess
        subprocess.Popen(['python', 'OrderingPage.py'])
        Window.destroy()


#WILL BE REMOVED IN FINAL || SKIPS Validation
#btnSubmit = CTkButton(Window, text="Login", width=200, height=40).place(x=412,y=270)
btnSubmit = CTkButton(Window, text="Login", width=200, height=40, command=open_ordering_ui).place(x=412,y=270)



#Intantiate UI specific to this page
setup_ui()

#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logo_Center()



Window.mainloop()