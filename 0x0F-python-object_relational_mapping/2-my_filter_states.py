#!/usr/bin/python3
"""
Script that displays all values in the states table of hbtn_0e_0_usa where
name matches the argument
"""

import sys

import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create the SQL query using format to include the user input
    query = "SELECT * \
        FROM states \
            WHERE name = '{}' ORDER BY id ASC".format(state_name)

    # Execute the query to retrieve states with the matching name
    cursor.execute(query)

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
