#!/usr/bin/python3
"""A module that lists all State objects
   from the database hbtn_0e_6_usa"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


db = 'mysql+mysqldb://{}:{}@localhost/{}'
if __name__ == "__main__":
    engine = create_engine(db.format(sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    session = Session(bind=engine)
    new_state = State(name='California')
    new_state.cities.append('San Francisco')
    session.add(new_state)
    session.commit()

