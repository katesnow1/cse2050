import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv(r'C:\Users\kate\OneDrive\cse2050\SkillShare.csv')

future_year = 2025
tournament_teams = data[data['YEAR'].astype(str) == str(future_year)]
num_teams = 16
if len(tournament_teams) < num_teams:
    raise ValueError(f"Not enough teams for a {num_teams}-team bracket. Found only {len(tournament_teams)} teams.")

teams = tournament_teams.head(num_teams)

team_info = teams[['TEAM', 'SEED', 'POWER INDEX']].to_dict(orient='records')
print("Team keys:", team_info[0].keys())

print("Tournament Teams:")
for t in team_info:
    print(f"  Seed {t['SEED']}: {t['TEAM']} (Power INDEX: {t['POWER INDEX']})")
    
def simulate_matchup(team1, team2, k=1):
    rating_diff = team1['POWER INDEX'] - team2['POWER INDEX']
    prob_team1 = 1 / (1 + np.exp(-k * rating_diff))
    if np.random.rand() < prob_team1:
        return team1
    else:
        return team2

def simulate_tournament(teams_list):
    if (len(teams_list) & (len(teams_list) - 1)) != 0:
        raise ValueError("Number of teams must be a power of 2 for a balanced bracket.")

    bracket = []
    current_round = teams_list.copy()
    round_number = 1
    
    while len(current_round) > 1:
        round_results = []
        print(f"\n--- Round {round_number} ---")

        for i in range(0, len(current_round), 2):
            team1 = current_round[i]
            team2 = current_round[i+1]
            winner = simulate_matchup(team1, team2)
            round_results.append(winner)
            print(f"Seed {team1['SEED']} {team1['TEAM']} vs Seed {team2['SEED']} {team2['TEAM']} => Winner: {winner['TEAM']}")
        bracket.append(round_results)
        current_round = round_results
        round_number += 1

    champion = current_round[0]
    return bracket, champion

bracket, champion = simulate_tournament(team_info)
print(f"\nChampion: {champion['TEAM']} (Seed {champion['SEED']}, Power Index: {champion['POWER INDEX']})")


# Load data from CSV
csv_file = 'SkillShare.csv'  # Replace with your actual file path
df = data

# Extract team names and Power Index
teams = df["TEAM"]
power_index = df["POWER INDEX"]

# Create spaced-out x positions
x_pos = np.arange(0, len(teams) * 2, 2)  # Add extra space between bars

# Create bar chart
plt.figure(figsize=(12, 6))
plt.bar(x_pos, power_index, color="pink", width=1.0)  # Adjust bar width

# Format x-axis
plt.xticks(x_pos, teams, rotation=45, ha="right")  # Rotate labels for readability
plt.ylabel("Power Index")
plt.title("Power Index of Teams")

plt.show()