import sqlite3

# Connect to SQLite database
conn = sqlite3.connect('main_dbt.db')
cursor = conn.cursor()

# Execute the query to get all table names
cursor.execute("DROP TABLE IF EXISTS agg_commits_users_by_month;")
cursor.execute("SELECT name FROM sqlite_master WHERE type = 'table';")

# Fetch all results
tables = cursor.fetchall()

# Print all table names
print('List of main_dbt tables:')
for table in tables:
    print(table[0])
