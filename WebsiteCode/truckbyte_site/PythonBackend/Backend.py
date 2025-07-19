from flask import Flask, request, jsonify
import mariadb

from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # This enables access from file:// and any other origins

def get_connection():
    try:
        conn = mariadb.connect(
            user="root",
            password="password",  # 👈 replace with your actual root password
            host="localhost",
            port=3306,
            database="dbtruckbytes"
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

if __name__ == '__main__':
    app.run(debug=True)