import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

np.random.seed(42)


heights = np.random.normal(loc=170, scale=10, size=1000)


incomes = np.random.exponential(scale=50000, size=1000)


scores = 100 - np.random.exponential(scale=10, size=1000)


df = pd.DataFrame({
    "Heights": heights,
    "Incomes": incomes,
    "Scores": scores
})

# Plotting
plt.figure(figsize=(15, 4))

for i, column in enumerate(df.columns, 1):
    plt.subplot(1, 3, i)
    sns.histplot(df[column], kde=True)
    plt.title(column)

plt.tight_layout()
plt.show()

# Mean vs Median Comparison
for column in df.columns:
    mean = df[column].mean()
    median = df[column].median()
    print(f"{column}: Mean = {mean:.2f}, Median = {median:.2f}")
