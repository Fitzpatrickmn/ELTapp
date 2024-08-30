import requests
import json

import requests

# Define the owner & repository variables
owner = 'psf'
repository = 'requests'

# Construct GitHub API URL to fetch issues data
url = f'https://api.github.com/repos/{owner}/{repository}/issues'

# Create get request
issues_response = requests.get(url)

# Check if the request was successful and store data
if issues_response.status_code == 200:
    issues = issues_response.json()
    
    issue_data = []
    for issue in issues:
        issue_info = {
            'issue_id': issue['id'],
            'user_id': issue['user']['id'],
            'issue_number': issue['number'],
            'title': issue['title'],
            'state': issue['state'],
            'created_at': issue['created_at'],
            'updated_at': issue['updated_at'],
            'closed_at': issue['closed_at'],
            'url': issue['html_url'],
            'comments': issue['comments'],
            'reactions': issue['reactions']['total_count']
        }
        
        issue_data.append(issue_info)

# Convert collected data into a JSON string
issue_json = json.dumps(issue_data, indent=4)

# Write the output JSON into to a file
with open('app/output_data/issues.json', 'w') as file:
    file.write(issue_json)

