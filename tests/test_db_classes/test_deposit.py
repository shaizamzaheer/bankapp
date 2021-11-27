#%%
# https://stackoverflow.com/questions/58660378/how-use-pytest-to-unit-test-sqlalchemy-orm-classes

from bankapp.bank_funcs import deposit
from sqlalchemy import select
from bankapp.db_classes import Account


def test_deposit(dbsession):
    deposit(account=1_000_001, amt=400)
    assert (
        dbsession.execute(select(Account).where(Account.acc_id == 1_000_001))
        .scalar_one()
        .balance_cents
        == 5400_00
    )


# %%
