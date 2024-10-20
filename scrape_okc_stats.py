import requests
import pandas as pd

# URL for Oklahoma City Thunder stats (Example API)
url = 'https://data.nba.net/data/10s/prod/v1/2024/teams/okc/roster.json'  # Modify this URL based on your API choice

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    players = data['league']['standard']['players']
    
    # Create a DataFrame
    df = pd.json_normalize(players)
    
    # Display the first few rows
    print(df.head())
else:
    print(f"Error: {response.status_code}")
