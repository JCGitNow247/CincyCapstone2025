from tkinter import *
from tkinter import messagebox

#To istall, run the following on terminal: pip install customtkinter & pip install customtkinter --upgrade
from customtkinter import * 
from PIL import Image

set_appearance_mode('light')

Window = CTk()

#Create size of window 
Window.geometry("1024x600")

company_name = "<CompanyName>"

#Display Titlebar Message
Window.title(company_name+" Powered by TruckBytes")

#Display Titlebar Icon
Window.iconbitmap("images/our.logos/TruckBytes.ico")


def Log_Out():
    #Add commands to log out
    #Maybe we should just give extra dropdown options to people with management codes
    #Instead of a dedicated management page.
    
    pass



def popup_about():
    messagebox.showinfo("Truckbytes", "Thank You For Choosing TruckBytes")
 



def About_Truckbytes():
    #Display popup info about 
    #What version, etc.
    pop_button = Button(Window, command=popup_about, text="Project by Cole, Adam & Jason", font=100)
    pop_button.pack(pady=220)

    #how do I close pop_button? This does not work
    #pop_button.quit
    pass


#Define a Menubar
menuBar = Menu(Window)
Window.config(menu=menuBar)

#Define 1st option on menuBar
file_menu = Menu(menuBar)
menuBar.add_cascade(label="File", font=14, menu=file_menu)
file_menu.add_command(label="About", font=14, command=About_Truckbytes)
#Adds a separator bar
file_menu.add_separator()
#This command closes the program.
file_menu.add_command(label="Close Program", font=14, command=Window.quit)

#Define 2nd option on menuBar
Log_Out_Menu = Menu(menuBar)
menuBar.add_cascade(label="Logout", menu=Log_Out_Menu)

#Fill in command later
Log_Out_Menu.add_command(label="Logout", font=14,command=Log_Out)





#Label of the page
lblTitle = CTkLabel(Window, text="Welcome To The Ordering Page", font=('Arial', 32))
lblTitle.place(x=105,y=40)

#Label to show Total
lblTotal = CTkLabel(Window, text="Total:", font=('Arial',20))
lblTotal.place(x=735,y=525)

Item1 = "SQL Item1"
Item2 = "SQL Item2"
Item3 = "SQL Item3"
Item4 = "SQL Item4"
Item5 = "SQL Item5"
Item6 = "SQL Item6"




#Do we need to create geometery based on number of items in the menu?

def open_sub_menu():
    new = Toplevel()


#Button
btnSubmit = CTkButton(Window, text="Submit", font=('Arial',20), width=200, height=50)
btnSubmit.place(x=735,y=45)

btnItem1 = CTkButton(Window, font=('Arial', 20), text=Item1, width=200, height=80)
btnItem1.place(x=94,y=119)

btnItem2 = CTkButton(Window, font=('Arial', 20), text=Item2, width=200, height=80)
btnItem2.place(x=94,y=268)

btnItem3 = CTkButton(Window, font=('Arial', 20), text=Item3, width=200, height=80)
btnItem3.place(x=94,y=415)

btnItem4 = CTkButton(Window, font=('Arial', 20), text=Item4, width=200, height=80)
btnItem4.place(x=388,y=119)

btnItem5 = CTkButton(Window, font=('Arial', 20), text=Item5, width=200, height=80)
btnItem5.place(x=388,y=268)

btnItem6 = CTkButton(Window, font=('Arial', 20), text=Item6, width=200, height=80, command= open_sub_menu)
btnItem6.place(x=388,y=415)






Window.mainloop()