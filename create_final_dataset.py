import pandas as pd

agg = pd.read_csv("aggregated_team_stats_2015-2024.csv")
agg.columns = agg.columns.str.strip().str.lower() 

pl = pd.read_csv("pl-tables-1993-2024.csv", encoding='latin-1')
pl.columns = pl.columns.str.strip().str.lower() 

# Filter the league table data for seasons between 2015 and 2024
pl_filtered = pl[pl["season-end-year"].between(2015, 2024)]

print("Aggregated data columns:", agg.columns.tolist())
print("PL table columns:", pl_filtered.columns.tolist())


final_df = pd.merge(
    agg,
    pl_filtered[["season-end-year", "team", "points"]],
    on=["season-end-year", "team"],
    how="left"
)

print("Final dataset preview:")
print(final_df.head())
print("Final dataset shape:", final_df.shape)

final_df.to_csv("final_dataset_2015-2024.csv", index=False)
