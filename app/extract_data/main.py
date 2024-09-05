from extract_data_functions import fetch_data, extract_commits, extract_issues, write_json_file

def main():
    owner = "psf" 
    repository = "requests" 

    # Fetch commits
    commits = fetch_data(owner, repository, "commits")
    if commits:
        # Extract commit and user data
        commit_data, user_data = extract_commits(commits)
        
        # Write commit and user data to JSON files
        write_json_file("commits.json", commit_data)
        write_json_file("users.json", user_data)

    # Fetch issues
    issues = fetch_data(owner, repository, "issues")
    if issues:
        # Extract issue data
        issue_data = extract_issues(issues)
        
        # Write issue data to a JSON file
        write_json_file("issues.json", issue_data)

    print("### Main Data Extraction Script Ran Successfully ###")

if __name__ == "__main__":
    main()
