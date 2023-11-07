# Github-repo-transfer
#### A GitHub Repository Transfer Automation Script

## Description
This script facilitates the automated transfer of multiple repositories from one GitHub organization to another. It is designed to read a list of repository names from a text file and use the GitHub API to perform the transfers efficiently. Ideal for scenarios involving organizational restructuring, repository archival, or consolidation processes.

## Features
- Bulk repository transfer between GitHub organizations
- Reads target repositories from a plaintext file
- Utilizes GitHub API for transfer operations
- Streamlines the migration process for GitHub repositories

## Prerequisites
- GitHub personal access token with admin permissions on both source and target organizations
- List of repositories in `repos_to_transfer.txt` file
- Admin rights for the user associated with the access token

## Usage
1. Clone the repository.
2. Install necessary dependencies.
3. Place your repository names in `repos_to_transfer.txt`.
4. Set up your environment with the required GitHub personal access token.
5. Run the script to initiate the transfers.

Refer to the in-script comments for detailed setup and execution instructions.

## GitHub API Reference
For complete API details and repository transfer requirements, visit the [GitHub documentation on transferring a repository](https://docs.github.com/en/rest/repos/repos#transfer-a-repository).
