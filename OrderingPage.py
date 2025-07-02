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
lblTitle = CTkLabel(Window, text="Welcome To The Ordering Page", font=('Arial', 32))
lblTitle.place(x=105,y=40)

#Label to show Total
lblTotal = CTkLabel(Window, text="Total:", font=('Arial',20))
lblTotal.place(x=735,y=525)



#Do we need to create geometery based on number of items in the menu?


#Button
btnSubmit = CTkButton(Window, text="Submit", font=('Arial',20), width=200, height=50)
btnSubmit.place(x=735,y=45)




btnItem1 = CTkButton(Window, font=('Arial', 20), text="Item #1", width=200, height=80)
btnItem1.place(x=94,y=119)

btnItem2 = CTkButton(Window, font=('Arial', 20), text="Item #2", width=200, height=80)
btnItem2.place(x=94,y=268)

btnItem3 = CTkButton(Window, font=('Arial', 20), text="Item #3", width=200, height=80)
btnItem3.place(x=94,y=415)



btnItem4 = CTkButton(Window, font=('Arial', 20), text="Item #4", width=200, height=80)
btnItem4.place(x=388,y=119)

btnItem5 = CTkButton(Window, font=('Arial', 20), text="Item #5", width=200, height=80)
btnItem5.place(x=388,y=268)

btnItem6 = CTkButton(Window, font=('Arial', 20), text="Item #6", width=200, height=80)
btnItem6.place(x=388,y=415)



Window.mainloop()