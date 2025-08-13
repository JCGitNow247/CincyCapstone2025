#Import TruckBytes Standard UI options
from OurDisplay import *
from DatabaseUtility import *
import re

import DatabaseUtility as DB



def setup_ui():
    global txtUsernameField, txtPasswordField

    #Standard width
    w = 200
    
    #Labels
    CTkLabel(Window,
             font=titleFont,
             text="Employee Login"
             ).place(x=400, y=50)
    
    CTkLabel(Window,
             font=font1,
            text="Last Name:"
             ).place(x=240, y=170)
    
    CTkLabel(Window,
             font=font1,
            text="Password:"
            ).place(x=240, y=215)

    #Entry Field
    txtUsernameField = CTkEntry(Window,
                                font=font1,
                                  width=w,
                                  height=35)
    txtUsernameField.place(x=412, y=170)

    txtPasswordField = CTkEntry(Window,
                                font=font1,
                                width=w,
                                height=35,
                                show="*")
    txtPasswordField.place(x=412, y=215)


    #Login Button
    CTkButton(Window, text="Login",
              font=font1,
              width=w,
              height=40,
              command=validate_fields
              ).place(x=412, y=270)



    #Valid Data to speed though validation
    def dummyData():
        txtUsernameField.insert(0, "Davis")
        txtPasswordField.insert(0, "4567")
        pass


    #Call for insert of valid data
    dummyData()


def show_invalid_msg():
    # This function displays messagebox Titlebar & then message
    messagebox.showinfo("Invalid Password", "Invalid Password\nPlease Try Again")
   
    pop_button= Button(Window,text="", command=show_invalid_msg)
    pop_button.pack(padx=30, pady=45)
    


#Validate user inputs
def validate_fields():
    employee_name = txtUsernameField.get().strip()
    password = txtPasswordField.get().strip()
 

    name_regex = r"^[A-Za-z\s\-']{2,50}$"
    if not re.match(name_regex, employee_name):
        messagebox.showerror("Invalid Name", "Please enter a valid name")
        return False
    

    #Validates Passwords
    if (len(password) <= 3):
        messagebox.showerror("Invalid Password", "Password must be at least 4 digits.")

        #Because the password was rejected, the password is removed
        txtPasswordField.delete(0, 'end')
        return False
    
    if not validate_employee_credentials(employee_name, password):
        messagebox.showerror("Login Failed", "Invalid last name or password")
        return False
    else:

        employeeID = get_employeeID(employee_name, password)
        if check_employee_logged_out(employeeID) == False:
            messagebox.showerror("Login Failed", f"Employee:\n{employee_name}\nis already logged in")
            return

        #####################
        ## Sucessful Login ##
         ####################
     
        messagebox.showinfo("Login Sucessful","Employee:\n"+ employee_name + "\nHas logged in.")

        #Insert login record
        shiftID = create_shift()
        insert_login_record(employeeID, shiftID)
    
        # Fetch employee type ID
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("""
            SELECT intEmployeeTypeID
            FROM Employees
            WHERE strLastName = %s AND strPassword = %s
        """, (employee_name, password))
        emp_type_id = cursor.fetchone()[0]
        conn.close()

        # Open the correct UI
        if emp_type_id == 2:
            open_Mgmt_ui()
        else:
            open_ordering_ui()

    return True
  


# Validates to see if employee credentials are in the database.
def validate_employee_credentials(last_name, password):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        SELECT COUNT(*) FROM Employees
        WHERE strLastName = %s AND strPassword = %s
    """
    cursor.execute(query, (last_name, password))
    result = cursor.fetchone()[0]
    conn.close()

    return result > 0



def handle_login():
    if validate_fields():
        #Fetch user data
        conn = get_connection()
        cursor = conn.cursor()

        last_name = txtUsernameField.get().strip()
        password = txtPasswordField.get().strip()

        query = """
            SELECT intEmployeeID, intEmployeeTypeID FROM Employees
            WHERE strLastName = %s AND strPassword = %s
        """
        cursor.execute(query, (last_name, password))
        row = cursor.fetchone()
        conn.close()

        if row:
            emp_id, emp_type_id = row
            login_data = {
                "is_logged_in": True,
                "employee_id": emp_id,
                "employee_type_id": emp_type_id
            }
            with open("login.json", "w") as f:
                json.dump(login_data, f, indent=4)

        login_success()
        open_ordering_ui()



#Intantiate UI specific to this page
setup_ui()

#Intantiate UI options
Create_Window()
Create_Menubar()
Display_Logo_Center()



Window.mainloop()