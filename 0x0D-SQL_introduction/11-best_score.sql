-- lists all records in second_table
-- results should display score and name(in this order)
-- where score >= 10 and should be ordered by score(top first)

SELECT score, name FROM second_table WHERE score >= 10
ORDER BY score DESC;
