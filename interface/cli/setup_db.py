from infrastructure.db.db_connection import engine
from infrastructure.db.models import metadata, accounts

def setup_database():
    metadata.create_all(engine)
    with engine.begin() as conn:
        conn.execute(
            accounts.insert(),
            [
                {"account_number": "ACC001", "owner_name": "Harsh", "account_type": "savings", "balance": 1000.0, "currency": "USD"},
                {"account_number": "ACC002", "owner_name": "Ayush", "account_type": "checking", "balance": 500.0, "currency": "USD"},
            ],
        )
