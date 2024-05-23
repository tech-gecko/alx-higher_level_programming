-- SQL script that displays the top 3 of cities temperature
-- during July and August ordered by temperature (descending).
SELECT city, MAX(CASE WHEN month IN (7, 8) THEN value END) AS avg_temp
FROM temperatures
GROUP BY city
ORDER BY avg_temp DESC
LIMIT 3;