#Import TruckBytes Standard UI options
from our_display import *




#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logos23()


#Label of the page
lblTitle = CTkLabel(Window, text="Management Page", font=('Arial', 32))
lblTitle.place(x=235,y=45)


#Create Buttons
btnOrder = CTkButton(Window, font=('Arial', 24), text="Truckbytes Ordering", width=300, height=80)
btnOrder.place(x=222,y=119)

btnAnalytics = CTkButton(Window, font=('Arial', 24), text="Analytics", width=300, height=80)
btnAnalytics.place(x=222,y=268)

btnMenuBuilder = CTkButton(Window, font=('Arial', 24), text="Menu Builder", width=300, height=80)
btnMenuBuilder.place(x=222,y=415)




#Create mainloop to run program
Window.mainloop()