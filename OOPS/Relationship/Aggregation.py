# Address
from ast import Add


class Address : 
    def  __init__(self, door, street, area, pincode):
        self.__door = door
        self.__street = street
        self.__area = area 
        self.__pincode = pincode 

    # setter method
    def updade_address(self, door, street, area, pincode):
        self.__door = door
        self.__street = street
        self.__area = area 
        self.__pincode = pincode 

    # getter method
    def view_address(self):
        return self.__door, self.__street, self.__area, self.__pincode

# Customer
class Customer : 

    def __init__(self, cust_id, name, age, phone_no, address):
        self.cust_id = cust_id
        self.name = name
        self.age = age 
        self.phone = phone_no 
        self.__address = address 

    def view_customer_address(self):
        return self.__address.view_address()


address = Address(115, "Padmavathi Street", "Mr Palli", 517502)

customer = Customer(1001, "Vinay", 27, 9154549566, address)

print(customer.view_customer_address())







    