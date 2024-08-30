

SELECT COUNT(*) AS commit_count, 
       strftime('%Y-%m', date(commit_date)) AS month
FROM main."commits"
GROUP BY month;