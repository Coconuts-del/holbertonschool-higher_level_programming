--  uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
--  using only 1 select and display tv.genres.name
--  sorted in ascending order by the genre name  
--  database name pass as an argument of mysql command 
SELECT tv_genres.name 
FROM tv_genres 
  JOIN tv_show_genres 
    ON tv_genres.id = tv_show_genres.genre_id
  JOIN tv_shows 
    ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = "Dexter" 
ORDER BY tv_genres.name;
