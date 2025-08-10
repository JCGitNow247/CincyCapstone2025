import mariadb

def get_connection():
    """
    <b>Name:</b> get_connection<br>
    <b>Abstract:</b> Returns a mariadb connection to dbTruckBytes<br>
    <b>Return:</b> <i>conn</i> - database connection object
    """
    try:
        conn = mariadb.connect(

            host='localhost',
            user='truckbytesdev',
            password='tb001',
            database='dbTruckBytes'
        )
    except mariadb.Error as e:
        print("database error: " + str(e))

    return conn

def fetch_one(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    row = cursor.fetchone()
    conn.close()
    return row

def fetch_all(query, params=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(query, params or ())
    rows = cursor.fetchall()
    conn.close()
    return rows

def insert_menu_item(menu_item):
    
    conn = get_connection()
    cursor = conn.cursor()

    sql = f"""
        CALL dbTruckBytes.uspAddMenuItem('{menu_item.get_name()}', {menu_item.get_image()}, {menu_item.get_typeID()}, '{menu_item.get_description()}', {menu_item.get_price()}, {menu_item.get_sub_menuID()}, '{menu_item.get_taxable()}');
    """
    cursor.execute(sql)

    conn.commit()
    cursor.close()
    conn.close()


def get_menu_items():
    """
    <b>Name:</b> get_menu_items<br>
    <b>Abstract:</b> Returns a dictionary of menu items by id and name<br>
    <b>Return:</b> <i>dictMenuItems</i> - dictionary of menu items
    """

    dictMenuItems = {}
    intMenuItemIndex = 0

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT MenuItemID, MenuItemName FROM VMenuItems ORDER BY MenuType')

    dictMenuItemsRows = cursor.fetchall()

    for row in dictMenuItemsRows:

        MenuItemID = row[0]
        MenuItemName = row[1]

        dictMenuItems[intMenuItemIndex] = {

            "id": MenuItemID,
            "name": MenuItemName
        }

        intMenuItemIndex += 1

    return dictMenuItems



def get_menu_item_name(ItemID):
    """
    <b>Name:</b> get_menu_item_name<br>
    <b>Abstract:</b> Get the name of a menu item from an id<br>
    <b>Param:</b> <i>ItemID</i> - input for menu item id<br>
    <b>Return:</b> <i>menu_item_name</i> - name of menu item
    """
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT MenuItemName FROM VMenuItems WHERE MenuItemID = ?', (ItemID,))

    row = cursor.fetchone()

    menu_item_name = row[0]

    return menu_item_name



def get_menu_item_price(ItemID):
    """
    <b>Name:</b> get_menu_item_price<br>
    <b>Abstract:</b> Get the price of a menu item from an id<br>
    <b>Param:</b> <i>ItemID</i> - input for menu item id<br>
    <b>Return:</b> <i>price</i> - price of menu item
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT dblPrice FROM MenuItems WHERE intMenuItemID = ?', (ItemID,))

    row = cursor.fetchone()

    price = row[0]

    return price



def get_menu_item_description(ItemID):
    """
    <b>Name:</b> get_menu_item_description<br>
    <b>Abstract:</b> Get the description of a menu item from an id<br>
    <b>Param:</b> <i>ItemID</i> - input for menu item id<br>
    <b>Return:</b> <i>description</i> - description of menu item
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT strDescription FROM MenuItems WHERE intMenuItemID = ?', (ItemID,))

    row = cursor.fetchone()

    menu_item_description = row[0]

    return menu_item_description


####################################################
####################################################
def get_average_sale():
    return fetch_one("SELECT AVG(dblSaleAmount) FROM Sales")[0]

def get_top_selling_items(limit=5):
    return fetch_all("""
        SELECT strOrderItemName, SUM(intAmount) as qty
        FROM OrderItems
        GROUP BY strOrderItemName
        ORDER BY qty DESC
        LIMIT %s
    """, (limit,))

def get_repeat_customer_count():
    return fetch_one("""
        SELECT COUNT(DISTINCT intCustomerID)
        FROM Orders
        WHERE intCustomerID IN (
            SELECT intCustomerID
            FROM Orders
            GROUP BY intCustomerID
            HAVING COUNT(*) > 1
        )
    """)[0]

def get_sales_this_week():
    query = """
        SELECT COALESCE(SUM(dblSaleAmount), 0)
        FROM Sales
        WHERE YEARWEEK(dtmDate, 1) = YEARWEEK(CURDATE(), 1)
    """
    row = fetch_one(query)
    return row[0] if row and row[0] is not None else 0.0


def get_sales_same_week_last_year():
    query = """
        SELECT COALESCE(SUM(dblSaleAmount), 0)
        FROM Sales
        WHERE YEARWEEK(dtmDate, 1) = YEARWEEK(DATE_SUB(CURDATE(), INTERVAL 1 YEAR), 1)
    """
    row = fetch_one(query)
    return row[0] if row and row[0] is not None else 0.0


####################################################
####################################################


def get_sub_menu_items(ItemID):
    """
    <b>Name:</b> get_sub_menu_items<br>
    <b>Abstract:</b> Returns a list of sub menu items by name from menu item id<br>
    <b>Param</b>: <i>ItemID</i> - input for menu item id<br>
    <b>Return:</b> <i>rows</i> - sub menu items list
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT SubMenuItemID, SubMenuItem, PortionPrice FROM VSubMenuItems WHERE MenuItem = ?', (ItemID,))
    rows = cursor.fetchall()

    return rows



def get_sub_menu_name(ItemID):
    """
    <b>Name:</b> get_sub_menu_name<br>
    <b>Abstract:</b> Returns the sub menu name associated to the menu item by menu item id<br>
    <b>Param:</b> <i>ItemID</i> - input for menu item id<br>
    <b>Return:</b> <i>sub_menu_name</i> - name of associated sub menu
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT SubMenu FROM VSubMenuName WHERE MenuItem = ?', (ItemID,))

    row = cursor.fetchone()

    sub_menu_name = row[0]

    return sub_menu_name



def get_menu_item_type(ItemID):
    """
    <b>Name:</b> get_menu_item_type<br>
    <b>Abstract:</b> Returns the menu name associated to the menu item by menu item id<br>
    <b>Param:</b> <i>ItemID</i> - input for menu item id<br>
    <b>Return:</b> <i>menu_item_type</i> - name of associated sub menu
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT MenuItemType FROM VMenuItemType WHERE MenuItem = ?', (ItemID,))

    row = cursor.fetchone()

    menu_item_type = row[0]

    return menu_item_type



def get_menus():
    """
    <b>Name:</b> get_menus<br>
    <b>Abstract:</b> Returns a list of menu types of id and name<br>
    <b>Return:</b> <i>Menus</i> - list of menu types
    """

    Menus = {}
    intMenuIndex = 0

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT MenuTypeID, MenuType FROM VMenus')

    rows = cursor.fetchall()

    for row in rows:

        MenuTypeID = row[0]
        MenuType = row[1]

        Menus[intMenuIndex] = {

            "id": MenuTypeID,
            "name": MenuType
        }

        intMenuIndex += 1


    return Menus



def get_menu_id(menu_name):
    """
    <b>Name:</b> get_menu_id<br>
    <b>Abstract:</b> Returns the menu type id from a menu name<br>
    <b>Param:</b> <i>menu_name</i> - input for menu type name<br>
    <b>Return:</b> <i>Menus</i> - list of menu types
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT MenuTypeID FROM VMenus WHERE MenuType = ?', (menu_name,))

    row = cursor.fetchone()

    if row is not None:
        menu_id = row[0]
    else:
        menu_id = None

    return menu_id



def get_sub_menus():
    """
    <b>Name:</b> get_sub_menus<br>
    <b>Abstract:</b> Returns a list of SubMenus of id and name<br>
    <b>Return:</b> <i>SubMenus</i> - list of SubMenus types
    """

    SubMenus = {}
    intSubMenuIndex = 0

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT SubMenuID, SubMenuName FROM VSubMenus')

    rows = cursor.fetchall()

    for row in rows:
        
        SubMenuID = row[0]
        SubMenuName = row[1]

        SubMenus[intSubMenuIndex] = {

            "id": SubMenuID,
            "name": SubMenuName
        }

        intSubMenuIndex += 1

    return SubMenus



def insert_food(name, amount, purchase_price, sell_price, food_type_id, sub_menu_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        INSERT INTO Foods (strFoodName, dblAmount, dblPurchasePrice, dblSellPrice, intFoodTypeID)
        VALUES (%s, %s, %s, %s, %s)
    """
    cursor.execute(sql, (name, amount, purchase_price, sell_price, food_type_id))
    conn.commit()

    cursor.execute("SELECT LAST_INSERT_ID()")
    food_id = cursor.fetchone()[0]

    if sub_menu_id is not None:

        sql = """
            INSERT INTO SubMenusFoods (intSubMenuID, intFoodID)
            VALUES (%s, %s)
        """

        cursor.execute(sql, (sub_menu_id, food_id))
        conn.commit()

    cursor.close()
    conn.close()
    return food_id



def get_food_by_id(food_id):
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        SELECT intFoodID, strFoodName, dblAmount, dblPurchasePrice, dblSellPrice, intFoodTypeID
        FROM Foods WHERE intFoodID = %s
    """
    cursor.execute(sql, (food_id,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()

    if row:
        return {
            "id": row[0],
            "name": row[1],
            "amount": row[2],
            "purchase": row[3],
            "sell": row[4],
            "type_id": row[5]
        }
    return None



def get_food_types():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT intFoodTypeID, strFoodType FROM FoodTypes")
    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return {row[0]: row[1] for row in rows}



def get_all_foods():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT intFoodID, strFoodName, dblAmount, dblPurchasePrice, dblSellPrice, intFoodTypeID
        FROM Foods
    """)

    rows = cursor.fetchall()
    cursor.close()
    conn.close()

    # Return a list of dicts for each food item
    return [
        {
            "id": row[0],
            "name": row[1],
            "amount": row[2],
            "purchase": row[3],
            "sell": row[4],
            "type_id": row[5]
        }
        for row in rows
    ]



def get_food_card_sub_menu(food_id):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        f"""
        SELECT SM.strSubMenuName
        FROM   SubMenus AS SM JOIN SubMenusFoods AS SMF
        ON     SM.intSubMenuID = SMF.intSubMenuID
        JOIN   Foods AS F
        ON     F.intFoodID = SMF.intFoodID
        WHERE  F.intFoodID = {food_id}
        """
    )

    row = cursor.fetchone()

    if row != None:
        sub_menu_name = row[0]
    else:
        sub_menu_name = None

    return sub_menu_name



def get_sub_menu_id(sub_menu_name):
    
    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT SubMenuID FROM VSubMenus WHERE SubMenuName = ?', (sub_menu_name,))

    row = cursor.fetchone()

    if row is not None:
        sub_menu_id = row[0]
    else:
        sub_menu_id = None

    return sub_menu_id



def update_food_item(food_id, updated_data):
    """
    Update a food record in the Foods table.

    Parameters:
    - food_id (int): ID of the food item to update.
    - updated_data (dict): Dictionary with keys:
        "name" (str),
        "amount" (float),
        "purchase" (float),
        "sell" (float),
        "type_id" (int)
    """
    conn = get_connection()
    cursor = conn.cursor()

    sql = """
        UPDATE Foods
        SET strFoodName = %s,
            dblAmount = %s,
            dblPurchasePrice = %s,
            dblSellPrice = %s,
            intFoodTypeID = %s
        WHERE intFoodID = %s
    """

    cursor.execute(sql, (
        updated_data["name"],
        updated_data["amount"],
        updated_data["purchase"],
        updated_data["sell"],
        updated_data["type_id"],
        food_id
    ))

    conn.commit()
    cursor.close()
    conn.close()



def update_food_sub_menu(food_id, sub_menu_name):
    conn = get_connection()
    cursor = conn.cursor()

    sub_menu_id = get_sub_menu_id(sub_menu_name)

    cursor.execute("SELECT intSubMenuFoodID FROM SubMenusFoods WHERE intFoodID = ?", (food_id,))

    row = cursor.fetchone()

    if row is not None:
        if sub_menu_id is not None:
            sql = """
                UPDATE SubMenusFoods
                SET intSubMenuID = %s
                WHERE intFoodID = %s
            """

            cursor.execute(sql, (sub_menu_id, food_id))
            conn.commit()
        else:
            cursor.execute("DELETE FROM SubMenusFoods WHERE intFoodID = ?", (food_id,))
            conn.commit()
    else:

        sql = """
            INSERT INTO SubMenusFoods (intSubMenuID, intFoodID)
            VALUES (%s, %s)
        """

        cursor.execute(sql, (sub_menu_id, food_id))
        conn.commit()

    cursor.close()
    conn.close()



def delete_food_by_id(food_id):
    """
    Delete a food record from the Foods table by its ID.

    Parameters:
    - food_id (int): ID of the food item to delete.
    """
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT intSubMenuFoodID FROM SubMenusFoods WHERE intFoodID = ?", (food_id,))

    row = cursor.fetchone()

    if row is not None:
            
            cursor.execute("DELETE FROM OrderItemsFoods WHERE intFoodID = ?", (food_id,))

            cursor.execute("DELETE FROM SubMenusFoods WHERE intFoodID = ?", (food_id,))
            conn.commit()

    sql = "DELETE FROM Foods WHERE intFoodID = %s"
    cursor.execute(sql, (food_id,))

    conn.commit()
    cursor.close()
    conn.close()



def get_total_sales():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(dblSaleAmount) FROM sales")
    result = cursor.fetchone()[0]
    conn.close()
    return result or 0



def get_sales_by_day():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT DATE(dtmDate), SUM(dblSaleAmount)
        FROM sales
        GROUP BY DATE(dtmDate)
        ORDER BY DATE(dtmDate)
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows



def get_sales_by_payment_type():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT intSalesPaymentTypeID, SUM(dblSaleAmount)
        FROM sales
        GROUP BY intSalesPaymentTypeID
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows



def get_total_hours_worked():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT SUM(TIMESTAMPDIFF(HOUR, dtmShiftStart, dtmShiftEnd))
        FROM employeesshifts
    """)
    total = cursor.fetchone()[0] or 0
    conn.close()
    return total



def get_employee_payroll():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT 
            e.intEmployeeID,
            CONCAT(e.strFirstName, ' ', e.strLastName) AS full_name,
            SUM(TIMESTAMPDIFF(HOUR, es.dtmShiftStart, es.dtmShiftEnd)) AS total_hours,
            e.dblHourlyRate,
            SUM(TIMESTAMPDIFF(HOUR, es.dtmShiftStart, es.dtmShiftEnd)) * e.dblHourlyRate AS total_pay
        FROM employeesshifts es
        JOIN Employees e ON es.intEmployeeID = e.intEmployeeID
        GROUP BY e.intEmployeeID, full_name, e.dblHourlyRate
    """)
    rows = cursor.fetchall()
    conn.close()
    return rows



def get_loyalty_customer(phone, email):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"SELECT intCustomerID FROM Customers WHERE strPhoneNumber = '{phone}' AND strEmail = '{email}'")

    row = cursor.fetchone()

    if row is not None:
        customerID = row[0]
    else:
        customerID = 0

    return customerID



def create_loyalty_customer(phone, email):
    
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO Customers (strEmail, strPhoneNumber) VALUES ('{email}', '{phone}')")

    conn.commit()

    cursor.execute("SELECT LAST_INSERT_ID()")

    row = cursor.fetchone()

    customerID = row[0]

    return customerID



def build_order(OrderItemsList, SQLTotal, customerID):

    if customerID == 0:
        customerID = "NULL"

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO Sales (dblSaleAmount, dtmDate, intSalesPaymentTypeID) VALUES ({SQLTotal}, NOW(), 2)")
    conn.commit()

    cursor.execute("SELECT intSaleID FROM Sales ORDER BY intSaleID DESC LIMIT 1")

    row = cursor.fetchone()

    recent_saleID = row[0]

    cursor.execute(f"INSERT INTO Orders (intTruckID, intSaleID, intCustomerID, strStatus) VALUES (1, {recent_saleID}, {customerID}, 'Unpaid')")
    conn.commit()

    cursor.execute("SELECT intOrderID FROM Orders ORDER BY intOrderID DESC LIMIT 1")

    row = cursor.fetchone()

    recent_orderID = row[0]

    for OrderItem in OrderItemsList:

        name = OrderItem.get_name()

        cursor.execute(f"INSERT INTO OrderItems (strOrderItemName, intAmount) VALUES ('{name}', 1)")
        conn.commit()

        cursor.execute("SELECT intOrderItemID FROM OrderItems ORDER BY intOrderItemID DESC LIMIT 1")

        row = cursor.fetchone()

        recent_order_itemID = row[0]

        cursor.execute(f"INSERT INTO OrderItemsOrders (intOrderID, intOrderItemID) VALUES ({recent_orderID}, {recent_order_itemID})")
        conn.commit()

        food_items = OrderItem.get_food_items()

        if food_items is not None:
            for food in food_items:
                foodID = food["id"]

                cursor.execute(f"INSERT INTO OrderItemsFoods (intOrderItemID, intFoodID) VALUES ({recent_order_itemID}, {foodID})")
                conn.commit()

    return recent_orderID
    


def mark_recent_order_paid(orderID):

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(f"UPDATE Orders SET strStatus = 'Paid' WHERE intOrderID = {orderID}")
    conn.commit()



def insert_new_sub_menu(subMenuName):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO SubMenus (strSubMenuName) VALUES ('{subMenuName}')")
    conn.commit()
    cursor.close()
    conn.close()