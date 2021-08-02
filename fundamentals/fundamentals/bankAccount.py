
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
            

account1 = BankAccount(0.05, 500)
account2 = BankAccount(0.025, 2000)

account1.deposit(30).deposit(120).deposit(10).withdraw(5).yield_interest().display_account_info()
account2.deposit(50).deposit(90).withdraw(52).withdraw(3).withdraw(45).withdraw(2).yield_interest().display_account_info()
BankAccount.print_acc_info()