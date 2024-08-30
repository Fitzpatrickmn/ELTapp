import sqlite3

# Connect to SQLite
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

# Execute query to aggregate commits and issues by user
cursor.execute('''
            WITH agg_commits AS(
               SELECT COUNT(*) as commit_count, 
               committer_id
            FROM commits
            GROUP BY committer_id
            ), 
               
            agg_issues AS(
               SELECT COUNT(*) as issue_count, 
               user_id
            FROM issues
            GROUP BY user_id
            )
               
            SELECT 
            u.user_id, 
            u.user_name, 
            u.user_email, 
            COALESCE(ac.commit_count, 0) as commit_count, 
            COALESCE(ai.issue_count, 0) as issue_count
            FROM 
            users u
            LEFT JOIN 
            agg_commits ac ON u.user_id = ac.committer_id
            LEFT JOIN 
            agg_issues ai ON u.user_id = ai.user_id; 
            ''')

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()