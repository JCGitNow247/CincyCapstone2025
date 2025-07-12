from tkinter import *

#For some reason messagebox is not included in the import *??
from tkinter import messagebox

#To istall, run the following on terminal:
# pip install Pillow
#Import To Display Images
from PIL import Image

#To istall, run the following on terminal:
# pip install customtkinter & pip install customtkinter --upgrade
from customtkinter import * 

#Used to open new .py files
import subprocess


#Instantiate a window
Window = CTk()

#Variable to link back to SQL
SQLCompanyName = "<SQLCompanyName>"



def open_ordering_ui():
    #This subprocess allows you to specify a program to open a specific file
    subprocess.Popen(['python', 'OrderingPage.py'])
    #This closes the current page
    Window.destroy()

def open_about_ui():
    subprocess.Popen(['python', 'about.py'])
    #Window.destroy()

def open_login_ui():
    subprocess.Popen(['python', 'ShiftLogin.py'])
    Window.destroy()

def open_credit_ui():
    subprocess.Popen(['python', 'CreditCard.py'])
    Window.destroy()

def open_loyalty_ui():
    #This subprocess allows you to specify a program to open a specific file
    subprocess.Popen(['python', 'Loyalty.py'])
    #This closes the current page
    Window.destroy()


#Intantiate UI
def Create_Window():
    #Create size of window
    Window.geometry("1024x600")

    #Display Titlebar Message
    Window.title(SQLCompanyName+" Powered by TruckBytes")

    #Display Titlebar Icon
    Window.iconbitmap("images/our.logos/TruckBytes.ico")

    #Prevents the resizing of hte window
    Window.resizable(False, False)

    #Forces light mode
    set_appearance_mode('light')



#Intantiate Menubar
def Create_Menubar():
    """
    Instead of a dedicated management page. 
    Maybe we should just give extra dropdown options
    to people with management codes
    """

    #Define a Menubar
    #Need to change menubars color, Neither of these worked
    menuBar = Menu(Window)# , background='blue')
    Window.config(menu=menuBar) #,bg_color="#c80d0d")
    #menuBar.configure(bg_color="#c80d0d")


    file_menu = Menu(menuBar)
  

    #File Menu options
    menuBar.add_cascade(label="File", font=14, menu=file_menu)

    #Define File Menu's submenus
    file_menu.add_command(label="About", font=14, command=open_about_ui)
    file_menu.add_command(label="Close Program", font=14, command=Window.quit)


    #Adds a separator bar
    #file_menu.add_separator()

    #Employee Menu Options
    Employee_Menu = Menu(menuBar)
    menuBar.add_cascade(label="Employee", menu=Employee_Menu)


    #Define Log Out Menu's submenus
    Employee_Menu.add_command(label="Log In", font=14,command=open_login_ui)
    
    #Define Log Out Menu's submenus
    Employee_Menu.add_command(label="Logout", font=14,command=open_loyalty_ui)



def Display_Logos23():

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


def Display_Logo_Center():
    
    #Display Logo
    original_logo = Image.open("images/our.logos/TruckBytes.png")
    resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(200,200))

    imgLogo = CTkLabel(Window,image=truck_logo, text="")
    imgLogo.place(x=412,y=340)