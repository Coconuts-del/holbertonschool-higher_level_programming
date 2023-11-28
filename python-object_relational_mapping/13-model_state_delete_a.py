#!/usr/bin/python3
"""
    deletes all State objects with a name containing the letter a
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
    """ retrives all state that contains a """
    del_state = session.query(State).filter(State.name.like('%a%'))

    """ delete all  """
    for state in del_state:
        session.delete(state)
    session.commit()
    session.close()
