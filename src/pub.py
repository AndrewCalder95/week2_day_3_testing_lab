class Pub:
    def __init__(self, name, till):
        self.pub_name = name 
        self.pub_till = till
        self.drink = []

    def return_pub_name(self, name):
        return name