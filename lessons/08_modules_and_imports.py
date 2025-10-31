"""
Lesson 08: Modules and Imports
===============================

This lesson covers:
- What are modules?
- Importing modules
- Creating your own modules
- Common built-in modules
- The standard library
"""

# ============================================================
# What are Modules?
# ============================================================
print("=== What are Modules? ===")
# A module is a file containing Python code (functions, classes, variables)
# Modules help organize code and promote reusability

# ============================================================
# Importing Built-in Modules
# ============================================================
print("\n=== Importing Built-in Modules ===")

# Method 1: Import entire module
import math

print(f"Pi: {math.pi}")
print(f"Square root of 16: {math.sqrt(16)}")
print(f"5 factorial: {math.factorial(5)}")

# Method 2: Import specific items
from math import ceil, floor

print(f"\nCeiling of 3.2: {ceil(3.2)}")
print(f"Floor of 3.8: {floor(3.8)}")

# Method 3: Import with alias
import datetime as dt

now = dt.datetime.now()
print(f"\nCurrent date and time: {now}")
print(f"Current year: {now.year}")

# Method 4: Import everything (not recommended for large modules)
# from math import *
# This imports all functions but can cause naming conflicts

# ============================================================
# Common Built-in Modules
# ============================================================
print("\n=== Common Built-in Modules ===")

# random - Generate random numbers
import random

print(f"Random integer (1-10): {random.randint(1, 10)}")
print(f"Random choice: {random.choice(['apple', 'banana', 'cherry'])}")

numbers = [1, 2, 3, 4, 5]
random.shuffle(numbers)
print(f"Shuffled list: {numbers}")

# datetime - Work with dates and times
from datetime import datetime, timedelta

today = datetime.now()
print(f"\nToday: {today.strftime('%Y-%m-%d %H:%M:%S')}")

tomorrow = today + timedelta(days=1)
print(f"Tomorrow: {tomorrow.strftime('%Y-%m-%d')}")

birthday = datetime(1990, 5, 15)
age = (today - birthday).days // 365
print(f"Age (if born May 15, 1990): {age} years")

# os - Operating system interface
import os

print(f"\nCurrent directory: {os.getcwd()}")
print(f"Directory contents: {os.listdir('.')[:5]}")  # First 5 items
print(f"Path separator: {os.sep}")

# sys - System-specific parameters
import sys

print(f"\nPython version: {sys.version}")
print(f"Platform: {sys.platform}")

# json - Work with JSON data
import json

# Python dict to JSON string
person = {"name": "Alice", "age": 25, "city": "New York"}
json_string = json.dumps(person)
print(f"\nJSON string: {json_string}")

# JSON string to Python dict
parsed = json.loads(json_string)
print(f"Parsed dict: {parsed}")

# ============================================================
# The math Module
# ============================================================
print("\n=== The math Module ===")

import math

# Constants
print(f"Pi: {math.pi}")
print(f"Euler's number: {math.e}")

# Basic operations
print(f"\nSquare root of 25: {math.sqrt(25)}")
print(f"2 to the power of 3: {math.pow(2, 3)}")
print(f"Absolute value of -5: {math.fabs(-5)}")

# Rounding
print(f"\nCeiling of 4.2: {math.ceil(4.2)}")
print(f"Floor of 4.8: {math.floor(4.8)}")

# Trigonometry (in radians)
angle = math.pi / 4  # 45 degrees
print(f"\nSin(45°): {math.sin(angle):.4f}")
print(f"Cos(45°): {math.cos(angle):.4f}")

# Logarithms
print(f"\nNatural log of e: {math.log(math.e)}")
print(f"Log base 10 of 100: {math.log10(100)}")

# ============================================================
# The random Module
# ============================================================
print("\n=== The random Module ===")

import random

# Random integers
print(f"Random int (1-100): {random.randint(1, 100)}")
print(f"Random int (0-9): {random.randrange(10)}")
print(f"Random even (0-10): {random.randrange(0, 11, 2)}")

# Random floats
print(f"\nRandom float [0,1): {random.random()}")
print(f"Random float (1-10): {random.uniform(1, 10)}")

# Random choices
colors = ["red", "green", "blue", "yellow"]
print(f"\nRandom color: {random.choice(colors)}")
print(f"Random sample (2): {random.sample(colors, 2)}")

# Shuffle
deck = list(range(1, 11))
print(f"\nOriginal deck: {deck}")
random.shuffle(deck)
print(f"Shuffled deck: {deck}")

# ============================================================
# The datetime Module
# ============================================================
print("\n=== The datetime Module ===")

from datetime import date, datetime, time, timedelta

# Current date and time
now = datetime.now()
print(f"Current datetime: {now}")
print(f"Year: {now.year}, Month: {now.month}, Day: {now.day}")
print(f"Hour: {now.hour}, Minute: {now.minute}, Second: {now.second}")

# Creating specific dates
specific_date = datetime(2025, 12, 31, 23, 59, 59)
print(f"\nNew Year's Eve 2025: {specific_date}")

# Date arithmetic
today = date.today()
one_week = timedelta(weeks=1)
next_week = today + one_week
print(f"\nToday: {today}")
print(f"Next week: {next_week}")

# Formatting dates
formatted = now.strftime("%B %d, %Y at %I:%M %p")
print(f"\nFormatted: {formatted}")

# Parsing dates
date_string = "2024-12-25"
parsed_date = datetime.strptime(date_string, "%Y-%m-%d")
print(f"Parsed date: {parsed_date}")

# ============================================================
# Creating Your Own Module
# ============================================================
print("\n=== Creating Your Own Module ===")

# To create a module:
# 1. Create a new .py file (e.g., my_utilities.py)
# 2. Add functions, classes, or variables
# 3. Import it in other files using: import my_utilities

# Example content for my_utilities.py:
"""
# my_utilities.py

def greet(name):
    return f"Hello, {name}!"

def add(a, b):
    return a + b

PI = 3.14159
"""

# Then in another file:
# import my_utilities
# print(my_utilities.greet("Alice"))
# print(my_utilities.add(5, 3))

# ============================================================
# Module Search Path
# ============================================================
print("\n=== Module Search Path ===")

import sys

print("Python searches for modules in these locations:")
for i, path in enumerate(sys.path[:5], 1):
    print(f"{i}. {path}")

# Python searches in this order:
# 1. Current directory
# 2. PYTHONPATH environment variable
# 3. Standard library directories
# 4. Site-packages (third-party packages)

# ============================================================
# The __name__ Variable
# ============================================================
print("\n=== The __name__ Variable ===")

# When a Python file is run directly, __name__ is set to "__main__"
# When it's imported as a module, __name__ is set to the module name

print(f"Current __name__: {__name__}")

# This pattern is commonly used:
"""
def main():
    # Your main program logic
    pass

if __name__ == "__main__":
    main()
"""

# This allows the file to be both:
# - Run as a standalone program
# - Imported as a module without running the main code

# ============================================================
# Package Management (pip)
# ============================================================
print("\n=== Package Management (pip) ===")

# pip is Python's package installer
# Use it to install third-party packages from PyPI (Python Package Index)

# Common pip commands (run in terminal, not in Python):
"""
pip install package_name      # Install a package
pip install package_name==1.0 # Install specific version
pip uninstall package_name    # Uninstall a package
pip list                      # List installed packages
pip show package_name         # Show package info
pip freeze                    # List all packages with versions
pip freeze > requirements.txt # Save dependencies to file
pip install -r requirements.txt # Install from requirements file
"""

# Popular packages to explore:
# - requests: HTTP library
# - numpy: Numerical computing
# - pandas: Data analysis
# - matplotlib: Data visualization
# - flask/django: Web frameworks

# ============================================================
# Practical Examples
# ============================================================
print("\n=== Practical Examples ===")

# Example 1: Generate a random password
import random
import string


def generate_password(length=12):
    """Generate a random password."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for _ in range(length))
    return password


print(f"Random password: {generate_password()}")

# Example 2: Calculate days until birthday
from datetime import date


def days_until_birthday(month, day):
    """Calculate days until next birthday."""
    today = date.today()
    birthday = date(today.year, month, day)

    if birthday < today:
        birthday = date(today.year + 1, month, day)

    days = (birthday - today).days
    return days


days = days_until_birthday(12, 25)  # Christmas
print(f"\nDays until Dec 25: {days}")


# Example 3: Dice roller simulator
def roll_dice(num_dice=2, num_sides=6):
    """Simulate rolling dice."""
    results = [random.randint(1, num_sides) for _ in range(num_dice)]
    return results, sum(results)


dice, total = roll_dice()
print(f"\nRolling 2 dice: {dice}, Total: {total}")

# ============================================================
# Exercise for You
# ============================================================
# Try these:
# 1. Create a module with utility functions (e.g., temperature converter)
# 2. Use the random module to create a number guessing game
# 3. Use datetime to calculate your age in days
# 4. Create a function that generates a random 6-digit PIN
# 5. Use math module to calculate the distance between two points
#    using the formula: sqrt((x2-x1)^2 + (y2-y1)^2)

# Your code here:
