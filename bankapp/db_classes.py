#%%
from sqlalchemy.ext.automap import automap_base
from bankapp import engine
import logging

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
