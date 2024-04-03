#!/usr/bin/python3
"""
Script lists all states with name starting with N from database hbtn_0e_0_usa
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]

        db = MySQLdb.connect(user=username, passwd=password,
                             db=database, port=3306)
        cursor = db.cursor()
        cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()
