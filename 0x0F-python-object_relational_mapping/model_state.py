#!/usr/bin/python3
""" 0x0F-python-object_relational_mapping """

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

from sqlalchemy import Column, Integer, String

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
    return "<State(name='%s')>" % (self.name,)


