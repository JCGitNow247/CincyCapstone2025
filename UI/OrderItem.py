class OrderItem:

    def __init__(self):
        self.m_intMenuItemID = 0
        self.m_strMenuItemName = ""
        self.m_aFoodItems = []

    

    def set_id(self, intMenuItemID):
        self.m_intMenuItemID = intMenuItemID

    def get_id(self):
        return self.m_intMenuItemID
    


    def set_name(self, strMenuItemName):
        self.m_strMenuItemName = strMenuItemName

    def get_name(self):
        return self.m_strMenuItemName
    


    def add_food_item(self, intFoodID, strFoodName):
        self.m_aFoodItems.append({

            'id': intFoodID,
            'name': strFoodName
        })