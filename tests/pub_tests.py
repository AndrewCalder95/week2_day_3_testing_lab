import unittest
from src.pub import Pub
from src.drinks import Drink

class TestPub(unittest.TestCase):
    def setUp(self):
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