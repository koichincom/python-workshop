"""
03: Data Structures

- Lists
- Dictionaries
- Tuples
"""

# ------------------------------------------------------------------------------
# Lists
# ------------------------------------------------------------------------------

fruits = ["apple", "banana", "cherry"]
print(f"Fruits: {fruits}")

# Accessing elements (0-indexed)
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Modifying lists
fruits.append("orange")  # Add to end
print(f"After append: {fruits}")

fruits[1] = "blueberry"  # Change element
print(f"After modification: {fruits}")

# ------------------------------------------------------------------------------
# Dictionaries
# ------------------------------------------------------------------------------

student = {"name": "Alice", "age": 20, "major": "Computer Science"}

print(f"\nStudent: {student}")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")

# Adding/modifying entries
student["gpa"] = 3.8
print(f"Updated: {student}")

# ------------------------------------------------------------------------------
# Tuples
# ------------------------------------------------------------------------------

coordinates = (3, 4)
print(f"\nCoordinates: {coordinates}")
print(f"X: {coordinates[0]}, Y: {coordinates[1]}")

# Tuples cannot be modified (immutable)
# coordinates[0] = 5  # This would cause an error!
