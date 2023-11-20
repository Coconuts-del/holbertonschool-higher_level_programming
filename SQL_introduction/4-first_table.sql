-- creates a table called first_table in your MySQL server
-- dont fail if the table already exists
-- the database name will be passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS first_table (
id INT, 
name VARCHAR(256)); 
