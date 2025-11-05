
from domain.entities.account import Account
from domain.value_objects.money import Money
from domain.services.transfer_service import TransferService
from infrastructure.repositories.account_repository_impl import InMemoryAccountRepository
from application.use_cases.transfer_money_usecase import TransferMoneyUseCase


def main():
    # --- Setup phase (normally done by dependency injection) ---
    account_repo = InMemoryAccountRepository()
    transfer_service = TransferService()
    use_case = TransferMoneyUseCase(account_repo, transfer_service)

    # --- Create two demo accounts ---
    acc1 = Account("ACC001", "Alice", "savings", Money(1000, "USD"))
    acc2 = Account("ACC002", "Bob", "checking", Money(500, "USD"))

    account_repo.save(acc1)
    account_repo.save(acc2)

    # --- Simulate transfer ---
    print("Before transfer:")
    print(acc1)
    print(acc2)

    print("\nTransferring $200 from Alice to Bob...\n")
    print(use_case.execute("ACC001", "ACC002", 200, "USD"))

    print("\nAfter transfer:")
    print(account_repo.get_by_id("ACC001"))
    print(account_repo.get_by_id("ACC002"))


if __name__ == "__main__":
    main()
