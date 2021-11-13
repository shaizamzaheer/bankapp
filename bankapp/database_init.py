#%%
# Using https://docs.sqlalchemy.org/en/20/tutorial/index.html

# create initial sqlite db
import logging
import attr
from sqlalchemy import create_engine, text, MetaData, Column, Table, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import registry

engine = create_engine("sqlite:///foo.db", echo=True, future=True)

mapper_registry = registry()


@mapper_registry.mapped
@attr.s
class User:
    __table__ = Table(
        "user",
        mapper_registry.metadata,
        Column("id", Integer, primary_key=True),
        Column("name", String(50)),
    )
    id = attr.ib()
    name = attr.ib()


with engine.connect() as conn:
    conn.execute(text("CREATE TABLE user (x int, y int)"))
    conn.execute(
        text("INSERT INTO user (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": "dkfj"}, {"x": 2, "y": "dkfdk"}],
    )
    conn.commit()

# %%
