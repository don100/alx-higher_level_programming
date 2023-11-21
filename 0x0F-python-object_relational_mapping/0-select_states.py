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
    
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    
    for row in cur.fetchall():
        print(row)
    
    db.close()
