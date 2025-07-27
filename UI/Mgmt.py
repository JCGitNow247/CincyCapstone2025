#Import TruckBytes Standard UI options
from OurDisplay import *



def setup_ui():

    #ButtonShape Variables
    w = 300
    h = 80
    #f = ('Arial', 24)

    #Label For the whole page
    CTkLabel(Window,
             text="Management Page",
             font=('Arial', 32)).place(x=235,y=45)
    
    #Create Buttons
    CTkButton(Window,text="Truckbytes Ordering",
              width=w,
              height=h,
              font=('Arial', 24),
              command=open_ordering_ui).place(x=222,y=119)
    
    CTkButton(Window, text="Analytics",
              width=w,
              height=h,
              font=('Arial', 24),
              command=open_analytics_ui).place(x=222,y=268)
    
    CTkButton(Window,
            text="Menu Builder",
              width=w,
              height=h,
              font=('Arial', 24),
              command=open_menu_builder_ui).place(x=222,y=415)
    
    CTkButton(Window, 
              text="UI & Location",
              width=w,
              height=h,
              font=('Arial', 24),
              command=open_analytics_ui).place(x=222,y=515)


#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()


#Intantiate UI specific to this page
setup_ui()



#Create mainloop to run program
Window.mainloop()