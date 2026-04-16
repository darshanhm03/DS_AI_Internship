import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Step 1: Create dataset
data = {
    "Student": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"],
    "Marks": [65, 70, 72, 68, 75, 80, 78, 74, 69, 200]
}

df = pd.DataFrame(data)

# Step 2: Calculate Mean and Standard Deviation
mean = df["Marks"].mean()
std = df["Marks"].std()

# Step 3: Calculate Z-score
df["z_score"] = (df["Marks"] - mean) / std

# Step 4: Detect Outliers
outliers = df[abs(df["z_score"]) > 3]

# Step 5: Print Results
print("Dataset with Z-Scores:")
print(df)

print("\nMean:", mean)
print("Standard Deviation:", std)

print("\nOutliers Detected (|Z| > 3):")
print(outliers)

# Step 6: Histogram
plt.figure()
plt.hist(df["Marks"], bins=10)
plt.title("Histogram of Marks")
plt.xlabel("Marks")
plt.ylabel("Frequency")
plt.show()

# Step 7: Boxplot
plt.figure()
plt.boxplot(df["Marks"])
plt.title("Boxplot of Marks (Outlier Detection)")
plt.ylabel("Marks")
plt.show()