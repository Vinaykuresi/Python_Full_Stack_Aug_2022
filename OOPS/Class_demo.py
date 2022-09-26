# Class
class Mobile:
                # parameters
    # Constructor
    def __init__(self, brand, price):
        # attributes/properties
        print("Id of self in Contructor : ", self)
        self.brand = brand
        self.price = price 

    # behavior/opearations
    def display(self):
        print("The Brand is : ", self.brand, " The Price : ", self.price)

    def update_price(self, price):
        self.price = price

# Object Reference
mob1 = Mobile("Apple",  100000)
mob2 = Mobile("Samsing", 34000)

# printing the properties
# print(mob1.brand, " : ", mob1.price)

# print(mob2.brand, " : ", mob2.price)

# invoking the behavior
mob1.display()
mob1.update_price(80000)
mob1.display()