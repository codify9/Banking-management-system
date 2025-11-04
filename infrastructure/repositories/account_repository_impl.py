
from domain.repositories.account_repository import AccountRepository
from domain.entities.account import Account
from domain.value_objects.money import Money

class InMemoryAccountRepository(AccountRepository):
    """Simple in-memory repository for demo or testing."""
    def __init__(self):
        self._storage = {}

    def get_by_id(self, account_number: str) -> Account:
        return self._storage.get(account_number)

    def save(self, account: Account) -> None:
        self._storage[account.account_number] = account
