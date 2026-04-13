import numpy as np

np.random.seed(42)

trials = 1000
count_sum_7 = 0

for _ in range(trials):
    die1 = np.random.randint(1, 7)
    die2 = np.random.randint(1, 7)

    if die1 + die2 == 7:
        count_sum_7 += 1

# MUST be outside loop
experimental_probability = count_sum_7 / trials

print("Experimental Probability of Sum = 7:", experimental_probability)
