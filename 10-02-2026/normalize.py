import numpy as np

np.random.seed(42)  
scores = np.random.randint(50, 101, size=(5, 3))

subject_means = scores.mean(axis=0)

centered_scores = scores - subject_means

print("Original Scores:")
print(scores)

print("\nSubject-wise Mean:")
print(subject_means)

print("\nCentered (Normalized) Scores:")
print(centered_scores)
