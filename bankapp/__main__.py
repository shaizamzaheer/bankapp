#%%
# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from bankapp import version
from bankapp.example import hello

# session future is true


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


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


@app.callback()
# @app.command(name="")
def main(
    #     name: str = typer.Option(
    #          ...,
    #      help="Person to greet."),
    #     color: Optional[Color] = typer.Option(
    #         None,
    #         "-c",
    #         "--color",
    #         "--colour",
    #         case_sensitive=False,
    #         help="Color for print. If not specified then choice will be random.",
    #     ),
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


#     """Print a greeting with a giving name."""
#     if color is None:
#         color = choice(list(Color))

#     greeting: str = hello(name)
#     console.print(f"[bold {color}]{greeting}[/]")

# app = typer.Typer()
items_app = typer.Typer()
app.add_typer(items_app, name="items")
users_app = typer.Typer()
app.add_typer(users_app, name="users")


@items_app.command("create")
def items_create(item: str):
    typer.echo(f"Creating item: {item}")


@items_app.command("delete")
def items_delete(item: str):
    typer.echo(f"Deleting item: {item}")


@items_app.command("sell")
def items_sell(item: str):
    typer.echo(f"Selling item: {item}")


@users_app.command("create")
def users_create(user_name: str):
    typer.echo(f"Creating user: {user_name}")


@users_app.command("delete")
def users_delete(user_name: str):
    typer.echo(f"Deleting user: {user_name}")


if __name__ == "__main__":
    app()
