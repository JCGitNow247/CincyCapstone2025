from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app) # Allows your frontend to access this backend from a different origin (like file://)

@app.route('/get-menu')
def get_menu():
    # This will communicate with SQL to get the data and send it to the Javascript code to dynamically create the menu cards.

    #SQL Query

    menu_data = [
        {
            "name": "Bronx Bomber",
            "description": "A delicious Pizza with red sauce, mozzarella, pepperoni, onions, and more."
        },
        {
            "name": "Veggie Delight",
            "description": "Topped with mushrooms, tomatoes, green olives, and spinach."
        },
        {
            "name": "Hawaiian Pizza",
            "description": "Topped with our signature red sauce, mozzerella, canadian bacon and pineapples"
        }
    ]
    return jsonify(menu_data)
if __name__ == '__main__':
    app.run(debug=True)