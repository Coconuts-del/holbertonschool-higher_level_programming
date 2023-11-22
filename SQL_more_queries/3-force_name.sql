--  creates the table force_name on your MySQL serve 
--  database passed as an argument of mysql command 
--  don't failed if TABLE force_name already exists 
CREATE TABLE IF NOT EXISTS force_name(
   id INT,
   name VARCHAR(256) NOT NULL
);
