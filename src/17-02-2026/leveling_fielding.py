import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler, MinMaxScaler

# Reproducibility
np.random.seed(42)

# Sample numeric dataset
age = np.random.randint(18, 60, 200)
salary = np.random.randint(20000, 150000, 200)

df = pd.DataFrame({
    "Age": age,
    "Salary": salary
})

print("Original Data:\n", df.head())

# -----------------------------
# ✅ Standardization
# -----------------------------
standard_scaler = StandardScaler()
df_standardized = pd.DataFrame(
    standard_scaler.fit_transform(df),
    columns=df.columns
)

print("\nStandardized Data:\n", df_standardized.head())

# -----------------------------
# ✅ Normalization
# -----------------------------
minmax_scaler = MinMaxScaler()
df_normalized = pd.DataFrame(
    minmax_scaler.fit_transform(df),
    columns=df.columns
)

print("\nNormalized Data:\n", df_normalized.head())

# -----------------------------
# ✅ Histograms
# -----------------------------

# Original Salary
plt.figure()
plt.hist(df["Salary"], bins=20)
plt.title("Original Salary Distribution")
plt.xlabel("Salary")
plt.ylabel("Frequency")
plt.show()

# Standardized Salary
plt.figure()
plt.hist(df_standardized["Salary"], bins=20)
plt.title("Standardized Salary Distribution (Mean=0, Std=1)")
plt.xlabel("Standardized Salary")
plt.ylabel("Frequency")
plt.show()

# Normalized Salary
plt.figure()
plt.hist(df_normalized["Salary"], bins=20)
plt.title("Normalized Salary Distribution (0 to 1 Range)")
plt.xlabel("Normalized Salary")
plt.ylabel("Frequency")
plt.show()
