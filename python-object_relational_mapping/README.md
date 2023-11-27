#Python - Object-relational mapping
### Description 
bridging the gap between Python and SQL using 
    the module "MySQLdb" to connect to a databas ande execute SQL queries 
    the module "SQLAlchemy"  as an introduction to Object Relational Mapping

### Provided files
   * [`0-select_states.sql`](./provided/0-select_states.sql)
### More info
####Install MySQLdb module version 2.0.x
For installing MySQLdb, you need to have MySQL installed.
```bash
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient==2.0.3
...
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info 
(2, 0, 3, 'final', 0)
```

####"Install SQLAlchemy module version 1.4.x
```bash
$ sudo pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.4.22'
```

you can ignore  this warning message:
```bash 
/usr/local/lib/python3.4/dist-packages/sqlalchemy/engine/default.py:552: Warning: (1681, "'@@SESSION.GTID_EXECUTED' is deprecated and will be re
moved in a future release.")                                                                                                        
cursor.execute(statement, parameters)  
```

## Tasks
### :white_check_mark: 0. Get all states
Write a script that lists all states from the database hbtn_0e_0_usa:
   * Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
   * You must use the module MySQLdb (import MySQLdb)
   * Your script should connect to a MySQL server running on localhost at port 3306
   * Results must be sorted in ascending order by states.id
   * Your code should not be executed when imported

   File(s): [`0-select_states.py`](./0-select_states.py)

### :white_check_mark: 1. Filter states
Write a script that lists all states with a name starting with N from the database hbtn_0e_0_usa:
   * Your script should take 3 arguments: mysql username, mysql password and database name (no argument validation needed)
   * You must use the module MySQLdb (import MySQLdb)
   * Your script should connect to a MySQL server running on localhost at port 3306
   * Results must be sorted in ascending order by states.id
   * Your code should not be executed when imported

   File(s): [`1-filter_states.py`](./1-filter_states.py)

### :white_check_mark: 2. Filter states by user input
Write a script that takes in an argument and displays all values in the states table of hbtn_0e_0_usa where name matches the argument.
   * Your script should take 4 arguments: mysql username, mysql password database name and state name searched)
   * You must use the module MySQLdb (import MySQLdb)
   * Your script should connect to a MySQL server running on localhost at port 3306
   * You must use format to create the SQL query with the user input
   * Results must be sorted in ascending order by states.id
   * Your code should not be executed when imported

   File(s): [`2-my_filter_states.py`](./2-my_filter_states.py)

### :white_check_mark: 3. SQL Injection... 
write a script that takes in arguments and displays all values in the states table of hbtn_0e_0_usa where name matches the argument. But this time, write one that is safe from MySQL injections!
   * Your script should take 4 arguments: mysql username, mysql password database name and state name searched)
   * You must use the module MySQLdb (import MySQLdb)
   * Your script should connect to a MySQL server running on localhost at port 3306
   * You must use format to create the SQL query with the user input
   * Results must be sorted in ascending order by states.id
   * Your code should not be executed when imported

   File(s): [`3-my_safe_filter_states.py`](./3-my_safe_filter_states.py)
