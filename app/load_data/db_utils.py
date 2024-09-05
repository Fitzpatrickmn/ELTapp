# db_utils.py

import sqlite3
import json

def load_json_data(file_path):
    """Loads JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def connect_to_db(db_name):
    """Connects to the SQLite database and returns the connection and cursor."""
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    return conn, cursor

def create_table(cursor, create_table_sql):
    """Creates a table based on the provided SQL statement."""
    cursor.execute(create_table_sql)

def insert_data(cursor, insert_sql, data):
    """Inserts data into the table."""
    for entry in data:
        cursor.execute(insert_sql, entry)

def query_data(cursor, query_sql):
    """Executes a query and returns the result."""
    cursor.execute(query_sql)
    return cursor.fetchall()

def close_connection(conn):
    """Commits and closes the database connection."""
    conn.commit()
    conn.close()
