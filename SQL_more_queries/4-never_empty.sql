--  creates the table id_not_null on your MySQL server 
--  database passed as an argument of mysql command 
--  don't failed if TABLE id_not_null already exists 
CREATE TABLE IF NOT EXISTS id_not_null(
   id INT DEFAULT 1,
   name VARCHAR(256) 
);
