#%%
# https://stackoverflow.com/questions/58660378/how-use-pytest-to-unit-test-sqlalchemy-orm-classes

from bankapp.bank_funcs import add_account
from sqlalchemy import select
from bankapp.models import Account
import pytest


@pytest.mark.parametrize(
    "cust_id,_type"[
        (10001, "LOC"),
    ]
)
def test_add_account(dbsession, cust_id, _type):
    _acc_id = add_account(cust_id, _type)
    assert dbsession.execute(
        select(Account).where(Account.acc_id == _acc_id)
    ).scalar_one()
