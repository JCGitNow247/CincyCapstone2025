from tkinter import *
from customtkinter import * #pip install customtkinter & pip install customtkinter --upgrade
from PIL import Image

set_appearance_mode('light')

Window = CTk()
Window.title("Employee Login")
Window.iconbitmap("images/our.logos/TruckBytes.ico")
Window.geometry("640x360")

lblTitle = CTkLabel(Window,
                    text="Employee Login",
                    font=('Arial', 16))
lblTitle.place(x=430,y=50)

lblUsername = CTkLabel(Window,
                       text="Username:", 
                       font=('Arial',14))
lblUsername.place(x=120,y=170)

lblPassword = CTkLabel(Window, 
                       text="Password:", 
                       font=('Arial',14))
lblPassword.place(x=120,y=215)

txtUsernameField = CTkTextbox(Window, width=200,height=1)
txtUsernameField.place(x=140,y=170)

txtPasswordField = CTkTextbox(Window, width=200,height=1)
txtPasswordField.place(x=140,y=215)

btnSubmit = CTkButton(Window,
                      text="Login", 
                      width=200, 
                      height=40)
btnSubmit.place(x=500,y=270)

original_logo = Image.open("images/our.logos/TruckBytes.png")
resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(200,200))

imgLogo = CTkLabel(Window,image=truck_logo, text="")
imgLogo.place(x=500,y=340)

Window.mainloop()