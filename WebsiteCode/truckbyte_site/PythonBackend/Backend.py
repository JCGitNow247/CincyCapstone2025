from flask import Flask, jsonify
import mariadb

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables access from file:// and any other origins

@app.route('/get-menu')
def get_menu():
    try:
        conn = mariadb.connect(
            user="root",
            password="password",  # 👈 replace with your actual root password
            host="localhost",
            port=3306,
            database="dbtruckbytes"
        )
    except mariadb.Error as e:
        return jsonify({"error": str(e)})
    
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

if __name__ == '__main__':
    app.run(debug=True)