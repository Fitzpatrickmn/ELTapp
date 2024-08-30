import sqlite3

# Connect to SQLite
conn = sqlite3.connect('main.db')
cursor = conn.cursor()

# Execute query to aggregate commits and issues by month 
cursor.execute('''
               WITH agg_commits AS (
                    SELECT COUNT(*) AS commit_count, 
                        strftime('%Y-%m', date(commit_date)) AS month
                    FROM commits
                    GROUP BY month
                    ), 
                    agg_issues AS (
                        SELECT COUNT(*) AS issue_count, 
                            strftime('%Y-%m', date(created_at)) AS month
                        FROM issues
                        GROUP BY month
                    )
               
                    SELECT
                        coalesce(ac.month, ai.month) AS month,
                        coalesce(ac.commit_count, 0) AS commit_count,
                        coalesce(ai.issue_count, 0) AS issue_count
                    FROM 
                        agg_commits ac 
                    LEFT JOIN 
                        agg_issues ai 
                    ON ac.month = ai.month
                    ORDER BY month;
                ''')

rows = cursor.fetchall()
for row in rows:
    print(row)

conn.close()


    