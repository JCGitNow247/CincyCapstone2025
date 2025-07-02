from tkinter import *

#To istall, run the following on terminal: pip install customtkinter & pip install customtkinter --upgrade
from customtkinter import * 
from PIL import Image

set_appearance_mode('light')

Window = CTk()

#Create size of window 
Window.geometry("1024x600")

#Display Titlebar Message
Window.title("<CompanyName>"+" Powered by TruckBytes")

#Display Titlebar Icon
Window.iconbitmap("images/our.logos/TruckBytes.ico")

#Label of the page
lblTitle = CTkLabel(Window, text="Management Page", font=('Arial', 32))
lblTitle.place(x=235,y=45)




#Create Buttons
btnOrder = CTkButton(Window, font=('Arial', 24), text="Truckbytes Ordering", width=300, height=80)
btnOrder.place(x=222,y=119)

btnAnalytics = CTkButton(Window, font=('Arial', 24), text="Analytics", width=300, height=80)
btnAnalytics.place(x=222,y=268)

btnMenuBuilder = CTkButton(Window, font=('Arial', 24), text="Menu Builder", width=300, height=80)
btnMenuBuilder.place(x=222,y=415)




#Display "TruckBytes.png" file
original_logo = Image.open("images/our.logos/TruckBytes.png")
resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250,250))

imgLogo = CTkLabel(Window,image=truck_logo, text="")
imgLogo.place(x=744,y=320)

#Display "their.logo.png" file
their_logo = Image.open("images/our.logos/their.logo.png")
resized_logo = their_logo.resize((200,200),Image.Resampling.LANCZOS)
truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250,250))

imgLogo = CTkLabel(Window,image=truck_logo, text="")
imgLogo.place(x=744,y=33)




#Create mainloop to run program
Window.mainloop()