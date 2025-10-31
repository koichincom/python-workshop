"""
Lesson 07: Data Structures
===========================

This lesson covers:
- Lists
- Tuples
- Dictionaries
- Sets
- List comprehensions
"""

# ============================================================
# Lists
# ============================================================
print("=== Lists ===")
# Lists are ordered, mutable collections

# Creating lists
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "hello", 3.14, True]
empty_list = []

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")
print(f"Mixed types: {mixed}")

# Accessing elements (0-indexed)
print(f"\nFirst fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")  # Negative index counts from end
print(f"Second fruit: {fruits[1]}")

# Slicing
print(f"\nFirst two numbers: {numbers[0:2]}")
print(f"Last three numbers: {numbers[-3:]}")
print(f"Every other number: {numbers[::2]}")

# Modifying lists
fruits[1] = "blueberry"
print(f"\nAfter modification: {fruits}")

# Adding elements
fruits.append("orange")  # Add to end
print(f"After append: {fruits}")

fruits.insert(1, "mango")  # Insert at index
print(f"After insert: {fruits}")

# Removing elements
fruits.remove("cherry")  # Remove by value
print(f"After remove: {fruits}")

last_fruit = fruits.pop()  # Remove and return last item
print(f"Popped: {last_fruit}, Remaining: {fruits}")

# List methods
numbers = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"\nOriginal: {numbers}")
print(f"Length: {len(numbers)}")
print(f"Count of 1: {numbers.count(1)}")
print(f"Index of 4: {numbers.index(4)}")

numbers.sort()
print(f"Sorted: {numbers}")

numbers.reverse()
print(f"Reversed: {numbers}")

# List concatenation and repetition
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print(f"\nCombined: {combined}")

repeated = [0] * 5
print(f"Repeated: {repeated}")

# Checking membership
print(f"\nIs 5 in numbers? {5 in numbers}")
print(f"Is 10 in numbers? {10 in numbers}")

# ============================================================
# Tuples
# ============================================================
print("\n=== Tuples ===")
# Tuples are ordered, immutable collections

# Creating tuples
coordinates = (3, 4)
person = ("Alice", 25, "New York")
single_item = (42,)  # Note the comma!
empty_tuple = ()

print(f"Coordinates: {coordinates}")
print(f"Person: {person}")

# Accessing elements (same as lists)
print(f"\nName: {person[0]}")
print(f"Age: {person[1]}")
print(f"City: {person[2]}")

# Unpacking
x, y = coordinates
print(f"\nx = {x}, y = {y}")

name, age, city = person
print(f"Unpacked: {name}, {age}, {city}")

# Tuples are immutable
# coordinates[0] = 5  # This would cause an error!

# But you can create a new tuple
new_coordinates = (5, 6)
print(f"\nNew coordinates: {new_coordinates}")

# When to use tuples vs lists:
# - Use tuples for data that shouldn't change (like coordinates, RGB colors)
# - Use lists for data that might be modified

# ============================================================
# Dictionaries
# ============================================================
print("\n=== Dictionaries ===")
# Dictionaries are unordered collections of key-value pairs

# Creating dictionaries
student = {"name": "Alice", "age": 20, "major": "Computer Science", "gpa": 3.8}

print(f"Student: {student}")

# Accessing values
print(f"\nName: {student['name']}")
print(f"Major: {student['major']}")

# Using get() method (safer - returns None if key doesn't exist)
print(f"Age: {student.get('age')}")
print(f"Grade: {student.get('grade', 'Not found')}")  # Default value

# Modifying dictionaries
student["age"] = 21  # Update existing key
student["graduation_year"] = 2025  # Add new key
print(f"\nUpdated student: {student}")

# Removing items
del student["gpa"]
print(f"After deletion: {student}")

removed_value = student.pop("graduation_year")
print(f"Popped value: {removed_value}")
print(f"After pop: {student}")

# Dictionary methods
print(f"\nKeys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")

# Looping through dictionaries
print("\nLooping through dictionary:")
for key, value in student.items():
    print(f"  {key}: {value}")

# Checking membership
print(f"\nIs 'name' a key? {'name' in student}")
print(f"Is 'Alice' a value? {'Alice' in student.values()}")

# Nested dictionaries
students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22},
    "student3": {"name": "Charlie", "age": 21},
}

print(f"\nNested dictionary: {students}")
print(f"Student1 name: {students['student1']['name']}")

# ============================================================
# Sets
# ============================================================
print("\n=== Sets ===")
# Sets are unordered collections of unique elements

# Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 5}
empty_set = set()  # Note: {} creates an empty dict, not set!

print(f"Fruits: {fruits}")
print(f"Numbers: {numbers}")

# Sets automatically remove duplicates
numbers_with_duplicates = {1, 2, 2, 3, 3, 3, 4, 5}
print(f"\nWith duplicates: {numbers_with_duplicates}")

# Adding and removing
fruits.add("orange")
print(f"After add: {fruits}")

fruits.remove("banana")  # Raises error if not found
print(f"After remove: {fruits}")

fruits.discard("mango")  # Doesn't raise error if not found
print(f"After discard: {fruits}")

# Set operations
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print(f"\nSet1: {set1}")
print(f"Set2: {set2}")
print(f"Union: {set1 | set2}")  # All elements from both
print(f"Intersection: {set1 & set2}")  # Common elements
print(f"Difference: {set1 - set2}")  # In set1 but not set2
print(f"Symmetric difference: {set1 ^ set2}")  # In either but not both

# Checking membership (very fast for sets!)
print(f"\nIs 3 in set1? {3 in set1}")

# ============================================================
# List Comprehensions
# ============================================================
print("\n=== List Comprehensions ===")
# A concise way to create lists

# Traditional way
squares = []
for x in range(10):
    squares.append(x**2)
print(f"Squares (traditional): {squares}")

# List comprehension
squares = [x**2 for x in range(10)]
print(f"Squares (comprehension): {squares}")

# With condition
evens = [x for x in range(20) if x % 2 == 0]
print(f"Even numbers: {evens}")

# String manipulation
words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(f"Uppercase: {upper_words}")

# Nested comprehension (2D list)
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
print(f"\nMultiplication table:")
for row in matrix:
    print(row)

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(1, 6)}
print(f"\nSquares dictionary: {squares_dict}")

# Set comprehension
unique_lengths = {len(word) for word in words}
print(f"Unique word lengths: {unique_lengths}")

# ============================================================
# Practical Examples
# ============================================================
print("\n=== Practical Examples ===")

# Example 1: Shopping cart
cart = {"apple": 1.50, "banana": 0.75, "bread": 2.50, "milk": 3.00}

print("Shopping cart:")
total = 0
for item, price in cart.items():
    print(f"  {item}: ${price:.2f}")
    total += price
print(f"Total: ${total:.2f}")

# Example 2: Word frequency counter
text = "hello world hello python world"
words = text.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(f"\nWord frequencies: {word_count}")

# Example 3: Finding common elements
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common = list(set(list1) & set(list2))
print(f"\nCommon elements: {common}")

# Example 4: Removing duplicates while preserving order
numbers = [1, 2, 2, 3, 4, 4, 5, 5, 5]
unique = []
seen = set()
for num in numbers:
    if num not in seen:
        unique.append(num)
        seen.add(num)
print(f"\nOriginal: {numbers}")
print(f"Unique (ordered): {unique}")

# ============================================================
# Exercise for You
# ============================================================
# Try these:
# 1. Create a function that merges two dictionaries
# 2. Write a program that finds the second largest number in a list
# 3. Create a phone book using a dictionary (name: phone_number)
# 4. Use a list comprehension to create a list of all numbers from 1-100
#    that are divisible by both 3 and 5
# 5. Create a function that takes two lists and returns their intersection

# Your code here:
