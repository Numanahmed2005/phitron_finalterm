from abc import ABC

#customer base class
class Customer(ABC):
    def __init__(self,admin):
        self.balance = 0
        self.cart  = []
        self.admin = admin
        #self.ahmed=Admin()
    def add_balance(self):
        money = int(input())
        self.balance += money



    def view_money (self):
        return self.balance

    def view_past_order(self):
        return self.cart

    def view_menus(self):
        self.admin.view_menu()


#tesing phase




#admin class

class Admin:
    def __init__(self):
        self.cart = []
        self.customer_account = []


    def add_menu(self):
        menu =input()

        self.cart.append(menu)

    def view_menu(self):
        return self.cart

    def remove_menu(self):
        menu = input()
        self.cart.remove(menu)

    def add_customer_account(self):
        #input example -> name email
        create_account= input()
        self.customer_account.append(create_account)


    def remove_customer_account(self):
        #input example -> name email
        remove_name_email = input()
        self.customer_account.remove(remove_name_email)

    def view_customer(self):
        return self.customer_account

    def modify_menu(self):
        #input example -> menu price
        value=input()
        self.cart.insert(0,value)

#test phase of admin class ->
#cusomers = Admin()
#cusomers.add_customer_account()
#print(cusomers.view_customer())

#cusomers.add_menu()
#cusomers.add_menu()
#print(cusomers.view_menu())

my_admin  = Admin()

Customers = Customer(my_admin)
my_admin.add_menu()
print(Customers.view_menus())


# Resturent class

class Resturant:

    def manage_menu(self):
        pass









