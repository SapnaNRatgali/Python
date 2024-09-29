# sorted(tuple) - Returns a sorted list of the tuple elements.
# sorted() is the function used to return a new sorted list from the elements of the iterable (like a tuple). 
# It does not modify the original tuple and is commonly used for sorting.


my_tuple = (3, 1, 4)

# Using sorted() to sort the tuple
sorted_list = sorted(my_tuple)  # Returns a sorted list: [1, 3, 4]

# Convert the sorted list back to a tuple
sorted_tuple = tuple(sorted_list)

print(sorted_tuple)  # Output: (1, 3, 4)
