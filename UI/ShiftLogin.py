#Import TruckBytes Standard UI options
from OurDisplay import *
import re


"""
Cole: testing some SQL connection code here
"""
# region SQL Connection test
import mariadb

conn = mariadb.connect(

    host="localhost",
    user="truckbytesdev",
    password="tb001",
    database="dbTruckBytes"
)

cursor = conn.cursor()
cursor.execute("SELECT fnEmployeeLogin('Whitaker','test1')")
EmployeeID = cursor.fetchone()[0]
print("Employee ID: ", EmployeeID)
# endregion




lblTitle = CTkLabel(Window, text="Employee Login", font=('Arial', 32))
lblTitle.place(x=400,y=50)

lblUsername = CTkLabel(Window, text="Last Name:", font=('Arial',20))
lblUsername.place(x=240,y=170)

lblPassword = CTkLabel(Window, text="Password:", font=('Arial',20))
lblPassword.place(x=240,y=215)




txtUsernameField = CTkTextbox(Window, width=200,height=1)
txtUsernameField.place(x=412,y=170)

#This show= arguement is how you obfuscate the field using a *
txtPasswordField = CTkEntry(Window, width=200,height=1,show="*")
txtPasswordField.place(x=412,y=215)


def MsgBoxInvalid():
    # This function displays messagebox Titlebar & then message
    messagebox.showinfo("Invalid Password", "Invalid Password\nPlease Try Again")
   
    pop_button= Button(Window,text="", command=MsgBoxInvalid)
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
#btnSubmit = CTkButton(Window, text="Login", width=200, height=40)
btnSubmit = CTkButton(Window, text="Login", width=200, height=40, command=open_ordering_ui)
btnSubmit.place(x=412,y=270)



#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logo_Center()

##################################

Window.mainloop()