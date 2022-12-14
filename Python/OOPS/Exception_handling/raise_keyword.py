
class CreditCard:
    def __init__(self, card_no, balance):
        self.card_no = card_no
        self.balance = balance

"""
    Vinay_card_details : {
        1001 : 2500,
        2002 : 3000
    }
"""

class Customer:
    def __init__(self, cards):
        self.cards = cards 

    def purchase_items(self, card_no, price):
        if price < 0 : 
            raise Exception("The price is printed incorrectly")
        if card_no not in self.cards:
            raise Exception("The given card details is not Valid")
        if price > self.cards[card_no].balance : 
            raise Exception("The balance is insufficient to purchase the items")

card1 = CreditCard(1001, 2500)
card2 = CreditCard(2002, 3000)

cards = {
    card1.card_no : card1,
    card2.card_no : card2
}

# Aggregstion : "has-A" relationship
customer = Customer(cards)

while(True):
    card_no = int(input("Enter the Card no : "))
    try:
        customer.purchase_items(card_no, 3000)
        print("The transaction has been done Successfully")
        break
    except Exception as e:
        print(e)
        # print("Some error has been occured")





