from domain.value_objects.money import Money

class Account:
    def __init__(self, account_number: str, owner_name: str, account_type: str, balance: Money):
        self.account_number = account_number
        self.owner_name = owner_name
        self.account_type = account_type
        self.balance = balance

    def deposit(self, amount: Money):
        self.balance = self.balance.add(amount)

    def withdraw(self, amount: Money):
        self.balance = self.balance.subtract(amount)

    def available_balance(self) -> Money:
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}) - {self.owner_name}: {self.balance}"

    
