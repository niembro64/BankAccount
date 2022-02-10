

class BankAccount:

    # don't forget to add some default values for these parameters!
    def __init__(self, n="BLANK", i_r=0.1, b=0):
        self.name = n
        self.balance = b
        self.int_rate = i_r

    @classmethod
    def printAll(cls):
        RobyAcct.display_account_info()
        EricAcct.display_account_info()
        return 0

        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if (self.balance - amount < 0):
            print("Insufficient Funds: Charging a $5 Fee")
            self.balance -= 5
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f"{self.name} - Balance: {self.balance} - Interest: {self.int_rate}")
        return self

    def yield_interest(self):
        if (self.balance >= 0):
            self.balance = self.balance * self.int_rate
        return self


##################################################

RobyAcct = BankAccount("Roby")
EricAcct = BankAccount("Eric")

RobyAcct.deposit(10).deposit(100).deposit(1000).withdraw(
    1).yield_interest().display_account_info()
EricAcct.deposit(10000).deposit(10000).withdraw(1).withdraw(
    1).withdraw(1).withdraw(1).yield_interest().display_account_info()


print()
RobyAcct.printAll()
