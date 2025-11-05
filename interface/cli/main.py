from infrastructure.db.db_connection import get_db_session
from infrastructure.repositories.account_repository_impl import SQLAccountRepository
from domain.services.transfer_service import TransferService
from application.use_cases.transfer_money_usecase import TransferMoneyUseCase
from interface.cli.setup_db import setup_database
from contextlib import contextmanager

@contextmanager
def db_context():
    gen = get_db_session()
    db = next(gen)
    try:
        yield db
        next(gen, None)  # commit
    except Exception as e:
        print("❌ Database error:", e)   # <— show real issue
        raise
    finally:
        gen.close()

def main():
    setup_database()  # initialize schema + sample data

    with db_context() as db:
        repo = SQLAccountRepository(db)
        transfer_service = TransferService()
        use_case = TransferMoneyUseCase(repo, transfer_service)

        print(use_case.execute("ACC001", "ACC002", 200, "USD"))

if __name__ == "__main__":
    main()
