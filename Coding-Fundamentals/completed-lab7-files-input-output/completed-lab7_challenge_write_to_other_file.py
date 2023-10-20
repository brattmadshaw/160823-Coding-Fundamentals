import os

# Define the directory path
directory_path = ".\completed-lab7-files-input-output"

# Create the directory if it doesn't exist
if not os.path.exists(directory_path):
    os.makedirs(directory_path)

teams = []

while True:
    team_name = input("Enter the name of a team (or type 'exit' to stop): ")
    if team_name.lower() == 'exit':
        break
    teams.append(team_name)

if teams:
    file_path = os.path.join(directory_path, 'completed-lab7_challenge_other_file.txt')

    with open(file_path, 'w') as file:
        for i, team in enumerate(teams, start=1):
            file.write(f"team {i}: {team}\n")

    print(f"Teams have been added to {file_path}.")
else:
    print("No teams were added to the list.")
