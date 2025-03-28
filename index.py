from os import remove  #admin class
class Admin:
    def __init__(self):
        self.cart = []
        self.customer_account = []
   # add menu
    def add_menu(self):
        menu =str(input("input dish name"))
        price = int(input("input the price "))
        self.cart.append({"name":menu,"price":price})
     #view menu
    def view_menu(self):
        return self.cart

    def remove_menu(self):
       del self.cart
        #menu = input()
        #self.cart.remove(menu)
    #### create customer account
    def add_customer_account(self):
        #input example -> name email
        name = str(input("please enter your name: "))
        email=str(input("please enter your email address : "))
        adress = str(input("plese enter your adress: "))
        self.customer_account.append({"name":name,"email":email,"address":adress})


    def remove_customer_account(self):
        name = str(input("please provide customer name: "))
        if name in self.customer_account:
            self.customer_account.remove(name)
            print("successfully removed account ")
        else:
            print("Name does not match ")
        #input example -> name email
        #remove_name_email = input()
        #self.customer_account.remove(remove_name_email)

    def view_customer(self):
        return self.customer_account

    def modify_menu(self):
        pass
        #input example -> menu price
        #value=input()
        #self.cart.insert(0,value)

#test phase of admin class ->
#cusomers = Admin()
#cusomers.add_customer_account()
#print(cusomers.view_customer())

#cusomers.add_menu()
#cusomers.add_menu()
#print(cusomers.view_menu())


#customer class
class Customer:
    def __init__(self,admin):
        self.balance = 0
        self.order_cart = []
        self.admin = admin

    def add_balance(self):
        money = int(input("enter money : "))
        self.balance +=money

    def view_balance(self):
         return self.balance
    def create_order(self):
         print(self.admin.view_menu())
         order=str(input("please enter your dish name"))
         print(self.admin.view_menu())
         self.order_cart.append(order)



    def view_past_order(self):
        return self.order_cart

    def view_menus(self):
        return self.admin.view_menu()


#admins = Admin()
#admins.add_menu()
#customers = Customer(admins)
#print(customers.view_menus())
# Resturent class
class Restaurant:
    def __init__(self,admin):
        self.admin = admin

    def manage_menu(self):
        return self.admin.view_menu()

    def manage_customer_account(self):
        return self.admin.view_customer()

def admin_menu(admin):

    print("1.create account ")
    print("2.view customer account ")
    print("3. add menu ")
    print("4 . view menu")
    print("5.remove menu ")
    print("6.Remove customer account")
    chc =int(input("input your preference "))
    if chc==1:
        admin.add_customer_account()
    elif chc==2:
        print(admin.view_customer() )
    elif chc==6:
        admin.remove_customer_account()


def option():
    print("1: Customer")
    print("2 : Resturant")
    print("3:Admin")
    print("4. cancel the program")
def cus(admins,rest):
    print("1.add balance ")
    print("2.view balace ")
    print("3.Ordr menu")
    print("4.past order")
    print("5. see the menu")
    print("6.Home page")
    chc = int(input("input your preference: "))

    if chc ==1:
        rest.add_balance()
    elif chc==2:
        print(rest.view_balance())
    elif chc==3:
        print(rest.create_order())
    elif chc==4:
        print(rest.view_past_order())
def restu(resturent):
    pass


def loop():
    admin = Admin()
    customer = Customer(admin)
    resturent=Restaurant(admin)
    while True :
        option()
        choice = int(input("enter your role : "))
        if choice==1:
            cus(admin,customer)
        elif choice==2:
            restu(resturent)
        elif choice==3:
            admin_menu(admin)

loop()











