import requests
from github import Github

# GitHub Personal Access Token
TOKEN = "your_github_token"  # Replace with your actual token

# Initialize the GitHub client
g = Github(TOKEN)

def delete_artifacts(repo):
    # Get all workflow runs
    runs = repo.get_workflow_runs()
    
    for run in runs:
        # Get artifacts for each run
        artifacts = run.get_artifacts()
        
        for artifact in artifacts:
            print(f"Deleting artifact {artifact.name} from {repo.name}")
            
            # Delete the artifact
            url = f"https://api.github.com/repos/{repo.full_name}/actions/artifacts/{artifact.id}"
            headers = {
                "Authorization": f"token {TOKEN}",
                "Accept": "application/vnd.github.v3+json"
            }
            response = requests.delete(url, headers=headers)
            
            if response.status_code == 204:
                print(f"Successfully deleted artifact {artifact.name}")
            else:
                print(f"Failed to delete artifact {artifact.name}. Status code: {response.status_code}")

def main():
    # Get all repositories for the authenticated user
    for repo in g.get_user().get_repos():
        print(f"Processing repository: {repo.name}")
        delete_artifacts(repo)

if __name__ == "__main__":
    main()