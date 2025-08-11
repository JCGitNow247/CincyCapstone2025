from flask import Flask, request, jsonify
import sys, os, mariadb, datetime, random, json
from flask_cors import CORS

# Add parent directory to path so we can import UI.DatabaseUtility
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from UI import DatabaseUtility as DB

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
            #host='192.168.1.236',      # Use this to connect to the pi's DB
            user='truckbytesdev',
            password='tb001',
            port=3306,
            database='dbTruckBytes'
        )
        return conn
    except mariadb.Error as e:
        return jsonify({"error": str(e)})

# --- NEW: Serve config.json so frontend can fetch it over HTTP ---
@app.route('/config')
def get_config():
    try:
        here = os.path.dirname(__file__)
        candidates = [
            os.path.join(here, '..', '..', '..', 'config.json'),  # repo root
            os.path.join(here, '..', 'config.json'),              # truckbyte_site/
            os.path.join(here, 'config.json'),                    # PythonBackend/
        ]
        for p in map(os.path.abspath, candidates):
            if os.path.exists(p):
                with open(p, 'r', encoding='utf-8') as f:
                    return jsonify(json.load(f))
        return jsonify({"error": f"config.json not found in: {candidates}"}), 500
    except Exception as e:
        return jsonify({"error": f"Unable to read config.json: {e}"}), 500


# Gets a list of all menu items
@app.route('/get-menu')
def get_menu():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT MenuItemID, MenuItemName, MenuItemDescription, MenuItemPrice FROM VMenuItems")
    rows = cursor.fetchall()

    items = []
    for row in rows:
        items.append({
            'id': row["MenuItemID"],
            'name': row["MenuItemName"],
            'description': row["MenuItemDescription"] if row["MenuItemDescription"] is not None else '',
            'price': float(row["MenuItemPrice"])
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
    cursor = conn.cursor(dictionary=True)

    # Get submenu ID from menu item name
    cursor.execute("""
        SELECT intSubMenuID
        FROM MenuItems
        WHERE strMenuItemName = %s
    """, (item_name,))
    result = cursor.fetchone()

    if not result or not result["intSubMenuID"]:
        conn.close()
        return jsonify([])

    submenu_id = result["intSubMenuID"]

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

    modifiers = [{"name": row["strFoodName"], "price": float(row["dblSellPrice"])} for row in rows]
    return jsonify(modifiers)

# Returns a list of available trucks
@app.route('/get-trucks')
def get_trucks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT intTruckNumber, strTruckName FROM Trucks")
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
    cursor.execute("SELECT strFoodName FROM Foods WHERE intFoodTypeID = 3")  # fixed case
    drinks = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(drinks)

# Handles employee login by matching last name and password
@app.route('/login-employee', methods=['POST'])
def login_employee():
    data = request.get_json()
    LastName = data['LastName'].strip()
    password = data['password'].strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        SELECT e.intEmployeeID, et.strEmployeeType
        FROM Employees e
        JOIN EmployeeTypes et ON e.intEmployeeTypeID = et.intEmployeeTypeID
        WHERE e.strLastName = %s AND e.strPassword = %s
    """, (LastName, password))

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
    customer_id = data.get("customerID") or None
    free_drink = data.get("freeDrink")
    truck_id = 1

    conn = get_connection()
    cursor = conn.cursor()

    # STEP 1: sale
    cursor.execute("""
        INSERT INTO Sales (dblSaleAmount, dtmDate, intSalesPaymentTypeID)
        VALUES (%s, NOW(), %s)
    """, (total, 1))
    sale_id = cursor.lastrowid

    # STEP 2: order
    cursor.execute("""
        INSERT INTO Orders (intTruckID, intSaleID, intCustomerID, strStatus)
        VALUES (%s, %s, %s, 'Paid')
    """, (truck_id, sale_id, customer_id))
    order_id = cursor.lastrowid

    # STEP 3: items
    for item in items:
        item_name = item.get('name', 'Unnamed Item')
        modifiers = item.get("modifiers", [])
        cursor.execute("INSERT INTO OrderItems (strOrderItemName, intAmount) VALUES (%s, %s)", (item_name, 1))
        order_item_id = cursor.lastrowid
        cursor.execute("INSERT INTO OrderItemsOrders (intOrderID, intOrderItemID) VALUES (%s, %s)", (order_id, order_item_id))
        for mod in modifiers:
            cursor.execute("SELECT intFoodID FROM Foods WHERE strFoodName = %s", (mod,))
            r = cursor.fetchone()
            if r:
                cursor.execute("INSERT INTO OrderItemsFoods (intOrderItemID, intFoodID) VALUES (%s, %s)", (order_item_id, r[0]))

    # >>> NEW: persist free drink as $0 line item
    if free_drink:
        cursor.execute("INSERT INTO OrderItems (strOrderItemName, intAmount) VALUES (%s, %s)", ("Free Drink", 1))
        free_item_id = cursor.lastrowid
        cursor.execute("INSERT INTO OrderItemsOrders (intOrderID, intOrderItemID) VALUES (%s, %s)", (order_id, free_item_id))
        cursor.execute("SELECT intFoodID FROM Foods WHERE strFoodName = %s", (free_drink,))
        r = cursor.fetchone()
        if r:
            cursor.execute("INSERT INTO OrderItemsFoods (intOrderItemID, intFoodID) VALUES (%s, %s)", (free_item_id, r[0]))
    # <<<

    # STEP 4: KDS cache (display only)
    description_lines = [item.get("html", "") for item in items]
    if free_drink:
        description_lines.append(f"<em>Free Drink: {free_drink}</em>")
    active_orders_cache.append({
        "id": order_id,
        "time": datetime.datetime.now().isoformat(),
        "description": "<br>".join(description_lines)
    })

    conn.commit()
    conn.close()
    return jsonify({"success": True, "id": order_id})

# Provides summary analytics including total sales, sales by day, and payroll info
@app.route('/get-analytics-summary')
def get_analytics_summary():
    conn = get_connection(); 
    cursor = conn.cursor(dictionary=True)

    # Totals & average
    cursor.execute("""
        SELECT SUM(dblSaleAmount) AS total_sales,
               AVG(dblSaleAmount) AS average_sale,
               COUNT(*) AS sale_count
        FROM Sales
    """)
    totals = cursor.fetchone() or {}
    total_sales = float(totals.get('total_sales') or 0)
    average_sale = float(totals.get('average_sale') or 0)

    # Sales this week & same week last year
    cursor.execute("""
        SELECT SUM(dblSaleAmount) AS amt
        FROM Sales
        WHERE YEARWEEK(dtmDate, 3) = YEARWEEK(CURDATE(), 3)
    """)
    sales_this_week = float((cursor.fetchone() or {}).get('amt') or 0)

    cursor.execute("""
        SELECT SUM(dblSaleAmount) AS amt
        FROM Sales
        WHERE YEARWEEK(dtmDate, 3) = YEARWEEK(DATE_SUB(CURDATE(), INTERVAL 1 YEAR), 3)
    """)
    same_week_last_year = float((cursor.fetchone() or {}).get('amt') or 0)

    # Last 7 sale dates that have sales
    cursor.execute("""
    SELECT DATE_FORMAT(DATE(dtmDate),'%Y-%m-%d') AS sale_date,
            SUM(dblSaleAmount) AS amount
    FROM Sales
    GROUP BY DATE(dtmDate)
    ORDER BY DATE(dtmDate) DESC
    LIMIT 7
    """)
    rows = cursor.fetchall()
    sales_by_day = list(([
    {"sale_date": r["sale_date"], "amount": float(r["amount"] or 0)}
    for r in rows
    ]))


    # Payment breakdown
    cursor.execute("""
        SELECT spt.strSalesPaymentType AS type,
               SUM(s.dblSaleAmount) AS total
        FROM Sales s
        JOIN SalesPaymentTypes spt ON s.intSalesPaymentTypeID = spt.intSalesPaymentTypeID
        GROUP BY spt.strSalesPaymentType
    """)
    payment_breakdown = cursor.fetchall()

    # Total hours worked
    cursor.execute("""SELECT SUM(TIMESTAMPDIFF(HOUR, dtmShiftStart, dtmShiftEnd)) AS total_hours
                   FROM EmployeesShifts""")
    total_hours = (cursor.fetchone() or {}).get('total_hours') or 0

    # Employee payroll
    cursor.execute("""
        SELECT CONCAT(e.strFirstName, ' ', e.strLastName) AS name,
               e.dblHourlyRate AS rate,
               SUM(TIMESTAMPDIFF(HOUR, es.dtmShiftStart, es.dtmShiftEnd)) AS hours
        FROM EmployeesShifts es
        JOIN Employees e ON es.intEmployeeID = e.intEmployeeID
        GROUP BY e.intEmployeeID
        ORDER BY name
    """)
    payroll = cursor.fetchall()

    # Repeat customers (customers with >1 order)
    cursor.execute("""
        SELECT COUNT(*) AS repeat_count
        FROM (
          SELECT o.intCustomerID
          FROM Orders o
          WHERE o.intCustomerID IS NOT NULL
          GROUP BY o.intCustomerID
          HAVING COUNT(*) > 1
        ) x
    """)
    repeat_customers = int((cursor.fetchone() or {}).get('repeat_count') or 0)

    conn.close()
    return jsonify({
        "total_sales": total_sales,
        "average_sale": average_sale,
        "sales_this_week": sales_this_week,
        "same_week_last_year": same_week_last_year,
        "sales_by_day": sales_by_day,          # [{sale_date, amount}]
        "payment_breakdown": payment_breakdown, # [{type, total}]
        "total_hours": total_hours,
        "payroll": payroll,                     # [{name, rate, hours}]
        "repeat_customers": repeat_customers
    })


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



@app.route('/api/paid-orders')
def get_paid_orders():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
    SELECT
        o.intOrderID,
        oi.intOrderItemID,
        oi.strOrderItemName AS order_item_name,
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

    orders = {}
    for row in rows:
        order_id = row['intOrderID']
        item_id = row['intOrderItemID']
        item_name = row['order_item_name']
        food_name = row['food_name']

        if order_id not in orders:
            orders[order_id] = {
                'order_id': order_id,
                'items': []
            }

        existing_item = next((i for i in orders[order_id]['items'] if i['item_id'] == item_id), None)

        if existing_item:
            if food_name and food_name not in existing_item['foods']:
                existing_item['foods'].append(food_name)
        else:
            orders[order_id]['items'].append({
                'item_id': item_id,
                'item_name': item_name,
                'foods': [food_name] if food_name else []
            })

    result = []
    for order in orders.values():
        result.append({
            'order_id': order['order_id'],
            'items': order['items']
        })

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
