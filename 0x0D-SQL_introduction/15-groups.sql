-- script that lists the number of records with the same score in second_table
-- The result should display: the score, the number of records
SELECT score, COUNT(score) AS "number" FROM second_table GROUP BY score ORDER BY score DESC;
