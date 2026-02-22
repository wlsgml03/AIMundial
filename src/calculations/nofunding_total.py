import pandas as pd
from pathlib import Path

def get_unfunded_famine_countries():
    base_dir = Path(__file__).resolve().parents[2]  # goes up to AIMundial/
    df = pd.read_csv(base_dir / 'clean_data' / 'famine_risk_scores.csv')
    
    no_funding = df[
        (df['predicted_famine'] == 1) &
        (df['allocations'].isna() | (df['allocations'] == 0))
    ]
    
    unfunded_count = no_funding['entity'].nunique()
    return no_funding, unfunded_count