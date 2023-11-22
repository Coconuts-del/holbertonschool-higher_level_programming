--  lists all genres from database hbtn_0d_tvshows 
--  and display the number of shows linked to each  using only 1 select
--  sorted descending order by number of shows linked  
--  database name pass as an argument of mysql command 
SELECT tv_genres.name as genre, count(*) as number_of_shows 
  FROM tv_genres 
  JOIN tv_show_genres
  ON tv_genres.id = tv_show_genres.genre_id 
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
