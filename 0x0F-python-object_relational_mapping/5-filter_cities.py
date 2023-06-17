#!/usr/bin/python3
"""
Script that lists all cities of a given state from the database hbtn_0e_4_usa
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

    # Execute the query to retrieve cities of the given state
    cursor.execute("SELECT cities.name \
                    FROM cities JOIN states \
                    ON cities.state_id = states.id \
                    WHERE states.name = %s \
                    ORDER BY cities.id ASC", (state_name,))

    # Fetch all the rows returned by the query
    cities = cursor.fetchall()

    # Print the cities
    if cities:
        print(", ".join(city[0] for city in cities))

    # Close cursor and database connection
    cursor.close()
    db.close()
