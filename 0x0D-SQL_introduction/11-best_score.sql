-- Script that lists "score >= 10" records of the table "second_table".
-- Results contain "score" and "name" ordered by descending score.
SELECT score, name
FROM second_table
WHERE score>=10
ORDER BY score DESC;
