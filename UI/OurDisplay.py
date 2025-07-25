from tkinter import *
import os
import tkinter.font as tkfont

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
import json ############################################
config_file = "config.json"
if os.path.exists(config_file):
    with open(config_file, "r") as f:
        CompanyPlaceholder = json.load(f).get("CompanyPlaceholder", "<SQLCompanyName>")
else:
    CompanyPlaceholder = "<SQLCompanyName>"




    #config_file = "config.json"
    logo_path = os.path.join("UI", "images", "our_logos", "their.logo.png")  # default


    if os.path.exists(config_file):
        with open(config_file, "r") as f:
            config = json.load(f)
            logo_path = config.get("CompanyLogo", logo_path)

    if os.path.exists(logo_path):
        their_logo = Image.open(logo_path)
    else:
        print(f"Warning: Could not find logo at {logo_path}")

















def open_ordering_ui():
    #This subprocess allows you to specify a program to open a specific file
    subprocess.Popen(['python', 'UI/OrderingPage.py'])
    #This closes the current page
    Window.destroy()

def open_about_ui():
    subprocess.Popen(['python', 'UI/about.py'])
    #Window.destroy()

def open_login_ui():
    subprocess.Popen(['python', 'UI/ShiftLogin.py'])
    Window.destroy()

def open_credit_ui():
    subprocess.Popen(['python', 'UI/CreditCard.py'])
    Window.destroy()

def open_loyalty_ui():
    #This subprocess allows you to specify a program to open a specific file
    subprocess.Popen(['python', 'UI/Loyalty.py'])
    #This closes the current page
    Window.destroy()

def open_menu_builder_ui():
    #This subprocess allows you to specify a program to open a specific file
    subprocess.Popen(['python', 'UI/MenuBuilder.py'])
    #This closes the current page
    Window.destroy()

def open_bus_builder_ui():
    #This subprocess allows you to specify a program to open a specific file
    subprocess.Popen(['python', 'UI/UIBuilder.py'])
    #This closes the current page
    Window.destroy()



#Intantiate UI
def Create_Window():
    #Create size of window
    Window.geometry("1024x600")

    #Display Titlebar Message
    Window.title(CompanyPlaceholder+" Powered by TruckBytes")

    #Display Titlebar Icon
    icon_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "TruckBytes.ico")
    if os.path.exists(icon_path):
        Window.iconbitmap(icon_path)
    else:
        print(f"Warning: Icon not found at {icon_path}. Skipping icon set.")

    #Prevents the resizing of hte window
    Window.resizable(False, False)

    #Forces light mode
    set_appearance_mode('light')



#Intantiate Menubar
"""
Instead of a dedicated management page, maybe we should 
just give extra dropdown options to people with management codes
"""
def Create_Menubar():
    #Need to change menubars color, Neither of these worked
    menuBar = Menu(Window)# , background='blue')
    Window.config(menu=menuBar) #,bg_color="#c80d0d")
    #menuBar.configure(bg_color="#c80d0d")

    #Define a Menubar
    file_menu = Menu(menuBar, tearoff=0)

    #File Menu options
    menuBar.add_cascade(label="File", font=14, menu=file_menu)

    #Define File Menu's submenu "About"
    file_menu.add_command(label="About", font=14, command=open_about_ui)

     #Define File Menu's submenu "Close Program"
    file_menu.add_command(label="Close Program", font=14, command=Window.quit)


    #Employee Menu Options
    Employee_Menu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Employee", menu=Employee_Menu)


    #Define Employee menu's submenu "Log In"
    Employee_Menu.add_command(label="Log In", font=14,command=open_login_ui)
    
    #Adds a separator bar
    file_menu.add_separator()
    
    #Define Employee menu's submenu "Log Out"
    Employee_Menu.add_command(label="Logout", font=14,command=open_loyalty_ui)


    
    #Mgmt Menu Options
    Mgmt_Menu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Management", menu=Mgmt_Menu)

    #Define Mgmt menu's submenu "Menu Builder"
    Mgmt_Menu.add_command(label="Menu Builder", font=14,command=open_menu_builder_ui)
    
    #Adds a separator bar
    file_menu.add_separator()
    
    #Define Mgmt menu's submenu "Business Profile"
    Mgmt_Menu.add_command(label="Business Profile", font=14,command=open_bus_builder_ui)

    #Define Mgmt menu's submenu "Analytics"
    Mgmt_Menu.add_command(label="Analytics", font=14,command="")



def Display_Logos_two_thirds():

    #Display "TruckBytes.png" file
    original_logo = Image.open("UI/images/our_logos/TruckBytes.png")
    resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250,250))
    CTkLabel(Window,image=truck_logo, text="").place(x=744,y=320)

    #Display "CompanyLogo.png" file
    company_logo = Image.open("UI/images/our_logos/CompanyLogo.png")
    resized_logo = company_logo.resize((200,200),Image.Resampling.LANCZOS)
    truck2_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250,250))
    CTkLabel(Window,image=truck2_logo, text="").place(x=744,y=33)



def Display_Logo_Center():
    
    #Display Logo
    original_logo = Image.open("UI/images/our_logos/TruckBytes.png")
    resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(200,200))

    imgLogo = CTkLabel(Window,image=truck_logo, text="")
    imgLogo.place(x=412,y=340)