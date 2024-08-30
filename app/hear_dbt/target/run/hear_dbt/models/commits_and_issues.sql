
  
    
    
    create  table main_schema."commits_and_issues"
    as
        

SELECT
    coalesce(ac.month, ai.month) AS month,
    coalesce(ac.commit_count, 0) AS commit_count,
    coalesce(ai.issue_count, 0) AS issue_count
FROM 
    main_schema."agg_commits" ac 
LEFT JOIN 
    main_schema."agg_issues" ai 
ON ac.month = ai.month
ORDER BY month;

  