#!/usr/bin/python3

"""
This script defines a state class
and a base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class

    Attributes:
        __table__name (str): The table name of the class id (int):
        The State is of the class name (str): The State name
        of the class
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(120), nullable=False)
