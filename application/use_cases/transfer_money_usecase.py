
from domain.services.transfer_service import TransferService
from domain.value_objects.money import Money
from domain.repositories.account_repository import AccountRepository

class TransferMoneyUseCase:
    """Application layer use case for transferring money between accounts."""

    def __init__(self, account_repository: AccountRepository, transfer_service: TransferService):
        self.account_repository = account_repository
        self.transfer_service = transfer_service

    def execute(self, from_account_id: str, to_account_id: str, amount: float, currency: str):
        # 1. Load accounts from repository
        from_account = self.account_repository.get_by_id(from_account_id)
        to_account = self.account_repository.get_by_id(to_account_id)

        # 2. Create Money value object
        money = Money(amount, currency)

        # 3. Perform domain operation
        self.transfer_service.transfer(from_account, to_account, money)

        # 4. Save updated accounts
        self.account_repository.save(from_account)
        self.account_repository.save(to_account)

        return f"Transferred {money} from {from_account.owner_name} to {to_account.owner_name}"
