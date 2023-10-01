"""
Transforms and Loads data into the local SQLite3 database
"""
import sqlite3
import csv


# load the csv file and insert into a new sqlite3 database
def load(dataset="data/US_births_2000-2014_SSA.csv"):
    """Transforms and Loads data into the local SQLite3 database"""
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    # skips the header of csv
    next(payload)
    conn = sqlite3.connect("Birth.db") 
    # create a new db called Birth.db,
    # save it as a cursor/variable as conn
    c = conn.cursor() # use c to execute any actions
    c.execute("DROP TABLE IF EXISTS Birth")
    c.execute( # insert SQL queries to transform data (create/modify the table)
    # Create the structure of data--assign the column name 
    # and the type of data for this column
        """
        CREATE TABLE Birth (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Year INTEGER,
            Month INTEGER,
            Day_Of_Month INTEGER,
            Day_Of_Week INTEGER,
            Births INTEGER
        )
    """
    )
    # insert
    c.executemany( # extract each column from db and put it into the table structure 
        # Fill in the content of the data from the Birth db
        """
        INSERT INTO Birth (
            Year,
            Month,
            Day_Of_Month,
            Day_Of_Week,
            Births
            ) 
            VALUES (?, ?, ?, ?, ?)""", # have the number of "?" with values
        payload,
    )
    conn.commit()
    conn.close()
    return "Done transform and load"