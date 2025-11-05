from infrastructure.db.db_connection import get_db_session
from infrastructure.db.db_connection import SessionLocal
from infrastructure.repositories.account_repository_impl import SQLAccountRepository
from domain.services.transfer_service import TransferService
from application.use_cases.transfer_money_usecase import TransferMoneyUseCase
from contextlib import contextmanager

@contextmanager
def db_context():
    gen = get_db_session()
    db = next(gen)
    try:
        yield db
        next(gen, None)  # commit
    except Exception:
        gen.throw(Exception)
    finally:
        gen.close()


def main():
    # create DB session
    db = SessionLocal()

    # inject dependencies
    repo = SQLAccountRepository(db)
    transfer_service = TransferService()
    use_case = TransferMoneyUseCase(repo, transfer_service)

    # execute
    print(use_case.execute("ACC001", "ACC002", 200, "USD"))

    db.close()

if __name__ == "__main__":
    main()
