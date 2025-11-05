from sqlalchemy import Table, Column, String, Float, MetaData

metadata = MetaData()

accounts = Table(
    "accounts",
    metadata,
    Column("account_number", String, primary_key=True),
    Column("owner_name", String),
    Column("account_type", String),
    Column("balance", Float),
    Column("currency", String),
)
