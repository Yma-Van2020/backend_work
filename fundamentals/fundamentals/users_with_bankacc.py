
class BankAccount:
    all_acc = []
    def __init__(self, int_rate = 0.01, balance = 0): 
        self.int_rate = int_rate
        self.balance = balance
        
        BankAccount.all_acc.append(self)
        
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
       self.balance -= amount
       return self

    def display_account_info(self):
       print("The current balance is: " + str(self.balance))
       
    def yield_interest(self):
       self.balance =  self.balance + (self.balance * self.int_rate)
       return self
    
    @classmethod
    def print_acc_info(cls):
        for account in cls.all_acc:
            account.display_account_info()

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.015, balance = 0)
    
    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self
    
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print("User: " + self.name + ", Balance: $" + str(self.account.balance))
    
    def transfer_money(self, other_user, amount):
        self.account.balance -= amount
        other_user.account.balance += amount
        return self

Jack = User("Jack S", "jacks@python.com")
Wendy = User("Wendy K", "wendyk@python.com")
Betty = User("Betty Z", "bettyz@python.com")

Jack.make_deposit(200).make_deposit(100).make_deposit(50).make_withdrawl(120).transfer_money(Betty,30).display_user_balance()

Wendy.make_deposit(20).make_deposit(10).make_withdrawl(2).make_withdrawl(1).display_user_balance()

Betty.make_deposit(50).make_withdrawl(1).make_withdrawl(2).make_withdrawl(3).display_user_balance()