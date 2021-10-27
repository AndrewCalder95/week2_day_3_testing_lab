import unittest
from src.pub import Pub

class TestPub(unittest.TestCase):
    def setUp(self):
        self.pub = Pub("The Sparkle Horse", 100)
        
    def test_pub_name(self):
        self.assertEqual("The Sparkle Horse", self.pub.pub_name)