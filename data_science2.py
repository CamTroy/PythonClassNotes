# NumPy - a library for arrays
# NumPy arrays are fixed size, single type, and can be multidimensional

# install numpy first

import numpy as np

# nums = [10, 20, 30, 40, 50, 60, 69, 70, 80, 90, 100, 420, 911] # Regular List

# Make NumPy array
nums_array = np.array([10, 20, 30, 40, 50, 60, 69, 70, 80, 90, 100, 420, 911, 1000])

# Get info about an array
def print_detes(arr):

    print(f"\nArray: {arr}")
    print(f"\nDimensions: {arr.ndim}")  # Amount of dimensions
    print(f"Size: {arr.size}")  # Amount of items
    print(f"Element type: {arr.dtype}")  # Type array is storing
    print(f"Shape: {arr.shape}")  # 2x2, 3x3, etc. In the case of nums_array, (13,)

print_detes(nums_array)

# Create arrays in different ways
print_detes(np.array([
    # PlayerId, MaxHP, CurrentHP - Taken from data_science.py
    [1, 150, 140], # Record 1 - Row 0
    [2, 200, 100], # Record 2 - Row 1
    [3, 500, 350], # Record 3 - Row 2
    [4, 250, 250], # Record 4 - Row 3
]))

# NumPy functions
zeroes = np.zeros((5, 5)) # Creates a 5x5 with zeroes for all values
print_detes(zeroes)

range_array = np.arange(1, 100, 1) # Create an array with a range, follows start, stop, step - Inclusive start, exclusive stop
print_detes(range_array)

linspace_array = np.linspace(0, 100, 5) # Creates an array with (start, stop, num).
# The third parameter, num, defines how many evenly spaced numbers you want between the start and stop.
print_detes(linspace_array)

reshaped_array = np.reshape(nums_array, (7, 2)) # It splits an array into a multidimensional one
print_detes(reshaped_array)