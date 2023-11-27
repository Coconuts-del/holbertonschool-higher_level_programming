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
