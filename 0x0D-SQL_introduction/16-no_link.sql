-- Script that lists all records, sorted by descending score.
-- Rows without a name value are not listed.
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC; 
