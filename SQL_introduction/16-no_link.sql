-- lists all records that have a non-Null name value sorted by highest score

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;