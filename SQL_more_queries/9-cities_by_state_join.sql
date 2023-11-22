--  lists all the cities  in database hbtn_0d_usa 
--  using JOIN and sorted ascending order by cities.id 
--  database name pass as an argument of mysql command 
SELECT cities.id, cities.name, states.name 
FROM cities 
JOIN states   
ON (cities.state_id = states.id)
ORDER BY cities.id;
