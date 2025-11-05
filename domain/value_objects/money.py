class Money:
    def __init__(self, amount: float, currency: str):
        self.amount = amount
        self.currency = currency

    def add(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot add different currencies")
        return Money(self.amount + other.amount, self.currency)

    def subtract(self, other):
        if self.currency != other.currency:
            raise ValueError("Cannot subtract different currencies")
        if other.amount > self.amount:
            raise ValueError("Insufficient funds")
        return Money(self.amount - other.amount, self.currency)

    def __repr__(self):
        return f"{self.amount:.2f} {self.currency}"
