#Import TruckBytes Standard UI options
from OurDisplay import *



def setup_ui():

    #ButtonShape Variables
    w = 300
    h = 80
    f = ('Arial', 24)
    button_size = {'width': 300, 'height': 80}


    #Label For the whole page
    CTkLabel(Window,
             text="Management Page",
             font=('Arial', 32)).place(x=235,y=45)
    

    # Button configuration: (text, command)
    buttons = [
        ("Truckbytes Ordering", open_ordering_ui),
        ("Analytics", open_analytics_ui),
        ("Menu Builder", open_menu_builder_ui),
        ("UI & Location", open_bus_builder_ui),
        ("Inventory", inventory_builder_ui),
    ]

    # Layout calculation
    start_y = 120       # where the first button appears
    spacing = 80       # vertical distance between buttons
    x_position = 222

    for index, (text, command) in enumerate(buttons):
        y_position = start_y + index * spacing
        CTkButton(Window, text=text, font=f, command=command, **button_size).place(x=x_position, y=y_position)



#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()


#Intantiate UI specific to this page
setup_ui()



#Create mainloop to run program
Window.mainloop()