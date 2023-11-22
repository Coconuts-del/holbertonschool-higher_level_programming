--  creates database hbtn_0d_usa and table states on your MySQL server 
--  don't failed if TABLE or DATABASE already exists 
--  id:primary key auto generated  state_id:foreign key states id
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
   id INT AUTO_INCREMENT PRIMARY KEY,
   state_id INT NOT NULL, 
   name VARCHAR(256) NOT NULL, 
   FOREIGN KEY(state_id) REFERENCES states(id)
);
