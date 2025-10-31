"""
Lesson 02: Variables and Data Types
====================================

This lesson covers:
- Variables and assignment
- Basic data types (int, float, str, bool)
- Type checking
- Type conversion
"""

# ============================================================
# Variables
# ============================================================
# A variable is a named container that stores a value
# Variable naming rules:
# - Must start with a letter or underscore
# - Can contain letters, numbers, and underscores
# - Case-sensitive (age and Age are different)
# - Cannot use Python keywords (like print, if, for, etc.)

name = "Alice"
age = 25
height = 5.6
is_student = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student:", is_student)

# ============================================================
# Data Types
# ============================================================

# Integers (int) - Whole numbers
count = 10
temperature = -5
year = 2024

# Floating-point numbers (float) - Decimal numbers
price = 19.99
pi = 3.14159
temperature_celsius = 23.5

# Strings (str) - Text enclosed in quotes
message = "Hello, Python!"
single_quotes = "This works too"
multiline = """This is a
multi-line string"""

# Booleans (bool) - True or False
is_raining = False
is_sunny = True
has_completed = True

# ============================================================
# Checking Types
# ============================================================
print("\nType checking:")
print("Type of age:", type(age))
print("Type of price:", type(price))
print("Type of name:", type(name))
print("Type of is_student:", type(is_student))

# ============================================================
# Type Conversion (Casting)
# ============================================================
print("\nType conversion:")

# String to integer
num_string = "42"
num_int = int(num_string)
print(f"'{num_string}' as integer:", num_int)

# Integer to string
age_int = 25
age_string = str(age_int)
print(f"{age_int} as string:", age_string, "(type:", type(age_string), ")")

# String to float
price_string = "19.99"
price_float = float(price_string)
print(f"'{price_string}' as float:", price_float)

# Float to integer (truncates decimal part)
value = 3.7
value_int = int(value)
print(f"{value} as integer:", value_int)

# Integer to boolean (0 is False, non-zero is True)
print(f"bool(0) =", bool(0))
print(f"bool(42) =", bool(42))

# ============================================================
# Variable Reassignment
# ============================================================
print("\nVariable reassignment:")
x = 10
print("x =", x)
x = 20
print("x =", x)  # Variables can be changed

# Variables can even change type!
x = "Now I'm a string!"
print("x =", x)

# ============================================================
# Multiple Assignment
# ============================================================
print("\nMultiple assignment:")

# Assign multiple variables in one line
a, b, c = 1, 2, 3
print(f"a={a}, b={b}, c={c}")

# Assign same value to multiple variables
x = y = z = 0
print(f"x={x}, y={y}, z={z}")

# ============================================================
# Exercise for You
# ============================================================
# Try these:
# 1. Create variables for your name, age, and favorite number
# 2. Print them with descriptive labels
# 3. Check their types using type()
# 4. Convert your age to a string and concatenate it with other text

# Your code here:
