from domain.repositories.account_repository import AccountRepository
from domain.entities.account import Account
from domain.value_objects.money import Money

class SQLAccountRepository(AccountRepository):
    def __init__(self, db_session):
        self.db = db_session

    def get_by_id(self, account_number):
        result = self.db.execute(
            "SELECT * FROM accounts WHERE account_number = :acc",
            {"acc": account_number}
        ).fetchone()
        if not result:
            return None
        return Account(
            result["account_number"],
            result["owner_name"],
            result["account_type"],
            Money(result["balance"], result["currency"]),
        )

    def save(self, account):
        self.db.execute(
            "UPDATE accounts SET balance = :bal WHERE account_number = :acc",
            {"bal": account.balance.amount, "acc": account.account_number},
        )
        self.db.commit()
