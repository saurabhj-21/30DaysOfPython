s ={} #This is still a dictionary
print(type(s))

s = set() #This is now an empty set
print(type(s)) #Output: <class 'set'>
# The set() constructor can also be used to create a set from a list, tuple, or dictionary. 

# Create a set from a list
list_to_set = set([1, 2, 3, 4, 5, "Saurabh"])
print(list_to_set) #Output: {1, 2, 3, 4, 5}

# Create a set from a tuple
tuple_to_set = set((1, 2, 3, 4, 5))
print(tuple_to_set) #Output: {1, 2, 3, 4, 5}

# Create a set from a dictionary
dict_to_set = set({1: "One", 2: "Two", 3: "Three"}) #Only keys are considered
print(dict_to_set) #Output: {1, 2, 3}


# Set Operations
s = {1, 2, 3}

# Method to add an element to a set
def add_element(s, element):
    s.add(element)
    return s
print(add_element(s, 4))  # Output: {1, 2, 3, 4}

# Method to remove an element from a set
def remove_element(s, element):
    s.discard(element)  # discard does not raise an error if the element is not found
    return s
print(remove_element(s, 2))  # Output: {1, 3, 4}

# Method to check if an element is in a set
def is_element_in_set(s, element):
    return element in s
print(is_element_in_set(s, 3))  # Output: True

# Method to get the union of two sets
def union_sets(set1, set2):
    return set1.union(set2)
print(union_sets({1, 2}, {2, 3}))  # Output: {1, 2, 3}

# Method to get the intersection of two sets
def intersection_sets(set1, set2):
    return set1.intersection(set2)
print(intersection_sets({1, 2}, {2, 3}))  # Output: {2}

# Method to get the difference of two sets
def difference_sets(set1, set2):
    return set1.difference(set2)
print(difference_sets({1, 2}, {2, 3}))  # Output: {1}







