/*
    dbt model to aggregate issues and commits data by month.
*/



WITH commits_issues_agg_by_month as (
                    WITH agg_commits AS (
                    SELECT COUNT(*) AS commit_count, 
                        strftime('%Y-%m', date(commit_date)) AS month
                    FROM main."commits"
                    GROUP BY month
                    ), 
                    agg_issues AS (
                        SELECT COUNT(*) AS issue_count, 
                            strftime('%Y-%m', date(created_at)) AS month
                        FROM main."issues"
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
                    ORDER BY month
)

SELECT *
FROM commits_issues_agg_by_month