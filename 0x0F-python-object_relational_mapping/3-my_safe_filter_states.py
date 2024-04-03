#!/usr/bin/python3
"""
Values in states tbl of db where name matches arg (safe from MySQL injection)
"""

import MySQLdb
import sys

if __name__ == "__main__":
    if len(sys.argv) == 5:
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        db = MySQLdb.connect(user=username, passwd=password,
                             db=database, port=3306)
        cursor = db.cursor()
        query = "SELECT * FROM states WHERE name=%s ORDER BY id"
        cursor.execute(query, (state_name,))
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        cursor.close()
        db.close()
