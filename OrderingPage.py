from our_display import *

Create_Window()
Create_Menubar()










#Label of the page
lblTitle = CTkLabel(Window, text="Welcome To The Ordering Page", font=('Arial', 32))
lblTitle.place(x=105,y=40)

#Label to show Total
lblTotal = CTkLabel(Window, text="Total:", font=('Arial',20))
lblTotal.place(x=735,y=525)

Item1 = "SQL Item1"
Item2 = "SQL Item2"
Item3 = "SQL Item3"
Item4 = "SQL Item4"
Item5 = "SQL Item5"
Item6 = "SQL Item6"




#Do we need to create geometery based on number of items in the menu?

def open_sub_menu():
    new = Toplevel()


#Button
btnSubmit = CTkButton(Window, text="Submit", font=('Arial',20), width=200, height=50)
btnSubmit.place(x=735,y=45)

btnItem1 = CTkButton(Window, font=('Arial', 20), text=Item1, width=200, height=80)
btnItem1.place(x=94,y=119)

btnItem2 = CTkButton(Window, font=('Arial', 20), text=Item2, width=200, height=80)
btnItem2.place(x=94,y=268)

btnItem3 = CTkButton(Window, font=('Arial', 20), text=Item3, width=200, height=80)
btnItem3.place(x=94,y=415)

btnItem4 = CTkButton(Window, font=('Arial', 20), text=Item4, width=200, height=80)
btnItem4.place(x=388,y=119)

btnItem5 = CTkButton(Window, font=('Arial', 20), text=Item5, width=200, height=80)
btnItem5.place(x=388,y=268)

btnItem6 = CTkButton(Window, font=('Arial', 20), text=Item6, width=200, height=80, command= open_sub_menu)
btnItem6.place(x=388,y=415)






Window.mainloop()