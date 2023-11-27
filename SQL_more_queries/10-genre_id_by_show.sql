--  lists all the shows in database hbtn_0d_tvshows using only 1 select
--  sorted ascending order by tv_shows.title and tv_show_genres.genre_id 
--  database name pass as an argument of mysql command 
SELECT tv_shows.title, tv_show_genres.genre_id  
FROM tv_shows 
JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title, tv_show_genres.genre_id;