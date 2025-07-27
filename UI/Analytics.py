#Import TruckBytes Standard UI options
from OurDisplay import *
import DatabaseUtility as DB

def display_analytics():
    total_sales = DB.get_total_sales()
    sales_by_day = DB.get_sales_by_day()
    sales_by_payment = DB.get_sales_by_payment_type()

    # Create a centered frame
    analytics_frame = CTkFrame(Window, width=600, height=500, corner_radius=15)
    analytics_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Total Sales
    CTkLabel(analytics_frame, text=f"Total Sales: ${total_sales:.2f}", font=('Arial', 28, 'bold')).place(x=150, y=20)

    # Sales by Day Title
    CTkLabel(analytics_frame, text="Sales by Day", font=('Arial', 20, 'bold')).place(x=30, y=80)

    y_offset = 120
    for date, amount in sales_by_day:
        CTkLabel(analytics_frame, text=f"{date}: ${amount:.2f}", font=('Arial', 16)).place(x=40, y=y_offset)
        y_offset += 30

    # Sales by Payment Type Title
    CTkLabel(analytics_frame, text="Sales by Payment Type", font=('Arial', 20, 'bold')).place(x=300, y=80)

    y_offset = 120
    for pay_type, amount in sales_by_payment:
        CTkLabel(analytics_frame, text=f"Type {pay_type}: ${amount:.2f}", font=('Arial', 16)).place(x=310, y=y_offset)
        y_offset += 30


#Intantiate UI options
Create_Window()
Create_Menubar()
display_analytics()


Window.mainloop()