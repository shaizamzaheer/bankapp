#%%
# functions for program access
from bankapp import max_amnt, session
from bankapp.db_classes import *
from sqlalchemy import select
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
    Args:
    account id,
    amount to withdraw: $
    """
    try:
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
    except ValueError2:
        print("Amount must be less than balance")
    except NoResultFound:
        print("Account not found")
