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
    Session,
)
from sqlalchemy.orm import declarative_base
from sqlalchemy_utils import PhoneNumber


def initialize_db() -> None:
    """
    Create the Database if it doesn't exist, put in some sample Data

    Parameters: None

    Return: None
    """

    DB = "banking.sqlite"
    db_path = Path(Path(__file__).parent, DB)

    if db_path.exists():
        db_path.unlink()

    bankapp_folder = str(Path(__file__).parent)
    db_connect_string = f"sqlite:///{bankapp_folder}/{DB}"

    # future = true allows sqlalchemy 2.0 syntax use
    engine = create_engine(db_connect_string, echo=True, future=True)
    meta = MetaData()
    Base = declarative_base()

    person_table = Table(
        "Person",
        meta,
        Column("id", Integer, primary_key=True),
        Column("first_name", String, nullable=False),
        Column("last_name", String, nullable=False),
        Column("address", String),
        Column("phone,", PhoneNumber),
    )

    customer_table = Table(
        "Customer",
        meta,
        Column("c_id", Integer, primary_key=True),
        Column("p_id", ForeignKey("Person.id"), nullable=False),
        Column("branch,", String),
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
    )

    meta.create_all(engine)
