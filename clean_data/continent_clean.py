import pandas as pd

file_path = 'data/Data_ CERF Donor Contributions and Allocations - allocations.csv'
df = pd.read_csv(file_path)

# Filter agencies
target_agency = ['World Food Programme', 'Food and Agriculture Organization']
df = df[df['agencyName'].isin(target_agency)].copy()

# Filter years
df = df[df['year'].between(2016, 2026)].copy()

# Group by Continent + Year
continent_year_df = (
    df.groupby(['continentName', 'year'], as_index=False)['totalAmountApproved']
    .sum()
)

continent_year_df.to_csv(
    'clean_data/clean_allocations/allocations_by_continent_year.csv',
    index=False
)