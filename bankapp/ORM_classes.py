#%%
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, MetaData, Table, update
from pathlib import Path
import logging
from bankapp import max_amnt

# TODO: #28 move db connection to config file
bankapp_folder = Path(__file__).parent
DB = "banking.sqlite"
db_path = bankapp_folder / DB
db_connect_string = f"sqlite:///{db_path}"

engine = create_engine(db_connect_string, echo=False, future=True)

# automatically determine basic classes and relationships
Base = automap_base()

# TODO: use inheritance to reflect the person sub-tables
Base.prepare(engine, reflect=True)
Person, Customer, Employee, Account, Service = (Base.classes.Person,)
Base.classes.Customer,
Base.classes.Employee,
Base.classes.Account,
Base.classes.Service


class Error(Exception):
    """Base class for exceptions in this module."""

    pass


class AmntApprovalError(Error):
    """Raised when an amnt withdrawn or deposited is greater than max amnt.

    Attributes:
        expression -- amt > max_amt(default 5000)
        message -- explanation of the error
    """

    def __init__(self, amt, message="That amount needs an approval"):
        self.amt = amt
        self.message = message


def deposit(account: int, amt: int) -> None:
    """Increase the balance with the amount specified"""
    with Session(engine) as session:
        while True:
            try:
                if amt <= 0:
                    raise ValueError
                if amt > max_amnt:
                    raise AmntApprovalError
                session.execute(
                    update(Account)
                    .where(Account.acc_id == account)
                    .values(fullname="Sandy Squirrel Extraordinaire")
                )
            except ValueError:
                pass

        # session.
        session.commit()


# class Person(Base):
#     __table__ = Table('Person', meta, autoload=True, autoload_with=engine)

# class Customer(Person):
#     __table__= Table('Customer', meta, autoload = True, autoload_with=engine)

# class Employee(Person):
#     __table__ = Table('Employee', meta, autoload = True, autoload_with=engine)

# class Account(Base):
#     __table__ = Table('Account', meta, autoload = True, autoload_with=engine)

# class Service(Base):
#     __table__= Table('Service', meta, autoload = True, autoload_with=engine)

# %%
