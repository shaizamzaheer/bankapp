from bankapp.bank_funcs import withdraw
from sqlalchemy import select
from bankapp.db_classes import Account


def test_withdraw(dbsession):
    withdraw(account=1_000_002, amt=400)
    assert (
        dbsession.execute(select(Account).where(Account.acc_id == 1_000_002))
        .scalar_one()
        .balance_cents
        == 600_00
    )
