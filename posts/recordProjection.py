import matplotlib.pyplot as plt
from nba_api.stats.endpoints import teamgamelog
from nba_api.stats.static import teams

# Get the team ID for the Oklahoma City Thunder
okc_team = teams.find_teams_by_full_name("Oklahoma City Thunder")[0]
okc_team_id = okc_team['id']

# Fetch the game log for the current season
game_log = teamgamelog.TeamGameLog(team_id=okc_team_id, season='2024-25')

# Get the data frame
game_data = game_log.get_data_frames()[0]

# Reverse the DataFrame to process games in chronological order
game_data = game_data.iloc[::-1]

# Calculate cumulative wins for accurate plotting
game_data['CumulativeWins'] = (game_data['WL'] == 'W').cumsum()

# Input Data
current_wins = game_data['CumulativeWins'].iloc[-1]
current_losses = len(game_data) - current_wins
games_played = current_wins + current_losses
win_percentage = current_wins / games_played

# Projection Calculations
total_games = 82
projected_wins = round(win_percentage * total_games)
projected_losses = total_games - projected_wins

# Generate Text
current_record_text = f"The Current OKC Thunder Record is {current_wins}-{current_losses}, which is a {win_percentage:.1%} win percentage."
projected_record_text = f"The Projected OKC Thunder Record is {projected_wins}-{projected_losses}."

# Plot the Line Graph
games_played_x = list(range(1, games_played + 1))
cumulative_wins_y = game_data['CumulativeWins'].tolist()

projected_games_x = list(range(games_played, total_games + 1))
projected_cumulative_wins_y = [cumulative_wins_y[-1] + int(win_percentage * (g - games_played)) for g in projected_games_x]

plt.figure(figsize=(8, 6))
plt.plot(games_played_x, cumulative_wins_y, label="Actual Wins", color="blue", linewidth=2)
plt.plot(projected_games_x, projected_cumulative_wins_y, label="Projected Wins", color="blue", linestyle="dotted")
plt.axhline(projected_wins, color="gray", linestyle="dashed", label=f"Projection: {projected_wins}-{projected_losses}")

# Customizing the Graph
plt.title("OKC Thunder Regular Season Record Projection", fontsize=14)
plt.xlabel("Games Played", fontsize=12)
plt.ylabel("Wins", fontsize=12)
plt.xticks(range(0, total_games + 1, 10))
plt.legend()
plt.grid(alpha=0.5)
plt.tight_layout()

# Save and Show Plot
plt.savefig("record_projection.png")
plt.show()

# Print the Text
print(current_record_text)
print(projected_record_text)
