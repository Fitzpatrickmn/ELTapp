import sqlite3
import json

# Load JSON data
with open('app/output_data/commits.json', 'r') as file:
    data = json.load(file)

# Connect to SQLite
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

cursor.execute('DROP TABLE IF EXISTS commits')

# Create table 
cursor.execute('''
    CREATE TABLE IF NOT EXISTS commits (
        commit_id VARCHAR PRIMARY KEY, 
        message STRING,
        url STRING, 
        comment_count INTEGER, 
        author_id INTEGER, 
        author_date TIMESTAMP, 
        committer_id INTEGER,
        commit_date TIMESTAMP
    )
''')

# Insert data into the table
for entry in data:
    cursor.execute('''
        INSERT INTO commits (commit_id, message, url, comment_count, author_id, author_date, committer_id, commit_date)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (entry['commit_id'], entry['message'], entry['url'], entry['comment_count'], entry['author_id'], entry['author_date'], entry['committer_id'], entry['commit_date']))

# Commit and close
conn.commit()

# Query the data
cursor.execute('SELECT COUNT(commit_id), COUNT (DISTINCT commit_ID) FROM commits')
rows = cursor.fetchall()

conn.close()

total_commits, unique_commits = rows[0]

print(f"### load_commits.py executed successfully. {total_commits} commits were loaded into the table, with {unique_commits} unique ids. ###")




