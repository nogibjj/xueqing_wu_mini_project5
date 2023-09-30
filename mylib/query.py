"""Query the database"""

import sqlite3

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")


def general_query(query):
    """runs a query a user inputs"""
    # Connect to the SQLite database
    conn = sqlite3.connect("Birth.db")

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Execute the query
    cursor.execute(query)

    # If the query modifies the database, commit the changes
    if (
        query.strip().lower().startswith("insert")
        or query.strip().lower().startswith("update")
        or query.strip().lower().startswith("delete")
    ):
        conn.commit()

    # Close the cursor and connection
    cursor.close()
    conn.close()

    log_query(f"{query}")


def create_record(
    Year, Month, Day_Of_Month, Day_Of_Week,Births
):
    """create example query"""
    conn = sqlite3.connect("Birth.db")
    c = conn.cursor()
    c.execute(
        """
        INSERT INTO Birth 
        (Year,
        Month,
        Day_Of_Month,
        Day_Of_Week,
        Births) 
        VALUES (?, ?, ?, ?, ?)
        """,
        (Year, Month, Day_Of_Month, Day_Of_Week, Births),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""INSERT INTO ServeTimesDB VALUES (
            {Year}, 
            {Month}, 
            {Day_Of_Month}, 
            {Day_Of_Week}, 
            {Births}
            );"""
    )


def update_record(
    id, Year, Month, Day_Of_Month, Day_Of_Week, Births
):
    """update example query"""
    conn = sqlite3.connect("Birth.db")
    c = conn.cursor()
    c.execute(
        """
        UPDATE Birth 
        SET Year=?, 
        Month=?, 
        Day_Of_Month=?, 
        Day_Of_Week=?, 
        Births=?
        WHERE id=?
        """,
        (Year, Month, Day_Of_Month, Day_Of_Week,Births, id),
    )
    conn.commit()
    conn.close()

    # Log the query
    log_query(
        f"""UPDATE Birth SET 
        Year={Year}, 
        Month={Month},
        Day_Of_Month={Day_Of_Month},
        Day_Of_Week={Day_Of_Week}, 
        Births={Births}, 
        WHERE id={id};"""
    )


def delete_record(record_id):
    """delete example query"""
    conn = sqlite3.connect("Birth.db")
    c = conn.cursor()
    c.execute("DELETE FROM Birth WHERE id=?", (record_id,))
    conn.commit()
    conn.close()

    # Log the query
    log_query(f"DELETE FROM Birth WHERE id={record_id};")


def read_data():
    """read data"""
    conn = sqlite3.connect("Birth.db")
    c = conn.cursor()
    c.execute("SELECT * FROM Birth")
    data = c.fetchall()
    log_query("SELECT * FROM Birth;")
    return data


