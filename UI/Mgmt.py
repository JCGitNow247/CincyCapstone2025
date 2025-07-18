#Import TruckBytes Standard UI options
from OurDisplay import *



#Label of the page
lblTitle = CTkLabel(Window, text="Management Page", font=('Arial', 32))
lblTitle.place(x=235,y=45)



#Create Buttons
btnOrder = CTkButton(Window, font=('Arial', 24), text="Truckbytes Ordering", width=300, height=80, command=open_ordering_ui)
btnOrder.place(x=222,y=119)

btnAnalytics = CTkButton(Window, font=('Arial', 24), text="Analytics", width=300, height=80)
btnAnalytics.place(x=222,y=268)

btnMenuBuilder = CTkButton(Window, font=('Arial', 24), text="Menu Builder", width=300, height=80, command=open_menu_builder_ui)
btnMenuBuilder.place(x=222,y=415)



#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos_two_thirds()



#Create mainloop to run program
Window.mainloop()