# Logical AND - " and  "
# This operator is used to combine two or more conditional statements, and it returns True only if all the conditions are true.

print(True and False)   
print()

print(5 > 3 and 4 > 2)  
print()

# And (True if both are True)
print(a and b)  # Since a = 0 (False) and b = 25 (True), result = 0
print()

# different scenarios

# 1. Both True:

a = 5
b = 10
result = (a > 0) and (b > 0)
print(result)

# output:  True
# (Both conditions are True, so the result is True.)


One False:

python
Copy code
a = -5
b = 10
result = (a > 0) and (b > 0)
print(result)
Output:

graphql
Copy code
False
(Since a > 0 is False, the whole expression is False.)

Short-circuiting:

python
Copy code
a = 5
b = -10
result = (a > 0) and (b > 0)
print(result)
Output:

graphql
Copy code
False
(When the first condition is True, Python evaluates the second condition. Since b > 0 is False, the result is False.)
