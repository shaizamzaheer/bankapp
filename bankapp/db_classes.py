#%%
from sqlalchemy.ext.automap import automap_base
from sqlalchemy import create_engine
import logging
from bankapp import db_connect_string

engine = create_engine(db_connect_string, echo=False, future=True)

# automatically determine basic classes and relationships
Base = automap_base()

# TODO: use inheritance to reflect the person sub-tables
Base.prepare(engine, reflect=True)

Person, Customer, Employee, Account, Service = (
    Base.classes.Person,
    Base.classes.Customer,
    Base.classes.Employee,
    Base.classes.Account,
    Base.classes.Service,
)

# %%
