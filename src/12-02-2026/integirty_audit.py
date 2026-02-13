import pandas as pd

# Load dataset
df = pd.read_csv("customer_orders.csv")

# Shape before cleaning
print("Shape before cleaning:", df.shape)
 
# Missing values report
print("\nMissing values report:")
print(df.isna().sum())

# Select numeric columns
numeric_cols = df.select_dtypes(include="number").columns

# Fill missing numeric values with median
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

#  Remove duplicate rows
df = df.drop_duplicates()

#  Shape after cleaning
print("\nShape after cleaning:", df.shape)
