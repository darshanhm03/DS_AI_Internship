import numpy as np
import pandas as pd

# Set seed for reproducibility
np.random.seed(42)

# Generate datasets
heights = np.random.normal(loc=170, scale=10, size=1000)
incomes = np.random.exponential(scale=50000, size=1000)
scores = 100 - np.random.exponential(scale=10, size=1000)

# Create DataFrame
df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

# ---- Z-SCORE CALCULATION ----
for column in df.columns:
    
    mean = df[column].mean()      
    std = df[column].std()    
    
    df[f"{column}_zscore"] = (df[column] - mean) / std

# ---- OUTLIER DETECTION ----
outliers = pd.DataFrame()

for column in df.columns[:3]:
    
    condition = df[f"{column}_zscore"].abs() > 3
    detected = df[condition]
    
    print(f"\n{column}")
    print(f"Mean (μ): {df[column].mean():.2f}")
    print(f"Std Dev (σ): {df[column].std():.2f}")
    print(f"Outliers Found: {detected.shape[0]}")
    
    outliers = pd.concat([outliers, detected])

# Remove duplicate rows
outliers = outliers.drop_duplicates()

print("\nTotal Unique Outlier Rows:", outliers.shape[0])
print(outliers.head())
