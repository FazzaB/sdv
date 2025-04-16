import pandas as pd
TEAM_NAME_MAP = {
    "Man City": "Manchester City",
    "Man United": "Manchester Utd",
    "Leeds": "Leeds United",
    "Nott'm Forest": "Nottingham Forest",
    "Wolves": "Wolverhampton Wanderers",  
    "QPR": "Queens Park Rangers",         
    "Hull": "Hull City",
    "West Brom": "West Bromwich Albion",
    "Sheffield Utd": "Sheffield United",
    "Leicester": "Leicester City",
    "Swansea": "Swansea City",
    "Stoke": "Stoke City",
    "Newcastle": "Newcastle United",
    "Newcastle Utd": "Newcastle United",
    "Norwich": "Norwich City",
    "Luton": "Luton Town",
    "Cardiff": "Cardiff City",
}

def standardise_team_name(name: str) -> str:
    """Return the standardised team name if found in TEAM_NAME_MAP, else the original."""
    if not isinstance(name, str):
        return name 
    name = name.strip()
    return TEAM_NAME_MAP[name] if name in TEAM_NAME_MAP else name

agg = pd.read_csv("aggregated_team_stats_2015-2024.csv")
agg.columns = agg.columns.str.strip().str.lower()

pl = pd.read_csv("pl-tables-1993-2024.csv", encoding='latin-1')
pl.columns = pl.columns.str.strip().str.lower()
pl_filtered = pl[pl["season-end-year"].between(2015, 2024)]

agg["team"] = agg["team"].apply(standardise_team_name)
pl_filtered["team"] = pl_filtered["team"].apply(standardise_team_name)

print("Aggregated data columns:", agg.columns.tolist())
print("PL table columns:", pl_filtered.columns.tolist())

final_df = pd.merge(
    agg,
    pl_filtered[["season-end-year", "team", "points"]],
    on=["season-end-year", "team"],
    how="left"
)

final_df["position"] = (
    final_df
    .groupby("season-end-year")["points"]
    .rank(method="first", ascending=False)
    .astype(int)
)

print("Final dataset preview:")
print(final_df.head())
print("Final dataset shape:", final_df.shape)

final_df.to_csv("final_dataset_2015-2024.csv", index=False)
