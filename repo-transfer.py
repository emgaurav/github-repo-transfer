import requests

# Your GitHub personal access token with the required scopes
GITHUB_TOKEN = '<github_token_goes_here>'

# Headers for authentication
headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
}

# Source and target organizations
source_org = '<source-org>'
target_org = '<target-org>'

# API URL
api_url = "https://api.github.com/repos"

# Read the list of repositories from the file
with open('repos_to_transfer.txt', 'r') as file:
    repositories = [line.strip() for line in file]

# Transfer each repository
for repo in repositories:
    # Set up the API endpoint
    transfer_url = f"{api_url}/{source_org}/{repo}/transfer"

    # Set up the data payload
    data = {
        "new_owner": target_org,
        "team_ids": []  # Specify team IDs if required
    }

    # Make the POST request to transfer the repository
    response = requests.post(transfer_url, headers=headers, json=data)

    # Check if the transfer was successful
    if response.status_code == 202:
        print(f"Transfer initiated for {repo}")
    else:
        print(f"Failed to initiate transfer for {repo}: {response.content}")

# End of the script
