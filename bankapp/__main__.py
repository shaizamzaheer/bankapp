#%%
# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from bankapp import version
from bankapp.bank_funcs import *

app = typer.Typer(
    name="bankapp",
    help="bankapp is a practice project in python to set up a bank model with entities such as customers, employees, services and records and some simple methods.",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]bankapp[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


def account_callback(value: int) -> int:
    if value != 2:
        raise typer.BadParameter("Only Camila is allowed")
    return value


@app.callback()
def main(
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the bankapp package.",
    ),
) -> None:
    return


# how to add commands as sub commands - create new apps
accounts_app = typer.Typer()
app.add_typer(accounts_app, name="accounts")
users_app = typer.Typer()
app.add_typer(users_app, name="users")


@accounts_app.command("create")
def accounts_create(item: str):
    console.print(f"Creating item: {item}")


@accounts_app.command("delete")
def accounts_delete(item: str):
    console.print(f"Deleting item: {item}")


@accounts_app.command("deposit")
def accounts_deposit(
    account: int = typer.Option(
        ..., "-acc", prompt="Enter account id", callback=account_callback
    ),
    amt: int = typer.Option(..., "-amt", prompt="Enter amt id"),
) -> None:
    console.print(f"Depositing: ${amt} to account {account}")
    deposit(account, amt)


@accounts_app.command("withdraw")
def accounts_withdraw(account: int, amt: int):
    console.print(f"Withdrawing: ${amt} from account {account}")
    withdraw(account, amt)


@users_app.command("create")
def users_create(user_name: str):
    console.print(f"Creating user: {user_name}")


@users_app.command("delete")
def users_delete(user_name: str):
    console.print(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()

# %%
