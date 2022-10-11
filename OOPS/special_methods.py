
class Mobile:
    # Constructor
    def __init__(self, brand, price):
        # attributes/properties
        # print("Id of self in Contructor : ", id(self))
        self.brand = brand
        self.price = price 
        # private variable
        self.__location = "Tirupati"

    def __str__(self):
        return self.brand+" "+str(self.price)

    """
        __add__
        __sub__
        __mul__
    """

    def __add__(self, other):
        return self.price+other.price

    # behavior/opearations
    def display(self):
        print("The Brand is : ", self.brand, " The Price : ", self.price)

    def update_price(self, price):
        self.price = price

    # enapsualation
    # setter
    def set_location(self, location):
        self.__location = location
    
    # getter
    def get_location(self):
        return self.__location


andriod = Mobile("Samsung", 35000)
apple = Mobile("Apple", 100000)

print(andriod+apple)