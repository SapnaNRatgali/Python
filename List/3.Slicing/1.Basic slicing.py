# Syntax of Slicing
'''
new_sequence = original_sequence[start:end:step]

start: The index at which to begin the slice (inclusive). If omitted, it defaults to 0.
end: The index at which to end the slice (exclusive). If omitted, it defaults to the length of the sequence.
step: The increment between each index in the slice (optional). If omitted, it defaults to 1.
'''

# Basic Slicing

my_list = [10, 20, 30, 40, 50]
print("My list contains : ",my_list)

sliced = my_list[1:4]  # Start at index 1, end at index 4 (exclusive)
print(f"Sliced list from index 1 to 4 (exclusive): {sliced}")  
print()
