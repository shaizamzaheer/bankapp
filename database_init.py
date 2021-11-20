#%%
# Using https://docs.sqlalchemy.org/en/20/tutorial/index.html

# create initial sqlite db and ORM
import logging
from pathlib import Path

from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    insert,
    # select
)

logging.basicConfig(
    filename=Path().parent / "logs" / "db_log.log", filemode="w", level=logging.DEBUG
)
logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)


def initialize_db() -> None:
    """
    Create the Database if it doesn't exist, then put in some sample data

    Tables made:
    Person, Customer, Employee, Account, Services

    Parameters: None

    Return: None
    """

    # TODO: #26 refactor out details into config
    bankapp_folder = Path(__file__).parent / "bankapp"
    DB = "banking.sqlite"
    db_path = bankapp_folder / DB

    if db_path.exists():
        db_path.unlink()

    db_connect_string = f"sqlite:///{db_path}"

    # future = true allows sqlalchemy 2.0 syntax use
    engine = create_engine(db_connect_string, echo=False, future=True)
    meta = MetaData()

    person_table = Table(
        "Person",
        meta,
        Column("id", Integer, primary_key=True),
        Column("first_name", String, nullable=False),
        Column("last_name", String, nullable=False),
        Column("address", String),
        Column("phone", String(10)),
    )

    customer_table = Table(
        "Customer",
        meta,
        Column("c_id", Integer, primary_key=True),
        Column("p_id", ForeignKey("Person.id"), nullable=False),
        Column("branch", String),
    )

    employee_table = Table(
        "Employee",
        meta,
        Column("e_id", Integer, primary_key=True),
        Column("p_id", ForeignKey("Person.id"), nullable=False),
        Column("role", String, nullable=False),
    )

    accounts_table = Table(
        "Account",
        meta,
        Column("acc_id", Integer, primary_key=True),
        Column("c_id", ForeignKey("Person.id"), nullable=False),
        Column("acc_type", String, nullable=False),
        Column("balance_cents", Integer),
    )

    services_table = Table(
        "Service",
        meta,
        Column("serv_id", Integer, primary_key=True),
        Column("c_id", ForeignKey("Person.id"), nullable=False),
        Column("serv_type", String, nullable=False),
        Column("approved", Integer),
    )

    meta.create_all(engine)

    # TODO: #27 put into different function
    with engine.connect() as conn:
        result = conn.execute(
            insert(person_table),
            [
                {
                    "id": 1001,
                    "first_name": "Billy",
                    "last_name": "Bob",
                    "address": "100 Saw St.",
                    "phone": "6475551111",
                },
                {
                    "id": 1002,
                    "first_name": "Bobby",
                    "last_name": "Brown",
                    "address": "101 Saw St.",
                    "phone": "6475551234",
                },
            ],
        )
        conn.commit()

        result = conn.execute(
            insert(customer_table),
            [{"c_id": 10_001, "p_id": 1001, "branch": "Capital HQ"}],
        )
        conn.commit()

        result = conn.execute(
            insert(employee_table),
            [
                {
                    "e_id": 100_001,
                    "p_id": 1002,
                    "role": "Credit Consultant",
                }
            ],
        )
        conn.commit()

        result = conn.execute(
            insert(accounts_table),
            [
                {
                    "acc_id": 1_000_001,
                    "c_id": 10001,
                    "acc_type": "Savings",
                    "balance_cents": 5000_00,
                },
                {
                    "acc_id": 1_000_002,
                    "c_id": 10001,
                    "acc_type": "Checkings",
                    "balance_cents": 1000_00,
                },
            ],
        )
        conn.commit()

        result = conn.execute(
            insert(services_table),
            [
                {
                    "serv_id": 100_000_001,
                    "c_id": 1001,
                    "serv_type": "loan",
                    "approved": 0,
                }
            ],
        )
        conn.commit()
        # #debug
        # for row in conn.execute(select(customer_table)):
        #     print(row)


initialize_db()
logging.shutdown()
# %%
