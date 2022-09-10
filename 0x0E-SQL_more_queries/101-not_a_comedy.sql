-- lists all shows without the genre Comedy

SELECT tv_shows.title AS title FROM tv_shows WHERE tv_shows.id
NOT IN (SELECT tv_shows.id from tv_shows inner join tv_show_genres
ON tv_shows.id = tv_show_genres.show_id INNER JOIN tv_genres ON
tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = "Comedy")
ORDER BY tv_shows.title;
