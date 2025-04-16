import pandas as pd

df = pd.read_csv("Combined_data_2015-2024.csv", encoding='latin-1')
df.columns = df.columns.str.strip().str.lower()  

print("Columns:", df.columns.tolist())

home = df[['season-end-year', 'hometeam', 'hst', 'hs', 'hc', 'fthg', 'hy']].copy()
home = home.rename(columns={
    'hometeam': 'team', 
    'hst': 'shots_on_target', 
    'hs': 'total_shots', 
    'hc': 'corners', 
    'fthg': 'goals_scored',
    'hy': 'yellow_cards'
})

away = df[['season-end-year', 'awayteam', 'ast', 'as', 'ac', 'ftag', 'ay']].copy()
away = away.rename(columns={
    'awayteam': 'team', 
    'ast': 'shots_on_target', 
    'as': 'total_shots', 
    'ac': 'corners', 
    'ftag': 'goals_scored',
    'ay': 'yellow_cards'
})

# Group by team and season, summing up the relevant metrics.
agg_home = home.groupby(['season-end-year', 'team']).sum().reset_index()
agg_away = away.groupby(['season-end-year', 'team']).sum().reset_index()

# Merge home and away aggregates on team and season
agg_total = pd.merge(agg_home, agg_away, on=['season-end-year', 'team'], 
                     suffixes=('_home', '_away'), how='outer').fillna(0)

# Sum home and away values to create season totals for each team.
agg_total['shots_on_target'] = agg_total['shots_on_target_home'] + agg_total['shots_on_target_away']
agg_total['total_shots'] = agg_total['total_shots_home'] + agg_total['total_shots_away']
agg_total['corners'] = agg_total['corners_home'] + agg_total['corners_away']
agg_total['goals_scored'] = agg_total['goals_scored_home'] + agg_total['goals_scored_away']
agg_total['yellow_cards'] = agg_total['yellow_cards_home'] + agg_total['yellow_cards_away']

agg_total = agg_total[['season-end-year', 'team', 
                       'shots_on_target', 'total_shots', 'corners', 'goals_scored', 'yellow_cards']]

# Save the aggregated team stats to a new CSV file.
agg_total.to_csv("aggregated_team_stats_2015-2024.csv", index=False)

print("Aggregated data preview:")
print(agg_total.head())
