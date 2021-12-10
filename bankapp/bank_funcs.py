#%%
# functions for program access
from bankapp import max_amnt, session
from bankapp.models import *
from sqlalchemy import select, exists, update
from sqlalchemy.orm.exc import NoResultFound


class Error(Exception):
    """Base class for exceptions."""

    pass


class AmtApprovalError(Error):
    """Raised when an amnt withdrawn or deposited is greater than max amnt.

    Attributes:
        expression -- amt > max_amt(default $5000)
        message -- Needs Employee approval
    """

    def __init__(self, message="That amount needs to be approved"):
        self.message = message


class ValueError2(Error):
    pass


def deposit(account: int, amt: int) -> None:
    """Increase the balance with the amount specified.
    account id,
    amount to deposit: $
    """
    try:
        if amt <= 0:
            raise ValueError
        if amt > max_amnt:
            raise AmtApprovalError
        # get current acc
        acc = session.execute(
            select(Account).where(Account.acc_id == account)
        ).scalar_one()
        # update
        acc.balance_cents += amt * 100
        session.commit()
    except ValueError:
        print("Amount must not be negative")
    except AmtApprovalError as e:
        print(e.message)
    except NoResultFound:
        print("Account not found")


def withdraw(account: int, amt: int) -> None:
    """decrease the balance with the amount specified.
    account id,
    amount to withdraw: $
    """
    try:
        amt = int(amt)
        # get current acc value
        acc = session.execute(
            select(Account).where(Account.acc_id == account)
        ).scalar_one()
        if amt <= 0:
            raise ValueError
        if amt > max_amnt:
            raise AmtApprovalError
        if amt > acc.balance_cents:
            raise ValueError2
        # update
        acc.balance_cents -= amt * 100
        session.commit()
    except ValueError:
        print("Amount must not be negative")
    except AmtApprovalError:
        pass
    except ValueError as e:
        # how do i raise the same exception with a custom message in python
        print("Amount must be less than balance")
    except NoResultFound:
        print("Account not found")


def add_account(cust_id: int, type: str) -> Account.acc_id:
    cust_id = int(cust_id)
    """Add an account for a specific user
    returns account object"""
    acc = Account(c_id=cust_id, acc_type=type, balance_cents=0)
    session.add(acc)
    session.commit()
    return acc.acc_id


def delete_account(ac_id) -> None:
    """Delete bank account given id"""
    try:
        acc = session.query(Account).filter(Account.acc_id == ac_id).first()
        session.delete(acc)
        session.commit()
    except NoResultFound:
        print("Account not found")


def add_customer(_fname: str, _lname: str, _addr: str, _phone: str) -> Customer.c_id:
    """Add an customer given fname, lname, address, and phone #"""
    stmt = (
        (Person.first_name == _fname)
        & (Person.last_name == _lname)
        & (Person.address == _addr)
        & (Person.phone == _phone)
    )
    # add to person table first if it's not there
    if not session.query(exists().where(stmt)).scalar():
        per = Person(first_name=_fname, last_name=_lname, address=_addr, phone=_phone)
        session.add(per)
        session.commit()
        _p_id = per.id
    else:
        _p_id = session.query(Person.id).filter(stmt).scalar()

    session.add(Customer(p_id=_p_id))
    session.commit()


def delete_customer(cust_id: int) -> None:
    """Delete customer given id"""
    try:
        cust = session.query(Customer).filter(Customer.c_id == cust_id).first()
        session.delete(cust)
        session.commit()
    except NoResultFound:
        print("Customer not found")


def loan_approval(s_id: int):
    """given a service_id, approve the loan"""
    try:
        serv = session.query(Service).get(s_id)
        serv.approved = 1
        session.commit()
    except NoResultFound:
        print("Customer not found")
