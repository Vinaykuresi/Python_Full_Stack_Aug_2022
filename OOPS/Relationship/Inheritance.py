
class Product: 

    def review(self):
        print("Product of Electronic Device")
    # def __init__(self):
    #     gadget_type = "Electronic device"
    #     portable_type = True

    # def review(self):
    #     return [self.gadget_type, self.portable_type]

# Class
# Multilevel Inheritance
# class Mobile(Product):
class Mobile:
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

# Inheritance
class FeaturePhone(Mobile) : 
    pass
# Inheritance
# Multiple Inheritance
class SmartPhone(Mobile, Product) : 
    pass 


smartPhone = SmartPhone("Iphone", 100000)

print(smartPhone.display())

print(smartPhone.brand)

# print(smartPhone.__location)
print(smartPhone.get_location())

print(smartPhone.review())
