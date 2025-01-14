from nba_api.stats.static import teams
from nba_api.stats.endpoints import teamdetails

# Get the team ID for the Oklahoma City Thunder
okc_team = teams.find_teams_by_full_name("Oklahoma City Thunder")[0]
okc_team_id = okc_team['id']

# Get the team details, which includes the roster
team_info = teamdetails.TeamDetails(team_id=okc_team_id)

# Print the team roster
print(team_info.get_data_frames()[0])  # The first DataFrame contains the roster

