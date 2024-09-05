import requests
import json

def fetch_data(owner, repository, data_type):
    """Fetch data from a GitHub repository for a given type (commits, issues, etc.)."""
    url = f'https://api.github.com/repos/{owner}/{repository}/{data_type}'
    response = requests.get(url)
    if response.status_code == 200:
        # Return the parsed JSON data
        return response.json()
    else:
        print(f"Failed to retrieve {data_type}: {response.status_code}")
        return None
    
def extract_commits(commits):
    commit_data = []
    user_data = []
    user_ids = set()

    for commit in commits:
        commit_info = {
            'commit_id': commit.get('sha', None),
            'message': commit.get('commit', {}).get('message', None),
            'url': commit.get('url', None),
            'comment_count': commit.get('commit', {}).get('comment_count', None),
            'author_id': commit.get('author', {}).get('id', None),
            'author_date': commit.get('commit', {}).get('author', {}).get('date', None),
            'committer_id': commit.get('committer', {}).get('id', None),
            'commit_date': commit.get('commit', {}).get('committer', {}).get('date', None)
        }

        author_info = {
            'user_id': commit.get('author', {}).get('id', None),
            'user_name': commit.get('commit', {}).get('author', {}).get('name', None),
            'user_login': commit.get('author', {}).get('login', None),
            'user_email': commit.get('commit', {}).get('author', {}).get('email', None)
        }

        committer_info = {
            'user_id': commit.get('committer', {}).get('id', None),
            'user_name': commit.get('commit', {}).get('committer', {}).get('name', None),
            'user_login': commit.get('committer', {}).get('login', None),
            'user_email': commit.get('commit', {}).get('committer', {}).get('email', None)
        }

        # Append commit
        commit_data.append(commit_info)
        
        # Add unique users to author and committer data stores
        if author_info['user_id'] not in user_ids:
            user_data.append(author_info)
            user_ids.add(author_info['user_id'])

        if committer_info['user_id'] not in user_ids:
            user_data.append(committer_info)
            user_ids.add(committer_info['user_id'])

    # Return the extracted data
    return commit_data, user_data

def extract_issues(issues):
    issue_data = []
    
    for issue in issues:
        issue_info = {
            'issue_id': issue.get('id', None),
            'user_id': issue.get('user', {}).get('id', None),
            'issue_number': issue.get('number', None),
            'title': issue.get('title', None),
            'state': issue.get('state', None),
            'created_at': issue.get('created_at', None),
            'updated_at': issue.get('updated_at', None),
            'closed_at': issue.get('closed_at', None),
            'url': issue.get('html_url', None),
            'comments': issue.get('comments', None),
            'reactions': issue.get('reactions', {}).get('total_count', None)
        }

        issue_data.append(issue_info)  

    return issue_data 

def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
