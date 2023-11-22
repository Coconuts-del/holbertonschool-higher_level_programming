--  lists all Comedy shows in the database hbtn_0d_tvshows
--  using only 1 select and display tv_shows.title 
--  sorted in ascending order by the show title  
--  database name pass as an argument of mysql command 
SELECT tv_shows.title 
FROM tv_shows 
  JOIN tv_show_genres 
    ON tv_shows.id = tv_show_genres.show_id
  JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
    WHERE tv_genres.name = "Comedy" 
ORDER BY tv_shows.title;
