
  
    
    
    create  table main_schema."agg_issues"
    as
        

SELECT COUNT(*) AS issue_count, 
       strftime('%Y-%m', date(created_at)) AS month
FROM main."issues"
GROUP BY month;

  