
GitHub Auto-Committer 🤖

This project provides a Python script that automatically creates and pushes commits to a GitHub repository on a schedule. It's designed to help users maintain a consistent commit streak for personal motivation or to automate updates to a log file.

The script can be run in two ways:

Locally: Using your computer's scheduler (like Cron on Linux/macOS or Task Scheduler on Windows). This requires your computer to be on at the scheduled time.

Cloud-based: Using GitHub Actions, which runs automatically in the cloud, even when your computer is offline. This is the recommended method.

Features
Automated Commits: Runs on a schedule to ensure consistent activity.

Customizable: Easily configure the repository path, commit message, and file to be modified.

Timestamped Changes: Each commit makes a small, unique change by adding a timestamp to a log file.

Zero-Maintenance Mode: With GitHub Actions, you can set it up once and forget about it.

How It Works
The core auto_committer.py script performs the following steps:

Opens a specified file within your local repository (e.g., commit_log.txt).

Appends the current date and time to the file, creating a change for Git to track.

Stages the modified file using git add.

Commits the change with a customizable message using git commit.

Pushes the commit to the origin remote repository using git push.

Setup and Usage
Prerequisites
Python 3

Git

A GitHub repository cloned to your local machine (or to be used with GitHub Actions).

Step 1: Get the Script
Clone this repository or add the auto_committer.py script to your own project's root directory.

Step 2: Install Dependencies
The script requires the GitPython library. Install it using pip:

Bash

pip install GitPython
Step 3: Choose Your Method
Method A: Running with GitHub Actions (Recommended)
This method runs the script on GitHub's servers and works even when your computer is off.

Create the Workflow File:
In your repository, create the directory structure .github/workflows/. Inside it, create a file named auto_commit.yml and paste the following content:

YAML

name: Daily Auto Commit

on:
  schedule:
    # Runs every day at 02:00 UTC. Use https://crontab.guru to customize.
    - cron: '0 2 * * *'
  # Allows you to run this workflow manually from the Actions tab
  workflow_dispatch:

jobs:
  auto-commit-job:
    runs-on: ubuntu-latest

    steps:
      - name: Check out repository
        uses: actions/checkout@v4
        with:
          # We need a token with write permissions to push changes
          token: ${{ secrets.GH_PAT }}

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install GitPython

      - name: Configure Git User
        run: |
          git config --global user.name 'GitHub Actions Bot'
          git config --global user.email 'github-actions-bot@users.noreply.github.com'

      - name: Run the auto-committer script
        run: python auto_committer.py
Create a Personal Access Token (PAT):
The workflow needs a token with permissions to push commits.

Go to GitHub Settings > Developer settings > Personal access tokens > Tokens (classic).

Click Generate new token.

Give it a Note (e.g., "Auto Commit Action"), set an Expiration, and select the repo scope.

Copy the generated token.

Add the Token as a Repository Secret:

In your repository, go to Settings > Secrets and variables > Actions.

Click New repository secret.

Name the secret GH_PAT.

Paste your Personal Access Token into the Secret box.

That's it! The action will now run on the schedule you defined.

Method B: Running Locally
This method uses your own computer to run the script.

Configure the Script:
Open auto_committer.py and modify the configuration variables at the top of the file:

Python

# --- CONFIGURATION ---
REPO_PATH = "/path/to/your/local/repo" # e.g., "C:/Users/YourUser/project"
FILE_TO_MODIFY = "commit_log.txt"
COMMIT_MESSAGE = "Automated commit on {date}"
# --- END OF CONFIGURATION ---
Schedule the Script:

On Windows: Use Task Scheduler to create a task that runs python.exe with auto_committer.py as the argument at your desired time.

On macOS/Linux: Use cron. Open your crontab with crontab -e and add a line like this to run the script daily at 10 PM:

Bash

0 22 * * * /usr/bin/python3 /path/to/your/script/auto_committer.py
⚠️ Disclaimer
This tool is intended for personal use, such as maintaining a commit streak on a personal project or learning about automation. It should not be used to misrepresent your activity in a professional, academic, or collaborative setting. Meaningful contributions are always more valuable than an artificially inflated commit graph.

