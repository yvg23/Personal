import os
import random
from datetime import datetime, timedelta

# Define the start and end dates
start_date = datetime(2022, 4, 15)
end_date = datetime(2024, 5, 6)  # One day before September 11, 2023

for i in range(2000):
    # Generate a random date within the specified range
    rand_days = random.randint(0, (end_date - start_date).days)
    commit_date = start_date + timedelta(days=rand_days)
    
    # Format the date as 'YYYY-MM-DD'
    formatted_date = commit_date.strftime('%Y-%m-%d')
    
    # Generate a commit message with the formatted date
    commit_message = f"Commit on {formatted_date}"
    
    # Append the commit message to 'test.txt'
    with open('test.txt', 'a') as file:
        file.write(commit_message + '\n')
    
    # Stage and commit the changes using Git
    os.system('git add test.txt')
    os.system(f'git commit --date="{commit_date}" -m "{commit_message}"')

# Push the commits to the remote repository
os.system('git push -u origin main')
