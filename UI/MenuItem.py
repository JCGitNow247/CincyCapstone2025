class MenuItem:

    def __init__(self):
        self.m_name = ""
        self.m_image = None
        self.m_typeID = 0
        self.m_description = ""
        self.m_price = 0
        self.m_sub_menuID = 0
        self.m_taxable = ""

    

    def set_name(self, name):
        self.m_name = name

    def get_name(self):
        return self.m_name
    


    def set_image(self, image):
        self.m_image = image

    def get_image(self):
        return self.m_image
    


    def set_typeID(self, typeID):
        self.m_typeID = typeID

    def get_typeID(self):
        return self.m_typeID
    


    def set_description(self, description):
        self.m_description = description

    def get_description(self):
        return self.m_description
    


    def set_price(self, price):
        self.m_price = price

    def get_price(self):
        return self.m_price
    


    def set_sub_menuID(self, sub_menuID):
        self.m_sub_menuID = sub_menuID

    def get_sub_menuID(self):
        return self.m_sub_menuID
    

    def set_taxable(self, taxable):
        self.m_taxable = taxable

    def get_taxable(self):
        return self.m_taxable