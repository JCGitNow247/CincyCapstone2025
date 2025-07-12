#Import TruckBytes Standard UI options
from OurDisplay import *
import re













lblTitle = CTkLabel(Window, text="Employee Login", font=('Arial', 32))
lblTitle.place(x=400,y=50)

lblUsername = CTkLabel(Window, text="Last Name:", font=('Arial',20))
lblUsername.place(x=240,y=170)

lblPassword = CTkLabel(Window, text="Password:", font=('Arial',20))
lblPassword.place(x=240,y=215)




txtUsernameField = CTkTextbox(Window, width=200,height=1)
txtUsernameField.place(x=412,y=170)

txtPasswordField = CTkTextbox(Window, width=200,height=1)
txtPasswordField.place(x=412,y=215)


#Validate user inputs
def validate_fields():
    employee_name = txtUsernameField.get("1.0", "end").strip()
    password = txtPasswordField.get("1.0", "end").strip()
 

    name_regex = r"^[A-Za-z\s\-']{2,50}$"
    if not re.match(name_regex, employee_name):
        messagebox.showerror("Invalid Name", "Please enter a valid name")
        return False
    
    if not (password.isdigit() and len(password) > 2):
        messagebox.showerror("Invalid Password", "Password must be at least 2 digits.")
        return False

    return True



def open_ordering_ui():
    if validate_fields():
        #import subprocess
        subprocess.Popen(['python', 'OrderingPage.py'])
        Window.destroy()



btnSubmit = CTkButton(Window, text="Login", width=200, height=40, command=open_ordering_ui)
btnSubmit.place(x=412,y=270)



#Display Logo
original_logo = Image.open("images/our.logos/TruckBytes.png")
resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(200,200))

imgLogo = CTkLabel(Window,image=truck_logo, text="")
imgLogo.place(x=412,y=340)













#Intantiate UI options
Create_Window()
Create_Menubar()



Window.mainloop()