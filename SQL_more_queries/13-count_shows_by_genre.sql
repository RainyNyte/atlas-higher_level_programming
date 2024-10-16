-- show the number of tv shows linked to each genre in hbtn_0d_tvshows

SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS genre FROM tv_genres Join tv_show_genres ON tv_genres.id = tv_show_genres.genre_id GROUP BY tv_genres.name HAVING number_of_shows > 0 ORDER BY DESC;