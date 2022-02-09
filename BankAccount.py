

class BankAccount:

    # don't forget to add some default values for these parameters!
    def __init__(self, n = "", i_r = 0, b = 0):
        self.name = n
        self.balance = b
        self.int_rate = i_r
        
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"{self.name} : {self.balance} : {self.int_rate}")
        return self
    def yield_interest(self):
        self.balance = self.balance * self.int_rate
        return self


f