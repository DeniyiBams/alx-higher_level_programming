#!/usr/bin/python3
"""
Contains the class definition of a City and an instance
"""

import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String
from relationship_state import Base, State
from sqlalchemy.orm import relationship


class City (Base):
    """ Definition of class City"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
    state = relationship("State", back_populates="cities")
