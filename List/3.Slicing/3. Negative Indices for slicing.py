# python supports negative indexing, which allows you to slice from the end of the sequence:

"""
----- how negative slicing works:- ------

Index:     0   1   2   3   4
           -------------------
List:    [10, 20, 30, 40, 50]
           -------------------
Index:    -5  -4  -3  -2  -1

"""

my_list = [10, 20, 30, 40, 50]
print("My list contains ",my_list)

# Using negative indexing to slice the list
# -1 refers to the last element, -2 to the second last, and so on.
sliced = my_list[-3:-1]  # Start at index -3 (30), end at index -1 (exclusive, so it doesn't include 50)

print(f"Sliced list from index -3 to -1 is : ",sliced) 
print()
