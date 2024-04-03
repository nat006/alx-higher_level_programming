#!/usr/bin/python3
"""
Contains definition of State class and an instance Base = declarative_base()
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Class that represents a state
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine(
             'mysql+mysqldb://username:password@localhost:3306/database')
    Base.metadata.create_all(engine)
