from src.drinks import Drink

class Pub:
    def __init__(self, name, till, drink_list):
        self.pub_name = name 
        self.pub_till = till
        self.drinks = drink_list

    
    # def add_drink(self, drink):
    #     for drink in self.drinks:
    #         self.drinks.append(drink)

   