#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where
name matches the argument (safe from SQL injection)
"""

import MySQLdb
import sys

if __name__ == '__main__':
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=username,
                         passwd=password,
                         db=database)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create the SQL query with a placeholder for the state name
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

    # Execute the query with the state name as a parameter
    cursor.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
