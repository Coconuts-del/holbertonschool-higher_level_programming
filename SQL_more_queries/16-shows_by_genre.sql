--  lists all shows, and all genres linked to that show,using only 1 select
--  sorted ascending order by the shows.title and genre name 
--  a show without genre display NULL
--  database name pass as an argument of mysql command 
SELECT tv_shows.title, tv_genres.name  
FROM tv_shows 
  LEFT JOIN tv_show_genres
    ON tv_shows.id = tv_show_genres.show_id 
  LEFT JOIN tv_genres
    ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name;
