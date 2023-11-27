#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    """Base.metadata.create_all(engine)"""
    session = Session(engine)
    count = session.query(State).join(
    ).filter(
        State.name.like(
            sys.argv[4])).count()
    if count:
        print("{}".format(count))
    else:
        print('Not found')
    session.close()
