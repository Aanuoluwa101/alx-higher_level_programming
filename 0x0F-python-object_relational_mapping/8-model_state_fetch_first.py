#!/usr/bin/python3
"""A module that lists all State objects
   from the database hbtn_0e_6_usa"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


db = 'mysql+mysqldb://{}:{}@localhost/{}'
if __name__ == "__main__":
    engine = create_engine(db.format(sys.argv[1], sys.argv[2],
                           sys.argv[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    states = session.query(State).order_by(State.id).first()

    if states is None:
        print("Nothing")
    else:
        print("{}: {}".format(states.id, states.name))
