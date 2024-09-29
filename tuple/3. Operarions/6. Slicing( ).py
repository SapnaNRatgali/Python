# Slicing ([:]) - Extracts a portion of the tuple.

# Syntax: tuple[start:stop:step]

# start: The index to start the slice (inclusive).
# stop: The index to end the slice (exclusive).
# step: The interval between elements (optional).

my_tuple = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)

# Slicing from index 2 to 5 using just start,stop
sliced_tuple = my_tuple[2:5]
print(sliced_tuple)  # Output: (2, 3, 4)
print()

# Slicing with a start,stop and step
sliced_tuple_step = my_tuple[1:8:2]
print(sliced_tuple_step)  # Output: (1, 3, 5, 7)
print()

# If we will omit start, it by defaults begins from (index 0).
# If we will omit stop, it by defaults go till end of the tuple.
# If we will omit step, it defaults the interval between elements to 1).

my_tuple = (10, 20, 30, 40, 50, 60)

# Slicing from start to index 4
sliced_tuple_omit_start = my_tuple[:4]
print(sliced_tuple_omit_start)  # Output: (10, 20, 30, 40)
print()

# Slicing from index 2 to the end
sliced_tuple_omit_stop = my_tuple[2:]
print(sliced_tuple_omit_stop)  # Output: (30, 40, 50, 60)
print()

# Negative Indices - You can also use negative indices to slice from the end of the tuple.

my_tuple = (10, 20, 30, 40, 50, 60)

# Slicing with negative indices
sliced_tuple_negative = my_tuple[-5:-2]
print(sliced_tuple_negative)  # Output: (30, 40, 50)
print()

# Slicing with a Negative Step - you can use a negative step to reverse the slice.

my_tuple = (0, 1, 2, 3, 4, 5)

# Slicing with a negative step
sliced_tuple_reverse = my_tuple[5:0:-1]
print(sliced_tuple_reverse)  # Output: (5, 4, 3, 2, 1)
print()


