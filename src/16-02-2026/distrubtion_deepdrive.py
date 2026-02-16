import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Sample dataset
data = {
    "Price": [40, 65, 80, 95, 120, 155, 190, 210, 85, 70, 60],
    "City": ["Bangalore", "Mumbai", "Delhi", "Bangalore", "Mumbai",
             "Delhi", "Delhi", "Mumbai", "Bangalore", "Bangalore", "Delhi"]
}

df = pd.DataFrame(data)

# Histogram with KDE (Numerical Variable)
sns.histplot(df["Price"], kde=True)
plt.title("Price Distribution")
plt.xlabel("Price (Lakhs)")
plt.ylabel("Frequency")
plt.show()

# Skewness & Kurtosis
skewness = df["Price"].skew()
kurtosis = df["Price"].kurt()

print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")

# Count Plot (Categorical Variable)
sns.countplot(x=df["City"])    

plt.title("City Frequency")
plt.xlabel("City")
plt.ylabel("Count")
plt.show()

# Observation Example
print("Observation: The distribution shape helps determine if transformations are needed.")
