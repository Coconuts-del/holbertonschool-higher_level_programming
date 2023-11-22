--  creates database hbtn_0d_usa and table states on your MySQL server 
--  don't failed if TABLE or DATABASE already exists 
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
   id INT AUTO_INCREMENT PRIMARY KEY,
   name VARCHAR(256) NOT NULL 
);
