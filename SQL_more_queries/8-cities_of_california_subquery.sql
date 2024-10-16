-- Lists all the cities where the state_id matches the id of California

SELECT name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;