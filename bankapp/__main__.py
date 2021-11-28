#%%
# type: ignore[attr-defined]

from rich.console import Console
import logging
from bankapp import version
from bankapp.bank_funcs import *

app = """
    name: bankapp
    help: bankapp is a practice project in python to set up a bank model with entities such as customers, employees, services and records and some simple methods.

    Commands:
        accounts
        customers
        employees
        services
        quit
"""
console = Console()
console.print(f"[yellow]bankapp[/] version: [bold blue]{version}[/]")


def main() -> None:
    while True:
        console.print(app)
        mode = input("Enter command:")
        if mode == "quit":
            exit()
        elif mode == "accounts":
            console.print(accounts_command)
        elif mode == "customers":
            console.print(customer_command)
        elif mode == "services":
            pass
        else:
            console.print("Incorrect command")


accounts_command = """
Choose:
1. create account
2. delete account
3. deposit
4. withdraw
5. quit
"""
customer_command = """
Choose:
1. customer create
2. customer delete
3. quit
"""

services_command = """
1. approve loan
2. quit
"""


def accounts_create(cust_id: int, type: str) -> None:
    console.print(f"Creating account {type} for customer: {cust_id}")


def accounts_delete(acc_id: str) -> None:
    console.print(f"Deleting account: {acc_id}")


def accounts_deposit(
    account: int,
    amt: int,
) -> None:
    console.print(f"Depositing: ${amt} to account {account}")
    deposit(account, amt)


def accounts_withdraw(account: int, amt: int) -> None:
    console.print(f"Withdrawing: ${amt} from account {account}")
    withdraw(account, amt)


def customers_create(
    id: int,
):
    console.print(f"Creating user: {id}")


def customer_delete(id: int):
    console.print(f"Deleting user: {id}")


def approve_loan(s_id: int):
    console.print(f"Approving loan: {s_id}")


if __name__ == "__main__":
    main()

# %%
