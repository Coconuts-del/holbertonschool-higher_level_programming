#!/usr/bin/python3
"""
    script taking 3 arguments mysql username, mysql password, database name
    lists all cities from the database hbtn_0e_4_usa by states.name
    sorted by citie_id asc using only 1 execute
    using module MySQLdb connect and server running on localhost at port 3306
    code dont be executed when imported
"""
import sys
import MySQLdb

if __name__ != "__main__":
    sys.exit(0)
if len(sys.argv) != 4:
    print("Usage : python script.py <username> <password> <database>")
    sys.exit(1)

""" connection to the database """
db = MySQLdb.connect(host="localhost", port=3306, charset='utf8',
                     user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3]
                     )

""" create a cursor to execute sql command """
c = db.cursor()
c.execute("SELECT cities.id, cities.name, states.name FROM cities "
          "JOIN states ON cities.state_id = states.id")


""" list all cities by state """
cities = c.fetchall()
for citie in cities:
    print(citie)

"""  close the cursor and the connection """
c.close()
db.close()
