from src.drinks import Drink
from src.customer import Customer

class Pub:
    def __init__(self, name, till, drink_list):
        self.pub_name = name 
        self.pub_till = till
        self.drinks = drink_list

    
    def purchase_drink(self, customer, drink):
        self.pub_till += drink.price
        customer.wallet -= drink.price

   