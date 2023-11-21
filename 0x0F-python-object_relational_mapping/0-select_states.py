#!/usr/bin/python3
import MySQLdb
import sys

MY_HOST = "localhost"
MY_USER = sys.argv[1]
MY_PASS = sys.argv[2]
MY_DB = sys.argv[3]

db = MySQLdb.connect(host=MY_HOST,    # your host, usually localhost
                     user=MY_USER,         # your username
                     passwd=MY_PASS,  # your password
                     db=MY_DB)        # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM states")

# print all the first cell of all the rows
for row in cur.fetchall():
    print(f"({row[0]}, '{row[1]}')")

db.close()
