"""
05: Loops

- for loops
- range() function
- Iterating through lists and dictionaries
- while loops
"""

# ------------------------------------------------------------------------------
# For Loops with range()
# ------------------------------------------------------------------------------

# range(stop) - from 0 to stop-1
for i in range(5):
    print(f"Count: {i}")


# range(start, stop)
print("\nCounting 1 to 5:")
for i in range(1, 6):
    print(i)

# ------------------------------------------------------------------------------
# Iterating Through Lists
# ------------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]

print("\nFruits:")
for fruit in fruits:
    print(f"- {fruit}")

# ------------------------------------------------------------------------------
# Iterating Through Dictionaries
# ------------------------------------------------------------------------------

student = {"name": "Alice", "age": 20, "major": "Computer Science"}

print("\nStudent info:")
for key, value in student.items():
    print(f"{key}: {value}")

# ------------------------------------------------------------------------------
# While Loops
# ------------------------------------------------------------------------------

count = 1
print("\nCounting with while:")
while count <= 5:
    print(count)
    count += 1
