#!/usr/bin/python3
"""A module that takes in the name of a state as an argument and
   lists all cities of that state, using the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == '__main__':
    username, password, db_name, search_string = sys.argv[1:5]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name from cities \
                   WHERE cities.state_id IN \
                   (SELECT states.id FROM states \
                   WHERE states.name = '%s')" % (search_string))
    states = cursor.fetchall()

    result = ''
    for state in states:
        result += state[0] + ', '

    result = result[:-2]
    print(result)

    cursor.close()
    db.close()
