from flask import Flask, request, jsonify
import mariadb

from flask_cors import CORS
import datetime
import random

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

# Path to here to start python backend servers.
# cd WebsiteCode\truckbyte_site\PythonBackend
# run python Backend.py to start the script.

# Connects to the MariaDB database
def get_connection():
    try:
        conn = mariadb.connect(
            host='localhost',
            user='truckbytesdev',
            password='tb001',
            port=3306,
            database='dbTruckBytes'
        )
        return conn
    except mariadb.Error as e:
        return jsonify({"error": str(e)})

# Gets a list of all menu items
@app.route('/get-menu')
def get_menu():

    conn = get_connection()
    cursor = conn.cursor(named_tuple=True)
    cursor.execute("SELECT MenuItemID, MenuItemName, MenuItemDescription, MenuItemPrice FROM VMenuItems")
    rows = cursor.fetchall()

    items = []
    for row in rows:
        items.append({
            'id': row.MenuItemID,
            'name': row.MenuItemName,
            'description': row.MenuItemDescription if row.MenuItemDescription is not None else '',
            'price': float(row.MenuItemPrice)
        })

    conn.close()
    return jsonify(items)

# Gets available modifier options for a specific menu item
@app.route('/get-modifiers')
def get_modifiers():
    item_name = request.args.get('item')  # Get ?item= from URL
    if not item_name:
        return jsonify([])

    conn = get_connection()
    cursor = conn.cursor(named_tuple=True)

    # Get submenu ID from menu item name
    cursor.execute("""
        SELECT intSubMenuID
        FROM MenuItems
        WHERE strMenuItemName = %s
    """, (item_name,))
    result = cursor.fetchone()

    if not result or not result[0]:
        conn.close()
        return jsonify([])

    submenu_id = result[0]

    # Get foods from that submenu
    cursor.execute("""
        SELECT f.strFoodName, f.dblSellPrice
        FROM SubMenusFoods smf
        JOIN Foods f ON smf.intFoodID = f.intFoodID
        WHERE smf.intSubMenuID = %s
        ORDER BY f.strFoodName
    """, (submenu_id,))

    rows = cursor.fetchall()
    conn.close()

    modifiers = [{"name": row.strFoodName, "price": float(row.dblSellPrice)} for row in rows]
    return jsonify(modifiers)

# Returns a list of available trucks
@app.route('/get-trucks')
def get_trucks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT intTruckNumber, strTruckName FROM Trucks");
    rows = cursor.fetchall()
    trucks = [{"id": row[0], "name": row[1]} for row in rows]
    return jsonify(trucks)

# Checks if a customer exists based on phone/email
@app.route('/check-customer', methods=['POST'])
def check_customer():
    data = request.get_json()

    phone = data['phone'].strip()
    email = data['email'].strip()

    print(f"Checking loyalty for {email}, {phone}")

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT intCustomerID
        FROM Customers
        WHERE strPhoneNumber = %s AND strEmail = %s
    """, (phone, email))

    result = cursor.fetchone()
    conn.close()

    return jsonify({ "exists": result is not None })

# Registers a new customer and assigns a random loyalty reward
@app.route('/register-customer', methods=['POST'])
def register_customer():
    data = request.get_json()

    phone = data['phone'].strip()
    email = data['email'].strip()

    conn = get_connection()
    cursor = conn.cursor()

    # Insert new customer
    cursor.execute("""
        INSERT INTO Customers (strEmail, strPhoneNumber)
        VALUES (%s, %s)
    """, (email, phone))

    # Optional: assign random reward if LoyaltyRewards table exists
    cursor.execute("SELECT intLoyaltyRewardID FROM LoyaltyRewards ORDER BY RAND() LIMIT 1")
    reward = cursor.fetchone()
    customer_id = cursor.lastrowid

    if reward:
        cursor.execute("""
            INSERT INTO LoyaltyMembers (intCustomerID, intLoyaltyRewardID)
            VALUES (%s, %s)
        """, (customer_id, reward[0]))

    conn.commit()
    conn.close()

    return jsonify({ "success": True })

# Applies loyalty rewards for an existing customer
@app.route('/apply-loyalty', methods=['POST'])
def apply_loyalty():
    data = request.get_json()
    email = data['strEmail'].strip()
    phone = data['strPhoneNumber'].strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Corrected query using actual column names
    cursor.execute("""
        SELECT c.intCustomerID, r.strLoyaltyRewardType
        FROM Customers c
        LEFT JOIN LoyaltyMembers lm ON c.intCustomerID = lm.intCustomerID
        LEFT JOIN LoyaltyRewards r ON lm.intLoyaltyRewardID = r.intLoyaltyRewardID
        WHERE c.strEmail = %s AND c.strPhoneNumber = %s
    """, (email, phone))

    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({
            "success": True,
            "customerID": result["intCustomerID"],
            "reward": result["strLoyaltyRewardType"]
        })
    else:
        return jsonify({ "success": False })

# Gets list of available drinks (used for free drink loyalty reward)        
@app.route('/get-drinks', methods=['GET'])
def get_drinks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT strFoodName FROM foods WHERE intFoodTypeID = 3")
    drinks = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(drinks)

# Handles employee login by matching username and password
@app.route('/login-employee', methods=['POST'])
def login_employee():
    data = request.get_json()
    username = data['username'].strip()
    password = data['password'].strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT e.intEmployeeID, et.strEmployeeType
        FROM Employees e
        JOIN EmployeeTypes et ON e.intEmployeeTypeID = et.intEmployeeTypeID
        WHERE e.strUserName = %s AND e.strPassword = %s
    """, (username, password))

    result = cursor.fetchone()
    conn.close()

    if result:
        return jsonify({
            "success": True,
            "employeeID": result["intEmployeeID"],
            "role": result["strEmployeeType"]
        })
    else:
        return jsonify({ "success": False })

# Temporary in-memory storage of submitted orders
active_orders_cache = []

# Returns list of currently active orders
@app.route('/get-active-orders')
def get_active_orders():
    # Return just the orders stored in the cache (placed via /submit-order)
    return jsonify(active_orders_cache)  # reverse to show newest first

# Handles new order submission, saves to DB, and caches the order for display
@app.route('/submit-order', methods=['POST'])
def submit_order():
    data = request.get_json()
    items = data.get("items", [])
    total = float(data.get("total", 0))
    customer_id = data.get("customerID")
    free_drink = data.get("freeDrink")
    truck_id = int(data.get("truckID", 1))

    conn = get_connection()
    cursor = conn.cursor()

    # Insert Sale
    cursor.execute("""
        INSERT INTO Sales (dblSaleAmount, dtmDate, intSalesPaymentTypeID)
        VALUES (%s, NOW(), 1)
    """, (total,))
    sale_id = cursor.lastrowid

    # Insert Order 
    cursor.execute("""
        INSERT INTO Orders (intTruckID, intSaleID, intCustomerID, strStatus)
        VALUES (%s, %s, %s, %s)
    """, (truck_id, sale_id, customer_id if customer_id else None, "Paid"))
    order_id = cursor.lastrowid

    conn.commit()
    conn.close()

    # Combine all items into 1 string description
    description_lines = [item.get("html", "") for item in items]
    if free_drink:
        description_lines.append(f"<em>Free Drink: {free_drink}</em>")

    description_html = "<br>".join(description_lines)

    # Store in the temporary cache
    active_orders_cache.append({
        "id": order_id,
        "time": datetime.datetime.now().isoformat(),
        "description": description_html
    })

    return jsonify({ "success": True, "id": order_id })

# Provides summary analytics including total sales, sales by day, and payroll info
@app.route('/get-analytics-summary')
def get_analytics_summary():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Total Sales + By Day
    cursor.execute("""
        SELECT 
            SUM(dblSaleAmount) AS total_sales
        FROM Sales
    """)
    total_sales = cursor.fetchone()['total_sales'] or 0

    cursor.execute("""
        SELECT 
            DATE(dtmDate) AS sale_date,
            SUM(dblSaleAmount) AS amount
        FROM Sales
        GROUP BY sale_date
        ORDER BY sale_date
    """)
    sales_by_day = cursor.fetchall()

    # Sales by Payment Type
    cursor.execute("""
        SELECT 
            spt.strSalesPaymentType AS type,
            SUM(s.dblSaleAmount) AS total
        FROM Sales s
        JOIN SalesPaymentTypes spt ON s.intSalesPaymentTypeID = spt.intSalesPaymentTypeID
        GROUP BY spt.strSalesPaymentType
    """)
    payment_breakdown = cursor.fetchall()

    # Total Hours Worked
    cursor.execute("""
        SELECT 
            SUM(TIMESTAMPDIFF(HOUR, dtmShiftStart, dtmShiftEnd)) AS total_hours
        FROM EmployeesShifts
    """)
    total_hours = cursor.fetchone()['total_hours']

    # Employee Payroll Breakdown
    cursor.execute("""
        SELECT 
            CONCAT(e.strFirstName, ' ', e.strLastName) AS name,
            e.dblHourlyRate AS rate,
            SUM(TIMESTAMPDIFF(HOUR, es.dtmShiftStart, es.dtmShiftEnd)) AS hours
        FROM EmployeesShifts es
        JOIN Employees e ON es.intEmployeeID = e.intEmployeeID
        GROUP BY e.intEmployeeID
    """)
    payroll = cursor.fetchall()

    conn.close()
    return jsonify({
        "total_sales": total_sales,
        "sales_by_day": sales_by_day,
        "payment_breakdown": payment_breakdown,
        "total_hours": total_hours,
        "payroll": payroll
    })




@app.route('/api/paid-orders')
def get_paid_orders():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Query joins all relevant tables to get order, order items, and food components
    query = """
    SELECT 
        o.intOrderID,
        oi.intOrderItemID,
        oi.strOrderITemName AS order_item_name,
        f.intFoodID,
        f.strFoodName AS food_name
    FROM Orders o
    JOIN OrderItemsOrders oio ON o.intOrderID = oio.intOrderID
    JOIN OrderItems oi ON oio.intOrderItemID = oi.intOrderItemID
    LEFT JOIN OrderItemsFoods oif ON oi.intOrderItemID = oif.intOrderItemID
    LEFT JOIN Foods f ON oif.intFoodID = f.intFoodID
    WHERE o.strStatus = 'Paid'
    ORDER BY o.intOrderID, oi.intOrderItemID, f.strFoodName
    """
    
    cursor.execute(query)
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    
    # Organize data into nested structure: orders -> order items -> foods
    orders = {}
    for row in rows:
        order_id = row['intOrderID']
        item_id = row['intOrderItemID']
        item_name = row['order_item_name']
        food_name = row['food_name']
        
        if order_id not in orders:
            orders[order_id] = {
                'order_id': order_id,
                'items': {}
            }
        
        if item_id not in orders[order_id]['items']:
            orders[order_id]['items'][item_id] = {
                'item_id': item_id,
                'item_name': item_name,
                'foods': []
            }
        
        # Add food name if present (could be null if no foods linked)
        if food_name and food_name not in orders[order_id]['items'][item_id]['foods']:
            orders[order_id]['items'][item_id]['foods'].append(food_name)
    
    # Convert to list and simplify items from dict to list
    result = []
    for order in orders.values():
        items_list = []
        for item in order['items'].values():
            items_list.append({
                'item_id': item['item_id'],
                'item_name': item['item_name'],
                'foods': item['foods']
            })
        result.append({
            'order_id': order['order_id'],
            'items': items_list
        })
    
    return jsonify(result)



@app.route('/api/complete-order', methods=['POST'])
def complete_order():
    data = request.get_json()
    order_id = data.get('orderId')
    print("Received JSON:", data)
    print("Received order_id:", order_id)

    if not order_id:
        return jsonify({'error': 'Missing order ID'}), 400
    
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE Orders SET strStatus = 'Completed' WHERE intOrderID = %s", (order_id,))
    conn.commit()

    return jsonify({'message': f'Order {order_id} marked as completed'}), 200



if __name__ == '__main__':
    app.run(debug=True)