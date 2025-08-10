#Import TruckBytes Standard UI options
from OurDisplay import *
import DatabaseUtility as DB

def display_analytics():
    total_sales = DB.get_total_sales()
    sales_by_day = DB.get_sales_by_day()
    sales_by_payment = DB.get_sales_by_payment_type()
    total_hours = DB.get_total_hours_worked()
    payroll_data = DB.get_employee_payroll()

    avg_sale = DB.get_average_sale()
    top_items = DB.get_top_selling_items(limit=5)
    repeat_customers = DB.get_repeat_customer_count()
    sales_this_week = DB.get_sales_this_week()
    sales_last_year_week = DB.get_sales_same_week_last_year()





    # Create a centered scrollable frame
    analytics_frame = CTkScrollableFrame(Window, width=600, height=500, corner_radius=15)
    analytics_frame.place(relx=0.5, rely=0.5, anchor="center")

    # Total Sales
    CTkLabel(analytics_frame, text=f"Total Sales: ${total_sales:.2f}", font=('Arial', 28, 'bold')).pack(pady=(20, 10))


   #CTkLabel(analytics_frame, text=f"Total Sales: ${total_sales:.2f}", font=('Arial', 28, 'bold')).pack(pady=(20, 10))
    CTkLabel(analytics_frame, text=f"Average Sale: ${avg_sale:.2f}", font=('Arial', 20)).pack()




    # Two-column Sales (wrap in a frame)
    sales_frame = CTkFrame(analytics_frame)
    sales_frame.pack(pady=(10, 10), fill="x")

    left_col = CTkFrame(sales_frame)
    right_col = CTkFrame(sales_frame)
    left_col.pack(side="left", padx=40)
    right_col.pack(side="right", padx=40)

    # Sales by Day
    CTkLabel(left_col, text="Sales by Day", font=('Arial', 20, 'bold')).pack(anchor="w")
    for date, amount in sales_by_day:
        CTkLabel(left_col, text=f"{date}: ${amount:.2f}", font=('Arial', 16)).pack(anchor="w")

    # Sales by Payment Type
    CTkLabel(right_col, text="Sales by Payment Type", font=('Arial', 20, 'bold')).pack(anchor="w")
    for pay_type, amount in sales_by_payment:
        CTkLabel(right_col, text=f"Type {pay_type}: ${amount:.2f}", font=('Arial', 16)).pack(anchor="w")




    # Top-selling items
    CTkLabel(analytics_frame, text="Top Selling Items", font=('Arial', 20, 'bold')).pack(pady=(20, 5))
    for item, qty in top_items:
        CTkLabel(analytics_frame, text=f"{item}: {qty} sold", font=('Arial', 16)).pack(anchor="w", padx=40)

    # Repeat customers
    CTkLabel(analytics_frame, text=f"Repeat Customers: {repeat_customers}", font=('Arial', 20, 'bold')).pack(pady=(20, 5))


    CTkLabel(analytics_frame,
            text=f"Sales This Week: ${sales_this_week:.2f}",
            font=('Arial', 20, 'bold')).pack(pady=(5, 5))

    CTkLabel(analytics_frame,
            text=f"Same Week Last Year: ${sales_last_year_week:.2f}",
            font=('Arial', 20, 'bold')).pack(pady=(5, 20))






    # Total Hours Worked
    CTkLabel(analytics_frame, text=f"Total Hours Worked: {total_hours} hrs", font=('Arial', 20, 'bold')).pack(pady=(20, 5))
    
    # Employee Payroll
    CTkLabel(analytics_frame, text="Employee Payroll", font=('Arial', 20, 'bold')).pack(pady=(10, 5))
    for _, name, hours, rate, pay in payroll_data:
        text = f"{name}: {hours} hrs @ ${rate:.2f} = ${pay:.2f}"
        CTkLabel(analytics_frame, text=text, font=('Arial', 16)).pack(anchor="w", padx=40)

        CTkButton(Window,
            font=font1,
            text="Return\nTo\nMangemant\nPage",
            width=60,
            height=60,
            command=open_Mgmt_ui
            ).place(x=18,y=45)

#Intantiate UI options
Create_Window()
Create_Menubar()
display_analytics()


Window.mainloop()