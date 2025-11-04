
from domain.value_objects.money import Money
from domain.entities.account import Account

class TransferService:
    """Handles business logic for transferring money between accounts."""

    def transfer(self, from_account: Account, to_account: Account, amount: Money):
        if from_account.account_number == to_account.account_number:
            raise ValueError("Cannot transfer to the same account.")

        # Withdraw from sender
        from_account.withdraw(amount)

        # Deposit to receiver
        to_account.deposit(amount)

        print(f"Transferred {amount} from {from_account.account_number} "
              f"to {to_account.account_number}")
