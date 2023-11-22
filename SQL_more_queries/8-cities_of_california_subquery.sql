--  lists all the cities of California in database hbtn_0d_usa 
--  without using JOIN and sorted ascending order by cities.id 
--  database name pass as an argument of mysql command 
SELECT id, name FROM cities 
WHERE state_id IN (SELECT id FROM states WHERE name = "California")  
ORDER BY id;
