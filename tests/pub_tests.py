import unittest
from src.pub import Pub
from src.drinks import Drink
from src.customer import Customer

class TestPub(unittest.TestCase):
    def setUp(self):
        self.customer1 = Customer("James", 25)
        self.customer2 = Customer("Sarah", 50)
        self.drinks_1 = Drink("Vodka", 4)
        self.drinks_2 = Drink("Beer", 5)
        self.drinks_3 = Drink("Wine", 7)

        drink_list = [self.drinks_1, self.drinks_2, self.drinks_3]
        
        self.pub = Pub("The Sparkle Horse", 100, drink_list)
        
    def test_pub_name(self):
        self.assertEqual("The Sparkle Horse", self.pub.pub_name)
    
    def test_pub_till(self):
        self.assertEqual(100, self.pub.pub_till)
    
    def test_pub_drinks(self):
        self.assertEqual(3, len(self.pub.drinks))

    def test_customer_name(self):
        self.assertEqual("James", self.customer1.name)

    def test_customer_wallet(self):
        self.assertEqual(50, self.customer2.wallet)

    def test_wallet_decrease(self):
        self.pub.purchase_drink(self.customer1, self.drinks_1)
        self.assertEqual(21, self.customer1.wallet)
    
    def test_till_increase(self):
        self.pub.purchase_drink(self.customer1, self.drinks_1)
        self.assertEqual(104, self.pub.pub_till)