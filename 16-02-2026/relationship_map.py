import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ✅ Generate Dataset (500 rows)
np.random.seed(42)

df = pd.DataFrame({
    # Log-normal distribution → realistic price skew
    "Price": np.random.lognormal(mean=4, sigma=0.5, size=500),

    # Random categorical variable
    "City": np.random.choice(
        ["Bangalore", "Mumbai", "Delhi", "Chennai", "Hyderabad"],
        size=500
    )
})

# Optional scaling (makes values look like real prices)
df["Price"] = df["Price"] * 10  # Convert to Lakhs-like range

# ✅ Histogram with KDE
sns.histplot(df["Price"], kde=True)
plt.title("Housing Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

# ✅ Skewness & Kurtosis

skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print(f"Skewness: {skewness:.2f}")
print(f"Kurtosis: {kurtosis:.2f}")

# ✅ Count Plot (Categorical Variable)
sns.countplot(x=df["City"])
plt.title("City Frequency Distribution")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

# ✅ Observation Example
print("\nObservation:")
print("If skewness is high → Prices are skewed → Consider Log Transformation.")
