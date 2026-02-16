import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "SquareFootage": [800, 1200, 1500, 1800, 2200, 2600, 3000, 3200],
    "Bedrooms": [1, 2, 3, 3, 4, 4, 5, 5],
    "Price": [40, 65, 80, 95, 120, 155, 190, 500]  # Notice potential outlier
}

df = pd.DataFrame(data)

# ✅ Correlation Matrix
corr_matrix = df.corr()

# Heatmap Visualization
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Matrix Heatmap")
plt.show()

# ✅ Identify Highly Correlated Variables
print("\nHighly Correlated Variable Pairs (Correlation > 0.8):")

for col1 in corr_matrix.columns:
    for col2 in corr_matrix.columns:
        if col1 != col2 and corr_matrix.loc[col1, col2] > 0.8:
            print(f"{col1} & {col2} -> {corr_matrix.loc[col1, col2]:.2f}")

# ✅ Boxplot for Outlier Detection
sns.boxplot(y=df["Price"])
plt.title("Price Outlier Detection")
plt.ylabel("Price (Lakhs)")
plt.show()

# ✅ Observation Example
print("\nObservation:")
print("Variables with very high correlation may cause multicollinearity.")
print("Extreme values in Price may indicate outliers affecting analysis.")
