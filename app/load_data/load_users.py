from db_utils import load_json_data, connect_to_db, create_table, insert_data, query_data, close_connection


# Load JSON data
data = load_json_data('app/output_data/users.json')

# Create table 
create_users_table_sql = '''
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER, 
        user_name STRING,
        user_login STRING,
        user_email STRING
    )
'''

# Insert data into the table
insert_users_sql = '''
        INSERT INTO users (user_id, user_name, user_login, user_email)
        VALUES (?, ?, ?, ?)
    '''

query_users_sql = 'SELECT COUNT(user_id), COUNT (DISTINCT user_id) FROM users'

# Connect to SQLite and create table
conn, cursor = connect_to_db('main.db')
cursor.execute('DROP TABLE IF EXISTS users')
create_table(cursor, create_users_table_sql)

# Insert data into the table
insert_data(cursor, insert_users_sql, [
    (
        entry['user_id'], entry['user_name'], entry['user_login'], entry['user_email']
    )
    for entry in data
])

# Query and print results
rows = query_data(cursor, query_users_sql)
close_connection(conn)

total_users, unique_users = rows[0]

print(f"### load_users.py executed successfully. {total_users} users were loaded into the table, with {unique_users} unique ids. ###")
