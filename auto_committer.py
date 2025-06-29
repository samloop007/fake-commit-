import os
from git import Repo
from datetime import datetime

# --- CONFIGURATION ---
# 1. Set the full path to your local repository
REPO_PATH = "/home/agaicodetech/Desktop/fk-git-push" 

# 2. Set the name of the file to modify for commits
#    This file should exist in your repository.
FILE_TO_MODIFY = "commit_log.txt"

# 3. Customize your commit message
#    The {date} placeholder will be replaced with the current timestamp.
COMMIT_MESSAGE = "Automated commit on {date}"
# --- END OF CONFIGURATION ---


def auto_commit():
    """
    Automatically creates a commit with a timestamp and pushes it to the remote.
    """
    if not os.path.isdir(REPO_PATH):
        print(f"Error: Repository path not found at '{REPO_PATH}'")
        return

    try:
        # Initialize the repository object
        repo = Repo(REPO_PATH)

        # Check if the repository is dirty (has uncommitted changes)
        if repo.is_dirty(untracked_files=True):
            print("Repository has uncommitted changes. Please commit them manually first.")
            return

        # --- Make a change to the file ---
        file_path = os.path.join(REPO_PATH, FILE_TO_MODIFY)
        
        if not os.path.exists(file_path):
             # Create the file if it doesn't exist
            with open(file_path, "w") as f:
                f.write("Commit log initialized.\n")

        # Append the current timestamp to the file
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(file_path, "a") as f:
            f.write(f"Commit made at: {current_time}\n")

        # --- Git Operations ---
        # 1. Stage the file
        repo.git.add(FILE_TO_MODIFY)
        print(f"Staged '{FILE_TO_MODIFY}'")

        # 2. Commit the changes
        final_commit_message = COMMIT_MESSAGE.format(date=current_time)
        repo.git.commit('-m', final_commit_message)
        print(f"Committed with message: '{final_commit_message}'")

        # 3. Push to the remote repository (e.g., 'origin')
        origin = repo.remote(name='origin')
        origin.push()
        print("Pushed changes to remote repository.")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    auto_commit()