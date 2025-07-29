from flask import Flask, request, jsonify
import mariadb

from flask_cors import CORS

import random

app = Flask(__name__)
CORS(app)  # This enables access from file:// and any other origins

# Path to here to start python backend servers.
# cd WebsiteCode\truckbyte_site\PythonBackend
# run python Backend.py to start the script.

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

@app.route('/get-trucks')
def get_trucks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT intTruckNumber, strTruckName FROM Trucks");
    rows = cursor.fetchall()
    trucks = [{"id": row[0], "name": row[1]} for row in rows]
    return jsonify(trucks)

@app.route('/check-customer', methods=['POST'])
def check_customer():
    data = request.get_json()

    first = data['firstName'].strip()
    last = data['lastName'].strip()
    phone = data['phone'].strip()
    email = data['email'].strip()

    print(f"Checking: {first} {last}, {phone}, {email}")  # For debugging

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT intCustomerID
        FROM Customers
        WHERE strFirstName = %s AND strLastName = %s AND strPhoneNumber = %s AND strEmail = %s
    """, (first, last, phone, email))

    result = cursor.fetchone()
    conn.close()

    return jsonify({ "exists": result is not None })



@app.route('/register-customer', methods=['POST'])
def register_customer():
    data = request.get_json()

    first = data['firstName'].strip()
    last = data['lastName'].strip()
    phone = data['phone'].strip()
    email = data['email'].strip()
    username = data['username'].strip()
    password = data['password'].strip()

    conn = get_connection()
    cursor = conn.cursor()

    # Insert new customer
    cursor.execute("""
        INSERT INTO Customers (strFirstName, strLastName, strUserName, strEmail, strPassword, strPhoneNumber)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (first, last, username, email, password, phone))

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

@app.route('/login-customer', methods=['POST'])
def login_customer():
    data = request.get_json()
    username = data['username'].strip()
    password = data['password'].strip()

    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    # Check user exists
    cursor.execute("""
        SELECT c.intCustomerID, r.strLoyaltyRewardType
        FROM Customers c
        LEFT JOIN LoyaltyMembers lm ON c.intCustomerID = lm.intCustomerID
        LEFT JOIN LoyaltyRewards r ON lm.intLoyaltyRewardID = r.intLoyaltyRewardID
        WHERE c.strUserName = %s AND c.strPassword = %s
    """, (username, password))

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

@app.route('/get-drinks', methods=['GET'])
def get_drinks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT strFoodName FROM foods WHERE intFoodTypeID = 3")
    drinks = [row[0] for row in cursor.fetchall()]
    cursor.close()
    conn.close()
    return jsonify(drinks)



if __name__ == '__main__':
    app.run(debug=True)