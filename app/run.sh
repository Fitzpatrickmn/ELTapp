# Extract Data from the API
python3 app/extract_data/download_commits_data.py
python3 app/extract_data/download_issues_data.py

# Load the Extracted Data into a SQLite Database
python3 app/load_data/load_commits.py
python3 app/load_data/load_issues.py
python3 app/load_data/load_users.py

# cd into the dbt Directory 
cd app/hear_dbt

# Run dbt
dbt debug
dbt run