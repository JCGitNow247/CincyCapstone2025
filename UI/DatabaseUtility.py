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



def get_sub_menu_items(ItemID):
    """
    <b>Name:</b> get_sub_menu_items<br>
    <b>Abstract:</b> Returns a list of sub menu items by name from menu item id<br>
    <b>Param</b>: <i>ItemID</i> - input for menu item id<br>
    <b>Return:</b> <i>rows</i> - sub menu items list
    """

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute('SELECT SubMenuItem FROM VSubMenuItems WHERE MenuItem = ?', (ItemID,))
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