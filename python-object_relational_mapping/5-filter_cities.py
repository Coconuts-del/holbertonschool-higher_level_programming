#!/usr/bin/python3
"""
    script taking 4 arguments mysql username mysql, password, database name
    and state name searched
    lists all cities of state name searched
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
    c.execute("SELECT cities.name FROM cities "
              "JOIN states ON cities.state_id = states.id "
              "WHERE states.name = binary %s ORDER BY cities.id", (sys.argv[4],))

    """ retrieve all the rows selected of the table cities """
    lines = c.fetchall()
    print(", ".join([line[0] for line in lines]))

    """  close the cursor and the connection """
    c.close()
    db.close()
