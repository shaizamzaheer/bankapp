from bankapp.bank_funcs import withdraw
from sqlalchemy import select
from bankapp.db_classes import Account
import pytest


@pytest.mark.parametrize(
    "acc,amount,expected",
    [
        (1_000_002, 400, 600_00),
    ],
)
def test_withdraw(dbsession, acc, amount, expected):
    withdraw(account=acc, amount=amount)
    assert (
        dbsession.execute(select(Account).where(Account.acc_id == acc))
        .scalar_one()
        .balance_cents
        == expected
    )
