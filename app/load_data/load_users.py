import sqlite3
import json

# Load JSON data
with open('app/output_data/users.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS users')

# Create table 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER, 
        user_name STRING,
        user_login STRING,
        user_email STRING
    )
''')

# Insert data into the table
for entry in data:
    cursor.execute('''
        INSERT INTO users (user_id, user_name, user_login, user_email)
        VALUES (?, ?, ?, ?)
    ''', (entry['user_id'], entry['user_name'], entry['user_login'], entry['user_email']))

# Commit and close
conn.commit()

# Query the data
cursor.execute('SELECT COUNT(user_id), COUNT (DISTINCT user_id) FROM users')
rows = cursor.fetchall()

conn.close()

total_users, unique_users = rows[0]

print(f"### load_users.py executed successfully. {total_users} users were loaded into the table, with {unique_users} unique ids. ###")



