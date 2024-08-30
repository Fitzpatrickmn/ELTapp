import sqlite3
import json

# Load JSON data
with open('app/output_data/issues.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS issues')

# Create table 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS issues (
        issue_id INTEGER PRIMARY KEY, 
        user_id INTEGER,
        issue_number INTEGER, 
        title STRING, 
        state VARCHAR, 
        created_at TIMESTAMP, 
        updated_at TIMESTAMP, 
        closed_at TIMESTAMP, 
        url STRING,
        comments INTEGER, 
        reactions INTEGER
    )
''')

# Insert data into the table
for entry in data:
    cursor.execute('''
        INSERT INTO issues (issue_id, user_id, issue_number, title, state, created_at, updated_at, closed_at, url, comments, reactions)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (entry['issue_id'], entry['user_id'], entry['issue_number'], entry['title'], entry['state'], entry['created_at'], entry['updated_at'], entry['closed_at'], entry['url'], entry['comments'], entry['reactions']))

# Commit and close
conn.commit()

# Query the data
cursor.execute('SELECT COUNT(issue_id), COUNT (DISTINCT issue_id) FROM issues')
rows = cursor.fetchall()

conn.close()

total_issues, unique_issues = rows[0]

print(f"### load_issues.py executed successfully. {total_issues} issues were loaded into the table, with {unique_issues} unique ids. ###")




