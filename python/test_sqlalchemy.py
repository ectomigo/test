"""
testing with sqlalchemy
"""

from sqlalchemy import MetaData, Table, Column, Integer, String, insert, select
from sqlalchemy.orm import declarative_base

metadata_obj = MetaData()
Base = declarative_base()

one_table = Table(
    'one',
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('val', String)
)

class Two(Base):
    __tablename__ = 'two'

    id = Column(Integer, primary_key=True)
    val = Column(String)

class SchemaThree(Base):
    __tablename__ = 'three'
    __table_args__ = {"schema": "sch"}

    id = Column(Integer, primary_key=True)
    val = Column(String)

stmt = insert(one_table).values(val='hi')
stmt = select(one_table).where(one_table.c.val == 'something')
stmt = select(Two)
