#!/usr/bin/python3
"""
Displays all values in the `states` table where the
`name` matches the user-specified argument, ensuring
the query is safe from SQL injections. The results
are sorted in ascending order by `states.id`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
	"""
	Fetches all states where the `name` matches the
	user input, using a parameterized query to prevent
	SQL injection. The results are ordered by `id`
	in ascending order and displayed in the
	format: (id, 'state_name').
	"""
	mysql_username = sys.argv[1]
	mysql_password = sys.argv[2]
	database_name = sys.argv[3]
	state_name_searched = sys.argv[4]
	db = MySQLdb.connect(
		host="localhost",
		port=3306,
		user=mysql_username,
		passwd=mysql_password,
		db=database_name
	)

	cursor = db.cursor()
	query = "SELECT id, name FROM states WHERE name = %s ORDER BY id ASC"
	cursor.execute(query, (state_name_searched,))
	states = cursor.fetchall()
	for state in states:
		print(f"({state[0]}, '{state[1]}')")

	cursor.close()
	db.close()
