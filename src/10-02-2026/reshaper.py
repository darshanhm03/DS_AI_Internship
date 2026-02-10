import numpy as np

data = np.arange(24)

reshaped = data.reshape(4, 3, 2)

transposed = reshaped.transpose(0, 2, 1)

print("Final shape:", transposed.shape)
print("Final array:")
print(transposed)
