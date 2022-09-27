# Class
class Mobile:
                # parameters
    # Constructor
    def __init__(self, brand, price):
        # attributes/properties
        print("Id of self in Contructor : ", id(self))
        self.brand = brand
        self.price = price 
        # private variable
        self.__location = "Tirupati"

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


# Object Reference
mob1 = Mobile("Apple",  100000)
mob2 = Mobile("Samsing", 34000)

print(mob1.get_location())
mob1.set_location("Bangalore")
print(mob1.get_location())
