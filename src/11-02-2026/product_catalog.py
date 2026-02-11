import pandas as pd

products = pd.Series([700, 150, 300, 250], index=['Laptop', 'Mouse', 'Keyboard', 'Moniter'])

laptop_price = products['Laptop']

first_two_products = products.iloc[:4]

print("Full Series:")
print(products)

print("\nPrice of Laptop:")
print(laptop_price)

print("\nFirst two products (positional indexing):")
print(first_two_products)
