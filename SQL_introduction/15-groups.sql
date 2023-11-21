-- lists the number of records with the same score in the table second_table of the 
-- database hbtn_0c_0 in your MySQL server.  
-- the result should display the score with the label number sorted by number of records.
-- The database name will be passed as an argument of the mysql command
SELECT score, count(score) as number FROM second_table 
GROUP BY score
ORDER BY number DESC;
