# List (mutable/changeable)

1. A list is like a container where you can store multiple items. 
2. It allows you to store multiple items (of the same or different data types) in a single variable so we can say lists are heterogeneous.
3. You can change what's inside the list, and you can access items using their position (index).
4. A list is one of the most versatile and commonly used data structures in Python.
5. Lists are dynamic, allowing them to grow or shrink as needed.
6. You can create a list using square brackets [] or the list() function.

Examples:

# Creating a list using square brackets
my_list = [10, 20, 30, 'apple', 3.14, True]

# When to use lists
1. Use lists when you need an ordered collection of elements that might change over time.
2. Ideal for situations where you need to frequently add, remove, or update elements.


# So, here are the names of the list methods:

append(), extend(), insert(), remove(), pop(), clear(), index(), count(),
sort(), reverse(), copy(), len()

# list operations:

Adding Elements: append(), extend(), insert()
Removing Elements: remove(), pop(), clear()
Accessing/Modifying: Indexing (my_list[index]), Slicing (my_list[start:end]), Updating (my_list[index] = value)
Searching: index(), count()
Sorting/Reversing: sort(), reverse()
Copying: copy()
List Arithmetic: Concatenation (+), Repetition (*)
Other: len(), in (membership check)
