#!/usr/bin/python3
"""
    script taking 3 arguments mysql username mysql password database name
    lists all states whith name startin with N from the database hbtn_0e_0_usa
    sorted by states_id asc
    using module MySQLdbconnect and server running on localhost at port 3306
    code dont be executed when imported
"""
import sys
import MySQLdb

if __name__ != "__main__":
    sys.exit(0)
if len(sys.argv) != 5:
    print("Usage : python script.py <username> <password> <database>"
          " <state name searched>")
    sys.exit(1)

""" connection to the database """
db = MySQLdb.connect(host="localhost", port=3306, charset='utf8',
                     user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3]
                     )

""" create a cursor to execute sql command without SQL injection """
c = db.cursor()
c.execute("SELECT * FROM states WHERE name like binary %s ORDER BY id",
          (sys.argv[4],))

""" retrieve all the rows selected of the table states"""
states = c.fetchall()
for state in states:
    print(state)

"""  close the cursor and the connection """
c.close()
db.close()
