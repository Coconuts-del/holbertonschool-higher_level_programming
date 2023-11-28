#!/usr/bin/python3
"""
    prints the first State object from the database hbtn_0e_6_usa
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """ creating connection to the MySQL server """
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    """ creating session to interact with database """
    Session = sessionmaker(bind=engine)
    session = Session()
    """ display the first state"""
    for state in session.query(State).order_by(State.id)[0:1]:
        print("{}: {}".format(state.id, state.name))
    session.close()
