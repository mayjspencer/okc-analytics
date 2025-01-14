from nba_api.stats.endpoints import AssistTracker
from nba_api.stats.static import teams

# Get the team ID for the Oklahoma City Thunder
okc_team = teams.find_teams_by_full_name("Oklahoma City Thunder")[0]
okc_team_id = okc_team['id']

# Create an AssistTracker object with parameters
assist_tracker = AssistTracker(
    season_nullable='2024-25',
    team_id_nullable=okc_team_id,
)

# Get the data frame
data = assist_tracker.get_data_frames()[0]
print(data.head())