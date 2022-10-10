
# class Mobile(Product):

class Mobile:
    # Constructor
    def __init__(self, brand, price):
        # attributes/properties
        print("Id of self in Contructor : ", id(self))
        self.brand = brand
        self.price = price 
        self.camera = "35px"
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

# Inheritance
class FeaturePhone(Mobile) : 
    # behavior/opearations
    def display(self):
        print("The Feature Phone brand is : ", self.brand, " The Price : ", self.price)
        # super
        super().display()
# Inheritance
# Multiple Inheritance
class SmartPhone(Mobile) : 

    def __init__(self, brand, price, version):
        super().__init__(brand, price)
        self.brand = brand
        self.price = price 
        self.version = version 
    # behavior/opearations
    def display(self):
        print("The SmartPhone brand is : ", self.brand, " The Price : ", self.price, " The version is : ", self.version) 


smartPhone = SmartPhone("Samsung", 40000, "A12")
smartPhone.display()

print(smartPhone.camera)


# FeaturePhone("Apple", 100000).display()

