# a bank account app


class BankAccount:
    balance = 0

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        print(f" Hello {self.name}, your balance is {self.balance} ")

    def show_balance(self):
        print(f" Your balance is {self.balance} ")

    def deposit(self, amount):
        if amount <= 0:
            print(" You can't deposit less than 0 dollars ")
        else:
            print(f" Adding {amount} to your balance ")
            self.balance += amount
        # print(f" Your new balance is {self.balance} ")

    def withdraw(self, amount):
        if amount > self.balance:
            print("You don't have enough money to withdraw")
        else:
            print(f" Withdrawing {amount} from your balance ")
            self.balance -= amount
        # print(f" Your new balance is {self.balance} ")


myAccount = BankAccount("bleep")
myAccount.__repr__()
myAccount.show_balance()
myAccount.deposit(2000)
myAccount.withdraw(1000)
myAccount.__repr__()
