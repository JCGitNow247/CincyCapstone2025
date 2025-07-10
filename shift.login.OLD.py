from tkinter import *
from customtkinter import *
from PIL import Image

set_appearance_mode('light')

Window = CTk()
Window.title("Employee Login")
Window.geometry("1200x600")

lblTitle = CTkLabel(Window,
                    text="Employee Login",
                    font=('Arial', 48))
lblTitle.place(x=430,y=50)

lblUsername = CTkLabel(Window,
                       text="Username:", 
                       font=('Arial',24))
lblUsername.place(x=400,y=170)

lblPassword = CTkLabel(Window, 
                       text="Password:", 
                       font=('Arial',24))
lblPassword.place(x=400,y=215)

txtUsernameField = CTkTextbox(Window, width=200,height=1)
txtUsernameField.place(x=600,y=170)

txtPasswordField = CTkTextbox(Window, width=200,height=1)
txtPasswordField.place(x=600,y=215)

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