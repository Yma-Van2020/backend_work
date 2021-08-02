

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Jack = User("Jack S", "jacks@python.com")
Wendy = User("Wendy K", "wendyk@python.com")
Betty = User("Betty Z", "bettyz@python.com")

Jack.make_deposit(200)
Jack.make_deposit(100)
Jack.make_deposit(50)
Jack.make_withdrawl(120)
Jack.transfer_money(Betty,30)
Jack.display_user_balance()

Wendy.make_deposit(20)
Wendy.make_deposit(10)
Wendy.make_withdrawl(2)
Wendy.make_withdrawl(1)
Wendy.display_user_balance()

Betty.make_deposit(50)
Betty.make_withdrawl(1)
Betty.make_withdrawl(2)
Betty.make_withdrawl(3)
Betty.display_user_balance()