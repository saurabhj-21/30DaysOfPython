#Check that a tuple type cannot be changed in python.

# Output the error message when trying to change an element of a tuple

# Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Trying to change an element of the tuple
try:
    my_tuple[0] = 10
except TypeError as e:
    print(f"Error: {e}")

# Output the tuple to show it remains unchanged
print("Tuple after attempting to change an element:", my_tuple)