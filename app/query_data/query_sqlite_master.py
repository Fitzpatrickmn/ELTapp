import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('main_dbt.db')
cursor = conn.cursor()

# Execute the query to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")

# Fetch all results
tables = cursor.fetchall()

# Print all table names
for table in tables:
    print(table[0])
