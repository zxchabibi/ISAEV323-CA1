class BankAccount:
    def __init__(self, holder, balance=0):
        self.account_holder = holder
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств!")
        else:
            self.balance -= amount
    def get_balance(self):
        return self.balance
account = BankAccount("Ivanov", 100)
account.deposit(50)
account.withdraw(200) 
account.withdraw(30)
print(account.get_balance()) 