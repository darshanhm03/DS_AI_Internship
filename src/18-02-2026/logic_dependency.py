import numpy as np

np.random.seed(42)

trials = 10000
success = 0

for _ in range(trials):
    bag = ["Red"] * 5 + ["Blue"] * 5

    pick1 = np.random.choice(bag)
    bag.remove(pick1)  

    pick2 = np.random.choice(bag)

    if pick1 == "Red" and pick2 == "Red":
        success += 1

experimental_prob = success / trials
theoretical_prob = (5/10) * (4/9)

print("\nDependent Events")
print("Experimental Probability:", experimental_prob)
print("Theoretical Probability:", theoretical_prob)
