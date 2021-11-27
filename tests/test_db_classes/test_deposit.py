#%%
# https://stackoverflow.com/questions/58660378/how-use-pytest-to-unit-test-sqlalchemy-orm-classes

from bankapp.bank_funcs import deposit
from sqlalchemy import select
from bankapp.db_classes import Account
import pytest


@pytest.mark.parametrize(
    "acc,amount,expected",
    [
        (1_000_001, 400, 5400_00),
        (1_000_001, 12000, 5000_00),
    ],
)
def test_deposit(dbsession, acc, amount, expected):
    deposit(account=acc, amt=amount)
    assert (
        dbsession.execute(select(Account).where(Account.acc_id == acc))
        .scalar_one()
        .balance_cents
        == expected
    )


# %%
