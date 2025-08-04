class OrderItem:

    def __init__(self):
        self.m_intMenuItemID = 0
        self.m_strMenuItemName = ""
        self.m_aFoodItems = []
        self.m_dblPrice = 0
        self.m_description = ""
    

    def set_id(self, intMenuItemID):
        self.m_intMenuItemID = intMenuItemID

    def get_id(self):
        return self.m_intMenuItemID
    

    def set_name(self, strMenuItemName):
        self.m_strMenuItemName = strMenuItemName

    def get_name(self):
        return self.m_strMenuItemName
    

    def set_price(self, dblPrice):
        self.m_dblPrice = dblPrice

    def get_price(self):
        return self.m_dblPrice
    

    def set_description(self, description):
        self.m_description = description

    def get_description(self):
        return self.m_description
    


    def add_food_item(self, intFoodID, strFoodName):
        self.m_aFoodItems.append({

            'id': intFoodID,
            'name': strFoodName
        })

    def get_food_items(self):
        return self.m_aFoodItems