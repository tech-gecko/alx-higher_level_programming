-- Script that lists the number of records with the same score.
-- The list is sorted by the number of records (descending).
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score, number DESC;
