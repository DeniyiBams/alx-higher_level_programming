-- displays top 3 cities temperature during july and august ordered by temperature(descending)

SELECT city, AVG(value) AS avg_temp FROM temperatures 
WHERE month IN (7, 8) GROUP BY city ORDER BY avg_temp DESC
LIMIT 3;
