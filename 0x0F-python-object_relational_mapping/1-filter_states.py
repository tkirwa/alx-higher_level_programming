#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from
 the database hbtn_0e_0_usa
"""

import sys

import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost", port=3306, user=username, passwd=password, db=db
    )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the query to retrieve states with a name starting with 'N'
    cursor.execute("SELECT * FROM `states` ORDER BY `id`")

    # Fetch all the rows returned by the query
    # states = cursor.fetchall()

    # Print the states

    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]

    # Close cursor and database connection
    cursor.close()
    db.close()
