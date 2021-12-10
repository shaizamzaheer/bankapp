#%%
# type: ignore[attr-defined]

from rich.console import Console
import logging
from bankapp import version
from bankapp.bank_funcs import *
from pathlib import Path

app = """
    bankapp
    help: bankapp is a practice project in python to set up 
    a bank model with entities such as customers, employees, 
    services and records and some simple methods.

    Choose:
    1. accounts
    2. customers
    3. services
    4. quit

"""
console = Console()
console.print(f"[yellow]bankapp[/] version: [bold blue]{version}[/]")

# import argparse
# parser = argparse.ArgumentParser()
# parser.add_argument("")
# args, unknown = parser.parse_known_args()


def accounts_mode() -> None:
    """
    Make changes to bank accounts.
    """
    while True:
        console.print(
            """
    Choose:
    1. create account
    2. delete account
    3. deposit
    4. withdraw
    5. quit
        """
        )
        mode = input("Enter command:")
        if mode in ["5", "quit"]:
            break
        elif mode == "1":
            cust = input("Enter cust id:")
            type = input("Enter Account Type:")
            account_create(cust, type)
        elif mode == "2":
            acc = input("Enter acc id:")
            account_delete(acc)
        elif mode == "3":
            cust = input("Enter acc id:")
            amt = input("Enter amt($):")
            account_deposit(cust, amt)
        elif mode == "4":
            cust = input("Enter acc id:")
            amt = input("Enter amt($):")
            account_withdraw(cust, amt)
        else:
            console.print("Incorrect Command")


def customers_mode() -> None:
    while True:
        console.print(
            """Choose:
    1. create customer
    2. delete customer
    3. quit
        """
        )
        mode = input("Enter command:")
        if mode in ["3", "quit"]:
            break
        elif mode == "1":
            fname = input("Enter customer first name:")
            lname = input("Enter customer last name:")
            addr = input("Enter customer address:")
            phone = input("Enter customer phone number:")
            customer_create(fname, lname, addr, phone)
        elif mode == "2":
            cust = input("Enter cust id:")
            customer_delete(cust)
        else:
            console.print("Incorrect Command")


def services_mode() -> None:
    while True:
        console.print(
            """
    1. approve loan
    2. quit
        """
        )
        mode = input("Enter command:")
        if mode in ["2", "quit"]:
            break
        elif mode == "1":
            s_id = input("Enter service id:")
            approve_loan(s_id)
        else:
            console.print("Incorrect Command")


def account_create(cust_id: int, type: str) -> None:
    console.print(f"Creating account {type} for customer: {cust_id}")
    add_account(cust_id, type)


def account_delete(acc_id: str) -> None:
    console.print(f"Deleting account: {acc_id}")
    delete_account(acc_id)


def account_deposit(account: int, amt: int) -> None:
    console.print(f"Depositing: ${amt} to account {account}")
    deposit(account, amt)


def account_withdraw(account: int, amt: int) -> None:
    console.print(f"Withdrawing: ${amt} from account {account}")
    withdraw(account, amt)


def customer_create(first_name: str, last_name: str, addr: str, phone: str) -> None:
    console.print(f"Creating user: {first_name} {last_name}")
    add_customer(first_name, last_name, addr, phone)


def customer_delete(id: int) -> None:
    console.print(f"Deleting user: {id}")
    delete_customer(id)


def approve_loan(s_id: int) -> None:
    console.print(f"Approving loan: {s_id}")
    loan_approval(s_id)


if __name__ == "__main__":
    logging.basicConfig(
        filename=Path().parent / "logs" / "db_log.log",
        filemode="w",
        level=logging.DEBUG,
    )
    logging.getLogger("sqlalchemy.engine").setLevel(logging.INFO)

    while True:
        logging.info("app started")
        console.print(app)
        mode = input("Enter command:")
        if mode in ["quit", "4"]:
            console.print("Quitting")
            logging.info("quitting app")
            exit()
        elif mode in ["1", "accounts"]:
            accounts_mode()
        elif mode in ["2", "customers"]:
            customers_mode()
        elif mode in ["3", "services"]:
            services_mode()
        else:
            console.print("Incorrect command")

# %%
