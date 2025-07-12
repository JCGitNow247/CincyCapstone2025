from tkinter import *
from customtkinter import * 
#For some reason messagebox is not included in the import *??


about = CTk()


#Create size of "about"
about.geometry("512x300")

#Display Titlebar Message
about.title("Powered by TruckBytes")

#Display Titlebar Icon
about.iconbitmap("images/our.logos/TruckBytes.ico")

#Prevents the resizing of hte window
about.resizable(False, False)

#Forces light mode
set_appearance_mode('light')




#Create Label 
lblAbout = CTkLabel(about, text="Project by Cole, Adam & Jason", font=('Arial',24), justify="center")
lblAbout.place(x=61, y=100)


about.mainloop()