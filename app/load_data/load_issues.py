# load_issues.py

from db_utils import load_json_data, connect_to_db, create_table, insert_data, query_data, close_connection

# Load JSON data
data = load_json_data('app/output_data/issues.json')

# SQL statements
create_issues_table_sql = '''
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
'''

insert_issues_sql = '''
    INSERT INTO issues (issue_id, user_id, issue_number, title, state, created_at, updated_at, closed_at, url, comments, reactions)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
'''

query_issues_sql = 'SELECT COUNT(issue_id), COUNT(DISTINCT issue_id) FROM issues'

# Connect to SQLite and create table
conn, cursor = connect_to_db('main.db')
cursor.execute('DROP TABLE IF EXISTS issues')
create_table(cursor, create_issues_table_sql)

# Insert data into the table
insert_data(cursor, insert_issues_sql, [
    (
        entry['issue_id'], entry['user_id'], entry['issue_number'], entry['title'], 
        entry['state'], entry['created_at'], entry['updated_at'], entry['closed_at'], 
        entry['url'], entry['comments'], entry['reactions']
    )
    for entry in data
])

# Query and print results
rows = query_data(cursor, query_issues_sql)
close_connection(conn)

total_issues, unique_issues = rows[0]

print(f"### load_issues.py executed successfully. {total_issues} issues were loaded into the table, with {unique_issues} unique ids. ###")
