#!/usr/bin/python3
"""A module takes in an argument and displays all values in the
   states table of hbtn_0e_0_usa where name matches the argument"""
import sys
import MySQLdb

if __name__ == '__main__':
    username, password, db_name, search_string = sys.argv[1:5]
    db = MySQLdb.connect(host='localhost', user=username,
                         passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * from states \
                   WHERE name LIKE {} \
                   ORDER BY states.id".format(("'%" + search_string + "%'")))
    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
