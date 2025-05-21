import numpy as np

pet_data = np.array([
    # [Age, Weight, Daily Food Consumption]
    [2, 5.0, 200],
    [4, 7.5, 300],
    [1, 3.2, 150],
    [5, 9.0, 350],
    [3, 6.0, 250],
    [2, 4.5, 180],
    [6, 10.0, 400],
    [1, 2.8, 140],
    [4, 7.2, 310],
    [3, 5.5, 220]
])

# Average Stats
#     What is the average age, weight and daily food consumption of the pets?
average_consumption = pet_data.mean(1)
print(f"The pets consume {average_consumption[3]} grams on average.\n")

# Hungry Pets
#     How many pets eat more than 300 grams of food daily?
more_than_300 = np.where(np.any(pet_data > 300, axis = 1))
print(f"{np.size(more_than_300[0])} pets eat more than 300 grams.\n")

# Weight Conversion
#     Convert all weight value from kg to lbs
multiplier = 2.2
weights_in_lbs = pet_data[:,1] * multiplier
print(f"The pets' weights converted to lbs are {weights_in_lbs}\n")

# Sorting
#     Sort the pets by age
sorted_pets = pet_data[pet_data[:, 0].argsort()]
print(f"The pets sorted by age: {sorted_pets}\n")