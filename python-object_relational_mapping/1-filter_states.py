#!/usr/bin/python3

"""
Lists all states with a name starting with
'N'  from the `states` table, sorted in
ascending order by their id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
	"""
	Fetches all states with names starting with 'N' from
	the `states` table in ascending order by `id`. The
	results are displayed in the format: (id, 'state_name').
	"""
	mysql_username = sys.argv[1]
	mysql_password = sys.argv[2]
	database_name = sys.argv[3]
	db = MySQLdb.connect(
		host="localhost",
		port=3306,
		user=mysql_username,
		passwd=mysql_password,
		db=database_name
	)

	cursor = db.cursor()
	cursor.execute("SELECT id, name FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
	states = cursor.fetchall()
	for state in states:
		print(f"({state[0]}, '{state[1]}')")

	cursor.close()
	db.close()
