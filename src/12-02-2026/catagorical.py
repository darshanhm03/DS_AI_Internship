import pandas as pd

# Sample data
data = {
    "Location": [" New York", "new york", "NEW YORK ", "New York"]
}

df = pd.DataFrame(data)

# 1. Remove leading and trailing spaces
df["Location"] = df["Location"].str.strip()

# 2. Standardize text case (you can use .lower() or .title())
df["Location"] = df["Location"].str.title()

# 3. Verify normalization
print(df["Location"].unique())