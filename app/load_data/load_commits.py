from db_utils import load_json_data, connect_to_db, create_table, insert_data, query_data, close_connection

# Load JSON data
data = load_json_data('app/output_data/commits.json')

# SQL statements
create_commits_table_sql = '''
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
'''

insert_commits_sql = '''
    INSERT INTO commits (commit_id, message, url, comment_count, author_id, author_date, committer_id, commit_date)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
'''

query_commits_sql = 'SELECT COUNT(commit_id), COUNT(DISTINCT commit_id) FROM commits'

# Connect to SQLite and create table
conn, cursor = connect_to_db('main.db')
cursor.execute('DROP TABLE IF EXISTS commits')
create_table(cursor, create_commits_table_sql)

# Insert data into the table
insert_data(cursor, insert_commits_sql, [
    (
        entry['commit_id'], entry['message'], entry['url'], entry['comment_count'], 
        entry['author_id'], entry['author_date'], entry['committer_id'], entry['commit_date']
    )
    for entry in data
])

# Query and print results
rows = query_data(cursor, query_commits_sql)
close_connection(conn)

total_commits, unique_commits = rows[0]

print(f"### load_commits.py executed successfully. {total_commits} commits were loaded into the table, with {unique_commits} unique ids. ###")
