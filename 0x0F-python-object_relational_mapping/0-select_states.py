#!/usr/bin/python3
import MySQLdb
import sys

MY_HOST = "localhost:3306"
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
    print(f"({row[0]}, '{row[1]}')")

db.close()
