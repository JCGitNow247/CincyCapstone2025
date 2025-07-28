import os
from tkinter import *

#Used to read json file
import json

#Used to open new .py files
import subprocess

from tkinter import Menu, messagebox
import tkinter.font as tkfont

#Import To Display Images
from PIL import Image ##--## To istall run the following on terminal: pip install Pillow

from customtkinter import * ##--## #To istall, run the following on terminal: pip install customtkinter & pip install customtkinter --upgrade

#Instantiate a window
Window = CTk()

#Variable to link back to json file
CONFIG_FILE = "config.json"
LOGIN_FILE = "login.json"
DEFAULT_COMPANY_NAME = "<SQLCompanyName>"
DEFAULT_LOGO_PATH = os.path.join("UI", "images", "our_logos", "CompanyLogo.png")

CompanyPlaceholder = DEFAULT_COMPANY_NAME
logo_path = DEFAULT_LOGO_PATH

if os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, "r") as config_file:
            contents = config_file.read()
            if contents.strip():
                config_data = json.loads(contents)
            else:
                config_data = {}
            CompanyPlaceholder = config_data.get("CompanyPlaceholder", DEFAULT_COMPANY_NAME)
            logo_path = config_data.get("CompanyLogo", DEFAULT_LOGO_PATH)
    except Exception as e:
        print("ERROR LOADING CONFIG.JSON:", e)
        CompanyPlaceholder = DEFAULT_COMPANY_NAME
        logo_path = DEFAULT_LOGO_PATH

# Load company logo if it exists
if os.path.exists(logo_path):
    their_logo = Image.open(logo_path)
else:
    pass
    #print(f"Warning: Could not find logo at {logo_path}")




#Intantiate UI
def Create_Window():
    #Create size of window
    Window.geometry("1024x600")

    #Prevents the resizing of the window
    Window.resizable(False, False)

    #Forces light mode
    set_appearance_mode('light')

    #Display Titlebar Message
    Window.title(CompanyPlaceholder+" Powered by TruckBytes")

    #Display Titlebar Icon
    icon_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "TruckBytes.ico")
    if os.path.exists(icon_path):
        Window.iconbitmap(icon_path)
    else:
        print(f"Warning: Icon not found at {icon_path}. Skipping icon set.")



def Create_Menubar():
    global is_logged_in
    employee_type_id = None

    try:
        with open(LOGIN_FILE, "r") as f:
            login_data = json.load(f)
            is_logged_in = login_data.get("is_logged_in", False)
            employee_type_id = login_data.get("employee_type_id", None)
    except Exception as e:
        print("Failed to load login state:", e)
        is_logged_in = False
        employee_type_id = None
    
    #Need to change menubars color, Neither of these worked
    menuBar = Menu(Window)# , background='blue')
    Window.config(menu=menuBar) #,bg_color="#c80d0d")
    #menuBar.configure(bg_color="#c80d0d")

    file_menu = Menu(menuBar, tearoff=0) #Define a Menubar

    menuBar.add_cascade(label="File", font=14, menu=file_menu) #File Menu options

    file_menu.add_command(label="About", font=14, command=open_about_ui) #Define File Menu's submenu "About"
    file_menu.add_command(label="Close Program", font=14, command=Window.quit) #Define File Menu's submenu "Close Program"

    #Adds a separator bar
    file_menu.add_separator()
    file_menu.add_separator()
    file_menu.add_separator()

    #Employee Menu Options
    Employee_Menu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Employee", menu=Employee_Menu)
    
    #Define Employee menu's submenu "Log Out"
    Employee_Menu.add_command(label="Logout", font=14, command=logout)
    #Define Employee menu's submenu "Log In"
    Employee_Menu.add_command(label="Log In", font=14, command=open_login_ui)




    
    #Define Employee menu's submenu "Log Out"
    Employee_Menu.add_command(label="Logout",
                                  font=14,
                                  command=open_loyalty_ui)
    
    #Define Employee menu's submenu "Log In"
    Employee_Menu.add_command(label="Log In",
                                font=14,
                                command=open_login_ui)
    
    


    # Show manager menu only 
    Mgmt_Menu = Menu(menuBar, tearoff=0)
    menuBar.add_cascade(label="Management", menu=Mgmt_Menu)
    Mgmt_Menu.add_command(label="Menu Builder", font=14, command=open_menu_builder_ui)
    Mgmt_Menu.add_command(label="Business Profile", font=14, command=open_UIbuilder_ui)
    Mgmt_Menu.add_command(label="Analytics", font=14, command=open_analytics_ui)



 
    #Define Mgmt menu's submenu "Menu Builder"
    Mgmt_Menu.add_command(label="Menu Builder", font=14,command=open_menu_builder_ui)
    
    #Adds a separator bar
    file_menu.add_separator()
    
    #Define Mgmt menu's submenu "Business Profile"
    Mgmt_Menu.add_command(label="Business Profile", font=14,command=open_UIbuilder_ui)

    #Define Mgmt menu's submenu "Analytics"
    Mgmt_Menu.add_command(label="Analytics", font=14,command=open_analytics_ui)
    
    #Define Mgmt menu's submenu "Inventory"
    Mgmt_Menu.add_command(label="Inventory", font=14,command=inventory_builder_ui)

   



# Fuctions to call other ui pages
def _open_ui(filename, close_window=True):
    """Helper to open a UI file and optionally close current window."""
    subprocess.Popen(['python', f'UI/{filename}'])
    if close_window:
        Window.destroy()

def open_analytics_ui(): _open_ui('Analytics.py')
def open_ordering_ui(): _open_ui('OrderingPage.py')
def open_about_ui(): _open_ui('about.py', close_window=False)
def open_login_ui(): _open_ui('ShiftLogin.py')
def open_credit_ui(): _open_ui('CreditCard.py')
def open_loyalty_ui(): _open_ui('Loyalty.py')
def open_menu_builder_ui(): _open_ui('MenuBuilder.py')
def open_UIbuilder_ui(): _open_ui('UIBuilder.py')
def inventory_builder_ui(): _open_ui('InventoryBuilder.py')






# Will log the user in upon success
def login_success():
    global is_logged_in


def logout():
    global is_logged_in

    is_logged_in = False

    login_data = {
        "is_logged_in": False,
        "employee_id": None,
        "employee_type_id": None
    }

    with open("login.json", "w") as f:
        json.dump(login_data, f, indent=4)

    open_loyalty_ui()

#Fuctions for UI setup type
def Display_Logos_two_thirds():

    #Display "TruckBytes.png" file
    original_logo = Image.open("UI/images/our_logos/TruckBytes.png")
    resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo,
                          dark_image=resized_logo,
                          size=(250,250))
    CTkLabel(Window,
             image=truck_logo,
             text="").place(x=744,y=320)
    
  
    #Display "CompanyLogo.png" file
    company_logo = Image.open("UI/images/our_logos/CompanyLogo.png")
    resized_logo = company_logo.resize((200,200),Image.Resampling.LANCZOS)
    truck2_logo = CTkImage(light_image=resized_logo,
                           dark_image=resized_logo,
                           size=(250,250))
    CTkLabel(Window,
             image=truck2_logo,
             text="").place(x=744,y=33)


def Display_Logo_Center():
    
    #Display Logo
    original_logo = Image.open("UI/images/our_logos/TruckBytes.png")
    resized_logo = original_logo.resize((200,200),Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo,
                          dark_image=resized_logo,
                          size=(200,200))

    imgLogo = CTkLabel(Window,image=truck_logo,
                       text="")
    imgLogo.place(x=412,y=340)