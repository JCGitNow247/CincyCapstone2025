#Import TruckBytes Standard UI options
from OurDisplay import *



def setup_ui():

    #ButtonShape Variables
    w = 300
    h = 80
    button_size = {'width': 250, 'height': 80}


    #Label For the whole page
    CTkLabel(Window,
             font=titleFont,
             text="Management Page"
             ).place(x=235,y=45)
    


    # Button configuration: (text, command)
    buttons = [
        ("Truckbytes Ordering", open_ordering_ui),
        ("UI & Location", open_UIbuilder_ui),
        ("Menu Builder", open_menu_builder_ui),
        ("Analytics", open_analytics_ui),
        ("Inventory", inventory_builder_ui),
    ]

    # Layout calculation
    start_x, start_y = 91, 151  # top-left corner of button grid
    x_spacing, y_spacing = 350, 120  # horizontal & vertical spacing
    columns = 2

    for index, (text, command) in enumerate(buttons):
        col = index % columns
        row = index // columns
        x_position = start_x + col * x_spacing
        y_position = start_y + row * y_spacing
        CTkButton(Window,
                   font=font1,
                   text=text,
                   command=command,
                   **button_size).place(x=x_position, y=y_position)


# Initialize window and menus

#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()


#Intantiate UI specific to this page
setup_ui()



#Create mainloop to run program
Window.mainloop()