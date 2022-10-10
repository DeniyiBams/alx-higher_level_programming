#!/usr/bin/python3
"""
Contains the class definition of a Sate and an instance
Base = declarative_base()
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State (Base):
    """ Definition of class State"""
    __tablename__ = 'states'

    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
