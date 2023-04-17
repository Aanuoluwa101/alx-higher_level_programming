#!/usr/bin/python3
"""A module that lists all State objects
   from the database hbtn_0e_6_usa"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

args = sys.argv
db = 'mysql+mysqldb://{}:{}@localhost/{}'
if __name__ == "__main__":
    engine = create_engine(db.format(args[1], args[2],
                           args[3]), pool_pre_ping=True)
    session = Session(bind=engine)
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
