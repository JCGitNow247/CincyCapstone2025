#Import TruckBytes Standard UI options
from OurDisplay import *
import DatabaseUtility as DB

def display_analytics():
    total_sales = DB.get_total_sales()
    sales_by_day = DB.get_sales_by_day()
    sales_by_payment = DB.get_sales_by_payment_type()

    CTkLabel(Window, text=f"Total Sales: ${total_sales:.2f}", font=('Arial', 24)).pack(pady=20)

    CTkLabel(Window, text="Sales by Day", font=('Arial', 20, 'bold')).pack()
    for date, amount in sales_by_day:
        CTkLabel(Window, text=f"{date}: ${amount:.2f}", font=('Arial', 16)).pack()

    CTkLabel(Window, text="Sales by Payment Type", font=('Arial', 20, 'bold')).pack(pady=(20, 0))
    for pay_type, amount in sales_by_payment:
        CTkLabel(Window, text=f"Type {pay_type}: ${amount:.2f}", font=('Arial', 16)).pack()

#Intantiate UI options
Create_Window()
Create_Menubar()
display_analytics()


Window.mainloop()