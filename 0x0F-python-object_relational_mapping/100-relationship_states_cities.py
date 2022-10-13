#!/usr/bin/python3
"""
lists all City objects from a database
"""


import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    cal = State(name="California")
    cal.cities = [city(name="San Francisco")]
    session.add(cal)
    session.commit()
    session.close()
