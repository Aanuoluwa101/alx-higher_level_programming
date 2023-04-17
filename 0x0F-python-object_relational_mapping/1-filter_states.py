#!/usr/bin/python3
"""A module  lists all states with a name starting
   with N (upper N) from the database hbtn_0e_0_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    username, password, db_name = sys.argv[1:4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * from states \
                   WHERE name LIKE 'N%' \
                   ORDER BY states.id")
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
