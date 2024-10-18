#!/usr/bin/python3
"""
Displays all values in the `states` table where
the `name` matches the user-specified argument.
The results are sorted in ascending order
by `states.id`.
"""

import MySQLdb
import sys

if __name__ == "__main__":
	"""
	Fetches all states where the `name` matches
	the user input from the `states` table, ordered
	by `id` in ascending order. The results are
	displayed in the format: (id, 'state_name').
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
	query = "SELECT id, name FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name_searched)
	cursor.execute(query)
	states = cursor.fetchall()
	for state in states:
		print(f"({state[0]}, '{state[1]}')")

	cursor.close()
	db.close()
