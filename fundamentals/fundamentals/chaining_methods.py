

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: $" + str(self.account_balance))
    
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Jack = User("Jack S", "jacks@python.com")
Wendy = User("Wendy K", "wendyk@python.com")
Betty = User("Betty Z", "bettyz@python.com")

Jack.make_deposit(200).make_deposit(100).make_deposit(50).make_withdrawl(120).transfer_money(Betty,30).display_user_balance()

Wendy.make_deposit(20).make_deposit(10).make_withdrawl(2).make_withdrawl(1).display_user_balance()

Betty.make_deposit(50).make_withdrawl(1).make_withdrawl(2).make_withdrawl(3).display_user_balance()