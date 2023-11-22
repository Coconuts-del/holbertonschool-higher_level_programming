--  creates the table unique_id on your MySQL server 
--  database passed as an argument of mysql command 
--  don't failed if TABLE unique_id already exists 
CREATE TABLE IF NOT EXISTS unique_id(
   id INT DEFAULT 1 UNIQUE,
   name VARCHAR(256) 
);
