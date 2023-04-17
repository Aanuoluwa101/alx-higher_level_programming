#!/usr/bin/python3
"""A module that lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    username, password, db_name = sys.argv[1:4]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute('SELECT cities.id, cities.name, states.name \
                   FROM states JOIN cities \
                   ON states.id=cities.state_id \
                   ORDER BY cities.id')
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
