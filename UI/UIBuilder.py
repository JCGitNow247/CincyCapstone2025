from OurDisplay import *
from customtkinter import *
from tkinter import filedialog
import os



truck_logo = None
imgLogo = None

def display_current_logo(img_path=None):
    """Load and display the company logo."""
    global truck_logo, imgLogo

    if img_path is None:
        img_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "their.logo.png")

    if not os.path.exists(img_path):
        print(f"Warning: Could not find image at {img_path}")
        return

    original_logo = Image.open(img_path)
    resized_logo = original_logo.resize((250, 250), Image.Resampling.LANCZOS)
    truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250, 250))

    if imgLogo is None:
        imgLogo = CTkLabel(Window, image=truck_logo, text="")
        imgLogo.place(x=683, y=115)
    else:
        imgLogo.configure(image=truck_logo)


def save_as_png():
    file_path = filedialog.askopenfilename(
        title="Select Your Company Logo",
        initialdir="images",
        filetypes=(("PNG Files", "*.png"), ("All files", "*.*"))
    )
    if file_path:
        display_current_logo(file_path)






def DisplayLabels():
    #Label of the page
    lblTitle = CTkLabel(Window, text="Business Builder", font=('Arial', 32, 'bold'))
    lblTitle.place(x=235,y=20)

    #Create Label for "Company Name"
    CompanyName = CTkLabel(Window, text="Company\nName:", font=('Arial',24))
    CompanyName.place(x=60,y=90)

    #Create Label for "Location"
    lblLocation = CTkLabel(Window, font=('Arial', 24), text="Current\nLocation")
    lblLocation.place(x=60,y=240)



def DisplayFields():
    #Create Textbox for "Company Name"
    txtCompanyNameField = CTkTextbox(Window, width=250,height=40, font=('Arial',24))
    txtCompanyNameField.place(x=200,y=90)

   #Create Textbox for "Location"
    txtLocationField = CTkTextbox(Window, width=250,height=150, font=('Arial',24))
    txtLocationField.place(x=200,y=240)



def DisplayButtons():
    #Create Button to Add Logo
    btnAddImage = CTkButton(Window, font=('Arial', 24), text="Click To Add Logo", width=200, height=50, command=save_as_png)
    btnAddImage.place(x=690,y=30)
    #Create button to Update Info
    btnUpdate = CTkButton(Window, font=('Arial', 24), text="Update Info", width=200, height=50, command="")
    btnUpdate.place(x=690,y=525)



def DisplayCurrentLogo():
    #Display "Food.Image.png" file
    img_path = os.path.join(os.path.dirname(__file__), "images", "our_logos", "their.logo.png")
    if os.path.exists(img_path):
        original_logo = Image.open(img_path)
        resized_logo = original_logo.resize((250, 250), Image.Resampling.LANCZOS)
        truck_logo = CTkImage(light_image=resized_logo, dark_image=resized_logo, size=(250, 250))
        imgLogo = CTkLabel(Window, image=truck_logo, text="")
        imgLogo.place(x=683, y=115)
    else:
        print(f"Warning: Could not find image at {img_path}")

    imgLogo = CTkLabel(Window,image=truck_logo, text="")
    imgLogo.place(x=683,y=115)



#Intantiate UI options
Create_Window()
Create_Menubar()

#Intantiate UI specific to this page
DisplayCurrentLogo()
DisplayLabels()
DisplayFields()
DisplayButtons()


#Create mainloop to run program
Window.mainloop()