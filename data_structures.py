# Data structures

# List
# Lists are mutable.
my_list = []
num_list = [1, 2, 3, 4, 5]
# Lists can have any mix of types in them. They maintain the order of the items inside, and duplicates are allowed.
confusing_list = [1, "one", ("one", "two"), 1.2]

confusing_list.append("bruh")

print("Lists:")
print(my_list)
print(num_list)
print(confusing_list)

# Tuples
# Tuples are immutable. They keep the order of the items inside, and also allow duplicates.
my_tuple = ()
num_tuple = (1, 2, 3, 4, 5)
confusing_tuple = (1, "one", ("one", "two"), 1.2)

print("Tuples:")
print(my_tuple)
print(num_tuple)
print(confusing_tuple)

# Sets
# All values in a set have to be unique, the order of items in sets doesn't matter and isn't considered.
# Items in a set can't be changed, but they can be added and removed.
my_set = {}
num_set = {1, 2, 3, 4, 5, 1, 2, 3, 4, 5}
confusing_set = {1, "one", ("one", "two"), 1.2}

print("Sets:")
print(my_set)
print(num_set)
print(confusing_set)

# Sets also are considered equal even if values are in different spots.
left_right_set = {"left", "right"}
right_left_set = {"right", "left"}
print(left_right_set == right_left_set) # Prints true

# Dictionary, key value pairs. The order of a dictionary matters, and duplicates are are not allowed.
# Dictionary items can be edited.
my_dictionary = {
    "Bruh": "Vruh",
    "Bro": "Vro"
}

word = "Bruh"
if word in my_dictionary:
    print("lmao")