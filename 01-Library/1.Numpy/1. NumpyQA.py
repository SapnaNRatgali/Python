import numpy as np   # Importing the NumPy library for array operations

#-------------------------------------------------------------------
# 1. Convert the below list into numpy array then display the array Input: my_list = [1, 2, 3, 4, 5] 

my_list = [1, 2, 3, 4, 5]  # Defining the input list
arr = np.array(my_list)  # Creates a NumPy array from the list

print("Numpy Array list is:", arr) 

#-------------------------------------------------------------------

# 2. Convert the below list into a numpy array then display the array then display the first and last index and then multiply each element by 2 and display the result. Input: my_list = [1, 2, 3, 4, 5]

my_list = [1, 2, 3, 4, 5]  # Defining another input list
arr = np.array(my_list)  # Creates a NumPy array from the list
print("Numpy Array list is:", arr)  # Prints the array

print("First element:", arr[0])  # Prints the first element (index 0)
print("Last element:", arr[-1])   # Prints the last element (negative index -1)

res = arr * 2  # Element-wise multiplication of the array by 2
print("Array after multiplying each element by 2:", res)  # Prints the new array
