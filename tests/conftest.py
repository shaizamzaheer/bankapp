# https://gist.github.com/kissgyorgy/e2365f25a213de44b9a2
#%%
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from bankapp.db_classes import Base
from bankapp import db_path
import pytest
import database_init


@pytest.fixture(scope="session")
def engine():
    return create_engine(f"sqlite:///{db_path}", future=True, echo=True)


@pytest.fixture(scope="session")
def tables(engine):
    Base.metadata.create_all(engine)
    yield
    # Base.metadata.drop_all(engine)


@pytest.fixture
def dbsession(engine, tables):
    database_init.initialize_db()
    """Returns an sqlalchemy session, and after the test tears down everything properly."""
    connection = engine.connect()
    # begin the nested transaction
    transaction = connection.begin()
    # use the connection with the already started transaction
    session = Session(bind=connection)
    # session = Session()
    yield session
    session.close()
    # roll back the broader transaction
    transaction.rollback()
    # put back the connection to the connection pool
    connection.close()


# %%
