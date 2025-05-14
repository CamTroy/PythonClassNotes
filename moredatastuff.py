# More data stuff

import numpy as np

def print_detes(arr):

    print(f"\nArray: {arr}")
    print(f"\nDimensions: {arr.ndim}")  # Amount of dimensions
    print(f"Size: {arr.size}")  # Amount of items
    print(f"Element type: {arr.dtype}")  # Type array is storing
    print(f"Shape: {arr.shape}")  # 2x2, 3x3, etc. In the case of nums_array, (13,)

# Student scores in [Math, Science, English]
data = np.array([
    # Math, Science, English
    [98, 67, 100],
    [70, 60, 10],
    [80, 73, 74],
    [50, 10, 0],
    [80, 69, 70],
    [100, 100, 100],
    [20, 40, 50],
    [100, 80, 105],
    [100, 100, 95],
    [96, 97, 98],
    [78, 82, 91]
])

avg_score = np.mean(data)
print(f"Average score: {avg_score}")

scores = data[:, 0]
avg_score = np.mean(avg_score)