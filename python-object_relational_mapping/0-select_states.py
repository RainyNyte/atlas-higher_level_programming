#!/usr/bin/python3

"""
This module connects to a MySQL database and lists all states
from the `states` table in ascending order by their id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
	"""
	Retrieves MySQL credentials and database name from command-line arguments,
	connects to the database, and fetches all states from the `states` table in ascending order.
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
	cursor.execute("SELECT * FROM states ORDER BY id ASC")
	states = cursor.fetchall()
	for state in states:
		print(f"({state[0]}, '{state[1]}')")

	cursor.close()
	db.close()
 