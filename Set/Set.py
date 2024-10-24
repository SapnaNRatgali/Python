

# Defining two lists
li1 = [1, 2, 5, 3, 7, 1]
li2 = [1.5, 2.6, 5.8, 3.9, 7.9, 1.3]
print("List 1:", li1)
print("List 2:", li2)

# Defining two tuples (Corrected to tuples)
tup1 = (5, 24, 4, 24, 1, 6, 5)  # Correct tuple definition
tup2 = (5.0, 24.1, 4.9, 24, 1.3, 6.5, 5.0)  # Correct tuple definition
print("\nTuple 1:", tup1)
print("Tuple 2:", tup2)

# Defining two sets (Duplicate values automatically removed in sets)
se1 = {1, 5, 8, 6, 4}  # Duplicate 1 is automatically removed
se2 = {1.5, 5.6, 8.8, 6.5, 4.6}  # Duplicate 1.5 is automatically removed
print("\nSet 1:", se1)
print("Set 2:", se2)

print("\n")  # Adding space for clarity

# Set Operations

# Union of sets a and b (Combines elements of both sets, removes duplicates)
a = {12, 13, 14, 15}
b = {14, 15, 16, 17}
print("Set a:", a)
print("Set b:", b)
print("Union of a and b:", a | b)  # or use a.union(b)

print("\n")

# Intersection of sets a and b (Elements common to both sets)
print("Intersection of a and b:", a & b)  # or use a.intersection(b)

print("\n")

# Difference of sets (Elements present in one set but not the other)
print("Difference of a and b (a - b):", a - b)
print("Difference of b and a (b - a):", b - a)

print("\n")

# Symmetric Difference (Elements present in either set, but not both)
print("Symmetric difference of a and b:", a ^ b)  # or use a.symmetric_difference(b)

print("\n")

# ---------------------------------------------
# Additional Set Operations

# Checking if a set is a subset of another set
# A set is a subset if all its elements are contained in another set.
a = {1, 2, 3}
b = {1, 2, 3, 4, 5}
print("Set a:", a)
print("Set b:", b)
print("Is a a subset of b?", a.issubset(b))
print("Is b a subset of a?", b.issubset(a))

print("\n")

# Checking if a set is a superset of another set
# A set is a superset if it contains all the elements of another set.
print("Is b a superset of a?", b.issuperset(a))
print("Is a a superset of b?", a.issuperset(b))

print("\n")

# Checking if two sets are disjoint
# Two sets are disjoint if they have no elements in common.
a = {1, 2, 3}
c = {4, 5, 6}
print("Set a:", a)
print("Set c:", c)
print("Are a and c disjoint?", a.isdisjoint(c))

print("\n")

# ---------------------------------------------
# Methods related to sets

# 1. add() - Adds an element to the set
a = {1, 2, 3, 4}
print("Initial set a:", a)
a.add(5)
print("After adding 5, set a becomes:", a)

print("\n")

# 2. clear() - Removes all elements from the set, making it empty
mset = {1, 2, 3}
print("Initial set mset:", mset)
mset.clear()
print("After clearing, set mset becomes:", mset)

print("\n")

# 3. remove() - Removes the specified element from the set. Raises KeyError if not found.
b = {1, 2, 3, 4}
print("Initial set b:", b)
b.remove(2)  # Removes 2 from the set
print("After removing 2, set b becomes:", b)
# Uncommenting the next line would raise an error since 2 is already removed:
# b.remove(2)

print("\n")

# 4. discard() - Removes the specified element if present. Does not raise an error if not found.
b = {1, 2, 3, 4}
print("Initial set b:", b)
b.discard(2)  # Removes 2 from the set
print("After discarding 2, set b becomes:", b)
b.discard(2)  # Does nothing since 2 is already removed
print("After discarding 2 again, set b remains:", b)

print("\n")

# 5. pop() - Removes and returns an arbitrary element from the set. Raises KeyError if empty.
print("Initial set b:", b)
element = b.pop()  # Removes and returns an arbitrary element
print("After popping an element, set b becomes:", b)
print("Popped element:", element)

print("\n")

# 6. copy() - Returns a shallow copy of the set
b_copy = b.copy()
print("Original set b:", b)
print("Copied set:", b_copy)

print("\n")





