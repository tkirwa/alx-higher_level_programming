#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""

import sys

import MySQLdb

if __name__ == "__main__":
    # Get command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password)

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS {}".format(database))

    # Select the database
    cursor.execute("USE {}".format(database))

    # Create the 'states' table if it doesn't exist
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS states (id INT NOT NULL AUTO_INCREMENT, name VARCHAR(256) NOT NULL, PRIMARY KEY (id))"
    )

    # Insert sample data into the 'states' table
    cursor.execute(
        "INSERT INTO states (name) VALUES ('California'), ('Arizona'), ('Texas'), ('New York'), ('Nevada')"
    )

    # Execute the query to retrieve all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    states = cursor.fetchall()

    # Print the states
    for state in states:
        print(state)

    # Close cursor and database connection
    cursor.close()
    db.close()
