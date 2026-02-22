import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

df = pd.read_csv(r'C:\Users\Test\Documents\AIMundial\clean_data\famine_risk_scores.csv')

# Only countries that received funding
funded = df[df['allocations'].notna() & (df['allocations'] > 0)]

X = funded[['famine_risk_score']].values
y = funded['allocations'].values

model = LinearRegression()
model.fit(X, y)

# Pick highest-risk unfunded country from 2022
unfunded_high_risk = df[
    (df['predicted_famine'] == 1) & 
    (df['allocations'].isna() | (df['allocations'] == 0)) &
    (df['year'] == 2022)
].sort_values('famine_risk_score', ascending=False).iloc[0]

test_country = unfunded_high_risk['entity']
test_year = int(unfunded_high_risk['year'])
test_score = unfunded_high_risk['famine_risk_score']
predicted_funding = model.predict([[test_score]])[0]

print(f"\nTest case: {test_country} ({test_year})")
print(f"Famine risk score: {test_score:.4f}")
print(f"Predicted funding needed: ${predicted_funding:,.0f}")

# Plot
fig, ax = plt.subplots(figsize=(9, 5))
ax.scatter(X, y, color='#5B92E5', alpha=0.7, s=60, label='Funded countries')

x_line = np.linspace(X.min() - 0.05, X.max() + 0.05, 200).reshape(-1, 1)
y_line = model.predict(x_line)
ax.plot(x_line, y_line, color='white', linewidth=2, label='Regression line')

ax.scatter(test_score, predicted_funding, color='#f97316', s=140, zorder=5,
           label=f'{test_country} {test_year} (predicted)')
ax.annotate(f'{test_country} ({test_year})\n${predicted_funding:,.0f}',
            xy=(test_score, predicted_funding),
            xytext=(12, 12), textcoords='offset points',
            color='#f97316', fontsize=9, fontweight='bold')

ax.set_facecolor('#0f1117')
fig.patch.set_facecolor('#0f1117')
ax.tick_params(colors='#94a3b8')
ax.xaxis.label.set_color('#94a3b8')
ax.yaxis.label.set_color('#94a3b8')
for spine in ax.spines.values():
    spine.set_edgecolor('#2a2d3a')
ax.set_xlabel('Famine Risk Score')
ax.set_ylabel('Funding Received (USD)')
ax.set_title('Famine Risk Score vs Funding Received', color='white', fontsize=13, pad=15)
ax.legend(facecolor='#1a1d27', labelcolor='white', framealpha=0.8)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x/1e6:.1f}M'))

plt.tight_layout()
plt.savefig(r'C:\Users\Test\Documents\AIMundial\clean_data\regression_plot.png', dpi=150, bbox_inches='tight')
print("\nPlot saved to clean_data/regression_plot.png")
from sklearn.metrics import r2_score
r2 = r2_score(y, model.predict(X))
print(f"R² Score: {r2:.3f}")