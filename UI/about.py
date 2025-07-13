from tkinter import *
from customtkinter import * 
#For some reason messagebox is not included in the import *??


about = CTk()


#Create size of "about"
#about.geometry("512x300")
#Creates geometry of "about". 1st & 2nd arguements are size, 3rd & 4th are screen location
about.geometry("512x300+560+490")



#Display Titlebar Message
about.title("Powered by TruckBytes")

#Display Titlebar Icon
about.iconbitmap("images/our.logos/TruckBytes.ico")

#Prevents the resizing of hte window
about.resizable(False, False)

#Forces light mode
set_appearance_mode('light')




#Create Label 
lblAbout = CTkLabel(about, text="Project by Cole Whitaker\nAdam Broderick\n&\nJason Cope\n2025 Summer Capstone", font=('Arial',24), justify="center")
lblAbout.place(x=125, y=65)


about.mainloop()