#%%
# # type: ignore[attr-defined]
"""bankapp is a practice project in python to set up a bank model with entities such as customers and employees and services and methods."""
from pathlib import Path

import sys

if sys.version_info >= (3, 8):
    from importlib import metadata as importlib_metadata
else:
    import importlib_metadata


def get_version() -> str:
    try:
        return importlib_metadata.version(__name__)
    except importlib_metadata.PackageNotFoundError:  # pragma: no cover
        return "unknown"


version: str = get_version()

# maximum amount (cents) that can be withdrawn or deposited
max_amnt: int = 5000_00

# prod db
bankapp_folder = Path(__file__).parent
DB = "banking.sqlite"
db_path = bankapp_folder / DB
db_connect_string = f"sqlite:///{db_path}"
# %%
