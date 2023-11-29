#!/usr/bin/python3
"""Start link class to table in database"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine, insert
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2],
                                  sys.argv[3]), pool_pre_ping=True)
    """Base.metadata.create_all(engine)"""
    session = Session(engine)
    stmt = insert(State).values(name="Louisiana")
    conn = engine.connect()
    state = conn.execute(stmt)
    print(state.inserted_primary_key[0])

    session.close()
