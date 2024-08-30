import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

# Execute the query to get all table names
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")

# Fetch all results
tables = cursor.fetchall()

# Print all table names
print('List of main tables:')
for table in tables:
    print(table[0])
