import requests
import json

# Define owner & repository variables
owner = 'psf'
repository = 'requests'

# Construct GitHub API URL to fetch commits data
url = f'https://api.github.com/repos/{owner}/{repository}/commits'

# Create get request
commits_response = requests.get(url)

# Check if the request was successful and store data
if commits_response.status_code == 200:
    commits = commits_response.json()  

    commit_data = []
    user_data = []
    user_ids = set()

    for commit in commits:
        commit_info = {
            'commit_id' : commit['sha'],
            'message' : commit['commit']['message'],
            'url' : commit['url'],
            'comment_count': commit['commit']['comment_count'], 
            'author_id' : commit['author']['id'], 
            'author_date' : commit['commit']['author']['date'],
            'committer_id' : commit['committer']['id'], 
            'commit_date' : commit['commit']['committer']['date']
            }
        
        author_info = {
            'user_id' : commit['author']['id'],
            'user_name': commit['commit']['author']['name'],
            'user_login' : commit['author']['login'],
            'user_email' : commit['commit']['author']['email'], 
            }
        
        committer_info ={
            'user_id' : commit['committer']['id'], 
            'user_name' : commit['commit']['committer']['name'],
            'user_login' : commit['committer']['login'],
            'user_email' : commit['commit']['committer']['email']}
        
        # Append commit
        commit_data.append(commit_info)
        
        # Add unique users to author and committer data stores
        if author_info['user_id'] not in user_ids:
            user_data.append(author_info)
            user_ids.add(author_info['user_id'])

        if committer_info['user_id'] not in user_ids:
            user_data.append(committer_info)
            user_ids.add(committer_info['user_id'])
        
        
else:
    print(f"Failed to retrieve commits: {commits_response.status_code}")


# Convert collected data into JSON strings
commit_json = json.dumps(commit_data, indent=4)

user_json = json.dumps(user_data, indent=4)

# Write the output JSON into to a file
with open('app/output_data/commits.json', 'w') as file:
    file.write(commit_json)

with open('app/output_data/users.json', 'w') as file: 
    file.write(user_json)