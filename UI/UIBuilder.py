from OurDisplay import *
from customtkinter import *
from tkinter import filedialog
import os
import json
import shutil













if os.path.exists(CONFIG_FILE):
    try:
        with open(CONFIG_FILE, "r") as config_file:
            contents = config_file.read()
            config_data = json.loads(contents) if contents.strip() else {}
            CompanyPlaceholder = config_data.get("CompanyPlaceholder", DEFAULT_COMPANY_NAME)
            
    except Exception as e:
        print("Failed to read config.json:", e)
        CompanyPlaceholder = DEFAULT_COMPANY_NAME





truck_logo = None
imgLogo = None

def display_current_logo(img_path=None):
    """Load and display the company logo."""
    global truck_logo, imgLogo

    if img_path is None:
        img_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "CompanyLogo.png")

    if not os.path.exists(img_path):
        print(f"Warning: Could not find image at {img_path}")
        return

    original_logo = Image.open(img_path)
    resized_logo = original_logo.resize((250, 250), Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250, 250))

    if imgLogo is None:
        imgLogo = CTkLabel(Window, image=truck_logo, text="").place(x=683, y=150)
    else:
        imgLogo.configure(image=truck_logo)



def save_as_png():
  
    file_path = filedialog.askopenfilename(
        title="Select Your Company Logo",
        initialdir="UI/images/Company_images",
        filetypes=(("PNG Files", "*.png"), ("All files", "*.*"))
    )
    if file_path:
        # Copy the new logo into your app's logos folder
        logo_folder = os.path.join(os.path.dirname(__file__), "images", "our_logos")
        if not os.path.exists(logo_folder):
            os.makedirs(logo_folder)
        
        new_logo_path = os.path.join(logo_folder, "CompanyLogo.png")
        shutil.copy(file_path, new_logo_path)

        # Save the path in config.json
        config_file = "config.json"
        config = {}
        if os.path.exists(config_file):
            with open(config_file, "r") as f:
                config = json.load(f)
        config["CompanyLogo"] = new_logo_path
        with open(config_file, "w") as f:
            json.dump(config, f)

        display_current_logo(new_logo_path)








def setup_basic_ui():
 
    global txtCompanyNameField, txtLocationField

    #Create Textbox for "Location"
    txtLocationField = CTkTextbox(Window,
                                  font=font1,
                                  width=250,
                                  height=150)
    txtLocationField.place(x=200,y=240)

    #Create Textbox for "Company Name"
    txtCompanyNameField = CTkTextbox(Window,
                                     font=font1,
                                     width=250,
                                     height=40)
    txtCompanyNameField.place(x=200,y=90)


   #Label of the page
    CTkLabel(Window,
             font=titleFont,
             text="Business Builder"
             ).place(x=235,y=20)
    
    #Create Label for "Company Name"
    CTkLabel(Window,
             font=font1,
             text="Company\nName:"
             ).place(x=60,y=90)
    
    #Create Label for "Location"
    CTkLabel(Window,
             font=font1,
             text="Current\nLocation:"
             ).place(x=60,y=240)


    #Create Button to Add Logo
    CTkButton(Window, font=font1,
              text="Click To Add Logo",
              width=200,
              height=50,
              command=save_as_png
              ).place(x=705,y=50)
    

    #Create button to Update Info
    CTkButton(Window,
              font=titleFont,
              text="Update Info",
              width=300,
              height=80,
              command=update_company_name
              ).place(x=660,y=445)



def DisplayCurrentLogo():
    #Display "Food.Image.png" file
    img_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "CompanyLogo.png")
    if os.path.exists(img_path):
        original_logo = Image.open(img_path)

        resized_logo = original_logo.resize((250, 250), Image.Resampling.LANCZOS)
        truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250, 250))
        CTkLabel(Window, image=truck_logo, text="").place(x=683, y=150)
    else:
        print(f"Warning: Could not find image at {img_path}")

    #CTkLabel(Window,image=truck_logo, text="").place(x=683,y=145)



def update_company_name():
    global CompanyPlaceholder


    CompanyPlaceholder = txtCompanyNameField.get("1.0", "end").strip()
    LocationPlaceholder = txtCompanyNameField.get("1.0", "end").strip()
    Window.title(CompanyPlaceholder + " Powered by TruckBytes")

    #Save both values to config.json
    config = {
        "CompanyPlaceholder": CompanyPlaceholder,
        "LocationPlaceholder": LocationPlaceholder
    }
    with open("config.json", "w") as f:
        json.dump(config, f)

    # Update window title
    Window.title(f"{CompanyPlaceholder} - {LocationPlaceholder} Powered by TruckBytes")
    Window.title(CompanyPlaceholder + " Powered by TruckBytes")


    '''
def update_company_Location():
    global LocationPlaceholder
    LocationPlaceholder = txtCompanyNameField.get("1.0", "end").strip()
    Window.title(LocationPlaceholder + " Powered by TruckBytes")

    # Save the updated name permanently in config.json
    with open("config.json", "w") as f:
        json.dump({"CompanyPlaceholder": CompanyPlaceholder}, f)
    Window.title(CompanyPlaceholder + " Powered by TruckBytes")
    '''


#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
DisplayCurrentLogo()
setup_basic_ui()



#Create mainloop to run program
Window.mainloop()