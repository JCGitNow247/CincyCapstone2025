#Import TruckBytes Standard UI options
from OurDisplay import *



def CreateButtonsAndLabels():
    #Label For Page
    CTkLabel(Window, text="Management Page", font=('Arial', 32)).place(x=235,y=45)
    
    #Create Buttons
    CTkButton(Window, font=('Arial', 24), text="Truckbytes Ordering", width=300, height=80, command=open_ordering_ui).place(x=222,y=119)
    CTkButton(Window, font=('Arial', 24), text="Analytics", width=300, height=80).place(x=222,y=268)
    CTkButton(Window, font=('Arial', 24), text="Menu Builder", width=300, height=80, command=open_menu_builder_ui).place(x=222,y=415)



#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()

CreateButtonsAndLabels()


#Create mainloop to run program
Window.mainloop()