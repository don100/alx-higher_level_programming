#!/usr/bin/python3
""" 0x0F-python-object_relational_mapping """
import MySQLdb
import sys


if __name__ == "__main__":
    MY_HOST = "localhost"
    username = sys.argv[1]
    password = sys.argv[2]
    name = sys.argv[3]

    db = MySQLdb.connect(host=MY_HOST,
                         user=username,
                         passwd=password,
                         db=name)

    cur = db.cursor()

    cur.execute("SELECT cities.name \
    FROM cities \
    LEFT JOIN states \
    ON cities.state_id=states.id \
    WHERE states.name LIKE BINARY '%s' \
    ORDER BY cities.id ASC" % (sys.argv[4], ))

    print(', '.join(''.join(i) for i in cur.fetchall()))

    db.close()
