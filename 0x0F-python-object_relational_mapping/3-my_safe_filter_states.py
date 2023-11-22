#!/usr/bin/python3
""" 0x0F-python-object_relational_mapping """
import MySQLdb
import sys


if __name__ == "__main__":
    MY_HOST = "localhost"
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db = MySQLdb.connect(host=MY_HOST,
                         user=username,
                         passwd=password,
                         db=dbname)

    cur = db.cursor()

    cur.execute("SELECT * FROM states \
    WHERE states.name LIKE BINARY %s \
    ORDER BY states.id ASC", (sys.argv[4]))

    for row in cur.fetchall():
        print(row)

    db.close()
