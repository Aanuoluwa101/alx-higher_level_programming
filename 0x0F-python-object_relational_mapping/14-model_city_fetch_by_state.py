#!/usr/bin/python3
"""This module prints all City objects
   from the database hbtn_0e_14_usa"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


db = 'mysql+mysqldb://{}:{}@localhost/{}'
args = sys.argv
if __name__ == '__main__':
    engine = create_engine(db.format(args[1], args[2], args[3]))
    session = Session(bind=engine)
    cities = session.query(State.name, City.id, City.name).\
        filter(State.id == City.state_id).order_by(City.id).all()

    for city in cities:
        print("{}: ({}) {}".format(city[0], city[1], city[2]))
