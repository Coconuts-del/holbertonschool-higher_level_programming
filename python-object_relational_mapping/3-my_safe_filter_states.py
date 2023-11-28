#!/usr/bin/python3
"""
    script taking 4 arguments mysql username mysql, password, database name
    and state name searched
    display all values in the states table of hbtn_0e_0_usa where name
    matches the argument without SQL injection
    sorted by states_id asc using module MySQLdb
    connect on MySQL server running on localhost at port 3306
    code dont be executed when imported
"""
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("Usage : python script.py <username> <password> <database>"
                 " <state name searched>")

    """ connection to the database """
    db = MySQLdb.connect(host="localhost", port=3306, charset='utf8',
                         user=sys.argv[1], passwd=sys.argv[2],
                         database=sys.argv[3])

    """ create a cursor to execute sql command without SQL injection """
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = binary %s ORDER BY id",
              (sys.argv[4],))

    """ retrieve all the rows selected of the table states"""
    lines = c.fetchall()
    for line in lines:
        print(line)

    """  close the cursor and the connection """
    c.close()
    db.close()
