--  lists all records with a score >= 10 in the table second_table of 
--  the database hbtn_0c_0 in your MySQL server.
--  Result ordered by score display score and name.
-- The database name will be passed as an argument of the mysql command
SELECT score,name FROM second_table WHERE score >= 10
ORDER BY SCORE DESC;
