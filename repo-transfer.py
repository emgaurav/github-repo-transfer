import requests
import logging
import os

# Setup logging
logging.basicConfig(level=logging.INFO)

# Your GitHub personal access token with the required scopes, fetched from environment variables
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')

# Source and target organizations, fetched from environment variables
source_org = os.getenv('SOURCE_ORG')
target_org = os.getenv('TARGET_ORG')

# API URL
api_url = "https://api.github.com/repos"

# Create a session
session = requests.Session()
session.headers.update({
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json",
})

# Read the list of repositories from the file
with open('repos_to_transfer.txt', 'r') as file:
    repositories = [line.strip() for line in file]

# Transfer each repository
for repo in repositories:
    transfer_url = f"{api_url}/{source_org}/{repo}/transfer"
    data = {"new_owner": target_org, "team_ids": []}

    try:
        response = session.post(transfer_url, json=data)

        if response.ok:
            logging.info(f"Transfer initiated for {repo}")
        else:
            logging.error(f"Failed to initiate transfer for {repo}: {response.text}")

    except requests.RequestException as e:
        logging.error(f"Network error during transfer of {repo}: {e}")

# Close the session
session.close()
