from dataclasses import dataclass

@dataclass(frozen=True)
class Money:
    amount: float
    currency: str

    def add(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add money of different currency")
        return Money(self.amount + other.amount, self.currency)
    
    def sub(self, other: "Money") -> "Money":
        if self.currency != other.currency:
            raise ValueError("Cannot add money of different currency")
        if self.amount < other.amount:
            raise ValueError("Cannot subtract more then the available amount")
        return Money(self.amount - other.amount, self.amount)
    
    def __str__(self) -> str:
        return f"{self.amount:.2f} {self.currency}"
