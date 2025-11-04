
from abc import ABC, abstractmethod
from domain.entities.account import Account

class AccountRepository(ABC):
    """Abstract interface for account persistence."""

    @abstractmethod
    def get_by_id(self, account_number: str) -> Account:
        pass

    @abstractmethod
    def save(self, account: Account) -> None:
        pass
