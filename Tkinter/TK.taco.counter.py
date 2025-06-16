# For TKinter Documentation, here is a link https://docs.python.org/3/library/tkinter.html#packer-options

# ttkthemes can be installed using py -m pip install git+https://github.com/RedFantom/ttkthemes
# Must have git installed for the command to work

# Linux install: pip install ttkthemes

# Imports everything releated to tkinter
from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images.
# windows = serves as a container to hold or contain these widgets.
# label = an area widget that holds text and/or an image within a window.
# You can either use pack or place for inserting a label onto the window.

Count = 0 #Global Variable

# When the button is clicked, the global variable count goes up by 1 and gets displayed on the GUI.
def Click():
    global Count
    Count += 1
    DisplayButtonCount.config(text=Count)

Window = Tk() #Instantiate an instance of a window
Window.title("TruckBytes POS System") #Adds a title to the title bar
Window.geometry("1250x1250") #Sets the height and width of the default state of the window

#Icon = PhotoImage(file=r"images/our.logos/TruckBytes.png") #Creates a variable linking the variable to a specified image
#Window.iconphoto(True, Icon) #Sets the icon to the window, if true is selected then the icon applies to the main window and any child windows. (there seems to be a bit of nuance to this command)
Window.config(background="#5cfcff") #Sets the background color of the window to the specified color.

#Photo = PhotoImage(file=r"images/our.logos/TruckBytes.POS.Blue.png")

# Option are key word arguments that we can pass in to the constructor for this widget
#The parenthisis acts as a constructor for the label which can then pass in arguments to modify the label.
label = Label(Window, #the container
              text="Thank You for ordering with us", #Text for label.
              font=('Arial', 40, 'bold'), #Font for label.
              fg="#46f346", #foreground color for the label, the text itself.
              bg='Black', #The background color of the label.
              relief=RAISED, #Determines what the border style of a widget will be. Legal values are: "raised", "sunken", "flat", "groove", and "ridge".
              bd=10, #This is the boarder width.
              padx=20, #This allows for padding between the text and the boarder in the x axis.
              pady=20, #This allows for padding between the text and the boarder in the y axis.
              #image=Photo, #This adds the photo image to the label.
              compound="bottom") #Sets a direction for where the image is supposed to be placed relative to the text that it is tied to.

button = Button(Window, text='Click to add a taco to your order') #instance of a button
button.config(command=Click) #Performs call back of function
button.config(font=('Ink Free', 50, 'bold'))
button.config(bg='#ff6200') #background color of the button
button.config(fg='#fffb1f') #foreground color of the button
button.config(activebackground='#FF0000') #The active background color of the button (when the button has been clicked)
button.config(activeforeground='#fffb1f') #The active foreground color of the button (when the button has been clicked)
# Button.config(state=DISABLED) #Disabled Button (ACTIVE/DISABLED)

DisplayButtonCount = Label(Window, text=Count) #Instance of a label that sets a text value to the value of the global variable count
DisplayButtonCount.config(font=('Monospace', 50)) #Configurations for the button, the font and size.

# Adds all the widgets to the window.
DisplayButtonCount.pack()
button.pack()
label.pack()


Window.mainloop() #Place window on computer screen, listen for events