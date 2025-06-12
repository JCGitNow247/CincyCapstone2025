# ttkthemes can be installed using py -m pip install git+https://github.com/RedFantom/ttkthemes
# Must have git installed for the command to work

# Linux install: pip install ttkthemes

from ttkthemes import ThemedTk # type: ignore -- warning with Pylance on VsCode
# import tkinter as tk -- use this import to use Tkinter's default package
from tkinter import ttk # use this import for themes

# function to give the buttons an event
def button_click(button_id):
    # programmatically changing the label's text
    if button_id == 1:
        label.config(text="Button 1 Clicked!")
    elif button_id == 2:
        label.config(text="Button 2 Clicked!")


# here we create the root window to display controls on

# root = tk.Tk() # -- creates a basic Tkinter window
root = ThemedTk('yaru')
root.title("Tkinter Testing")
root.geometry("600x400")

# creating a label, telling it which window to be assigned to and setting the text

# label = tk.Label(root, text="Hello, Tkinter!") # -- creates a basic Tkinter label
label = ttk.Label(root, text="Hello, TTk!")

# .pack() will position the button on the windoww
label.pack()
#label.grid(row=0, column=0) # -- use grid for precise locations

# creating a button, telling it which window to be assigned to, setting the text, and giving it a command (event)
# lambda allows us to give the button a specific argunment to pass to button_click
# without it the button can only call button_click -- ex. command=button_click

# button1 = tk.Button(root, text="Click Me!", command=lambda: button_click(1)) # -- basic Tkinter button
button1 = ttk.Button(root, text="Click Me!", command=lambda: button_click(1))
button1.pack()
#button1.grid(row=10, column=20)

# button2 = tk.Button(root, text="No, Click Me!", command=lambda: button_click(2)) # -- basic Tkinter button
button2 = ttk.Button(root,text="No, Click Me!", command=lambda: button_click(2))
button2.pack()
# button2.grid(row=10, column=50)

# this method begins the display of the window
root.mainloop()