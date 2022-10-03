# Class
class Mobile:
    discount = 50
    __discount = 60
                # parameters
    # Constructor
    def __init__(self, brand, price):
        # attributes/properties
        print("Id of self in Contructor : ", id(self))
        self.brand = brand
        self.price = price 
        # private variable
        self.__location = "Tirupati"

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(value):
        Mobile.__discount = value

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

# accesing the static or class level variable
print(mob1.discount)
print(Mobile.discount)

Mobile.discount = 30

print(mob2.discount)
