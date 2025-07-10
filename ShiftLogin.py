from our_display import *

Create_Window()
Create_Menubar()





lblTitle = CTkLabel(Window,
                    text="Employee Login",
                    font=('Arial', 32))
lblTitle.place(x=400,y=50)

lblUsername = CTkLabel(Window,
                       text="Last Name:", 
                       font=('Arial',20))
lblUsername.place(x=240,y=170)

lblPassword = CTkLabel(Window, 
                       text="Password:", 
                       font=('Arial',20))
lblPassword.place(x=240,y=215)

txtUsernameField = CTkTextbox(Window, width=200,height=1)
txtUsernameField.place(x=412,y=170)

txtPasswordField = CTkTextbox(Window, width=200,height=1)
txtPasswordField.place(x=412,y=215)

btnSubmit = CTkButton(Window,
                      text="Login", 
                      width=200, 
                      height=40)
btnSubmit.place(x=412,y=270)

original_logo = Image.open("images/our.logos/TruckBytes.png")
resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(200,200))

imgLogo = CTkLabel(Window,image=truck_logo, text="")
imgLogo.place(x=412,y=340)

Window.mainloop()