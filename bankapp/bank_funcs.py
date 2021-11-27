#%%
# functions for program access
from bankapp import max_amnt, session
from bankapp.db_classes import *
from sqlalchemy import select


class Error(Exception):
    """Base class for exceptions."""

    pass


class AmtApprovalError(Error):
    """Raised when an amnt withdrawn or deposited is greater than max amnt.

    Attributes:
        expression -- amt > max_amt(default $5000)
        message -- Needs Employee approval
    """

    def __init__(self, amt, message="That amount needs to be approved"):
        self.amt = amt
        self.message = message


class ValueError2(Error):
    pass


class Account(Account):
    def deposit(account: int, amt: int) -> None:
        """Increase the balance with the amount specified.
        account id,
        amount to deposit: $
        """
        while True:
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
                break
            except ValueError:
                print("Amount must not be negative")
            except AmtApprovalError:
                pass

    def withdraw(account: int, amt: int) -> None:
        """decrease the balance with the amount specified.
        Args:
        account id,
        amount to withdraw: $
        """
        while True:
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
                break
            except ValueError:
                print("Amount must not be negative")
            except AmtApprovalError:
                pass
            except ValueError2:
                print("Amount must be less than balance")
