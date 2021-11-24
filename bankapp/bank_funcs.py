#%%
# functions for program access
from bankapp import max_amnt
from db_classes import *
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


def deposit(session, account: int, amt: int) -> None:
    """Increase the balance with the amount specified
    Args: session,
    account id,
    amount to deposit
    """
    while True:
        try:
            if amt <= 0:
                raise ValueError
            if amt > max_amnt:
                raise AmtApprovalError
            # get current acc value
            acc = session.execute(
                select(Account).where(Account.acc_id == account)
            ).scalar_one()
            val = acc.balance_cents
            # update
            acc.balance_cents = val + amt
            session.commit()
            break
        except ValueError:
            print("Amount must not be negative")
        except AmtApprovalError:
            pass
