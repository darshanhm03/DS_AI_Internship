import pandas as pd

# Sample data to demonstrate the problem
data = {
    "Price": ["$100", "$250.50", "$75", "$300"],
    "Date": ["2024-01-01", "2024-01-05", "2024-01-10", "2024-01-15"]
}

df = pd.DataFrame(data)

# 1. Check initial data types
print("Initial data types:")
print(df.dtypes)

# 2. Remove '$' symbol and convert Price to float
df["Price"] = df["Price"].str.replace("$", "", regex=False).astype(float)

# 3. Convert Date column to datetime
df["Date"] = pd.to_datetime(df["Date"])

# Check data types after conversion
print("\nData types after conversion:")
print(df.dtypes)