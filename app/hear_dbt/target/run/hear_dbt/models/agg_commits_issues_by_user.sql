
  
    
    
    create  table main_dbt."agg_commits_issues_by_user"
    as
        /*
    dbt model to aggregate issues and commits data by user.
*/



WITH commits_issues_agg_by_user as (
                    WITH agg_commits AS(
                    SELECT COUNT(*) as commit_count, 
                    committer_id
                    FROM main."commits"
                    GROUP BY committer_id
                    ), 
                    agg_issues AS(
                    SELECT COUNT(*) as issue_count, 
                    user_id
                    FROM main."issues"
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
                    agg_issues ai ON u.user_id = ai.user_id
)

SELECT *
FROM commits_issues_agg_by_user

  