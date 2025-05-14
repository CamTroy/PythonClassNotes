# BIG data

# Lists/slicing
nums = [10, 20, 30, 40, 50, 60, 69, 70, 80, 90, 100, 420, 911]

# Negatives work in reverse, so there is -1, -2, -3... all the way to the start of the array
# Last thing in the array, use index -1
print(nums[-1])

# Slicing - (start:stop) & (start:stop:step)
# start is inclusive
# stop is not inclusive
sliced = nums[3:6]
print(sliced)

# Default stop is the end of the array, step determines the next element to get
sliced = nums[0::2]
print(sliced)

# Data set
# Player Stats - Example in a 2D array
player_data = [
    # PlayerId, MaxHP, CurrentHP
    [1, 150, 140], # Record 1 - Row 0
    [2, 200, 100], # Record 2 - Row 1
    [3, 500, 350], # Record 3 - Row 2
    [4, 250, 250], # Record 4 - Row 3
]

for player in player_data:

    print(f"Player {player[0]} has a max HP of {player[1]} and currently has {player[2]}({player[2] / player[1] * 100}%) HP.")