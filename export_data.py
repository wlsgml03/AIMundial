from src.calculations.nofunding_total import get_unfunded_famine_countries
no_funding, _ = get_unfunded_famine_countries()

filtered = no_funding[no_funding['year'].between(2012, 2022)]

filtered.to_csv('clean_data/unfunded_countries_2012_2022.csv', index=False)
print(f"Saved {len(filtered)} rows")
