

#customer base class
class Customer:
    def __init__(self):
        self.balance = 0
        self.cart  = []
    def add_balance(self):
        money = int(input())
        self.balance += money

    def view_money (self):
        return self.balance

    def view_past_order(self):
        return self.cart

    def create_order(self):

        

