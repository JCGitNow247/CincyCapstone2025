from flask import Flask, jsonify
import pyodbc

from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables access from file:// and any other origins

@app.route('/get-menu')
def get_menu():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=CWBR001;'
        'DATABASE=dbTruckBytes;'
        'UID=sa;'
        'PWD='
    )
    cursor = conn.cursor()
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

    return jsonify(items)

if __name__ == '__main__':
    app.run(debug=True)