-- lists the number of records with the same score
-- should display the score and number of records for the score
-- should be sorted by number of records(descending)

SELECT score, COUNT(*) AS number FROM second_table GROUP BY score
ORDER BY number DESC;
