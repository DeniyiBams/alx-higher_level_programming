#!/usr/bin/python3
"""
Contains the class definition of a City and an instance
Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City (Base):
    """ Definition of class City"""
    __tablename__ = 'cities'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer. ForeignKey('states.id'))
