import matplotlib.pyplot as plt

# Data
months = [1, 2, 3, 4, 5]
revenue = [2000, 4500, 4000, 7500, 9000]

# Line plot
plt.plot(months, revenue)

# Titles and labels
plt.title("Monthly Revenue Growth")
plt.xlabel("Month")
plt.ylabel("Revenue in USD")

# Show plot
plt.show()
