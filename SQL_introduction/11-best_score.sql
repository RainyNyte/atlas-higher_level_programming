-- lists all records from second_table where score is >= 10, displaying score and name, sorted by highest score

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;