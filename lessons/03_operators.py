"""
Lesson 03: Operators
====================

This lesson covers:
- Arithmetic operators
- Comparison operators
- Logical operators
- Assignment operators
"""

# ============================================================
# Arithmetic Operators
# ============================================================
print("=== Arithmetic Operators ===")

a = 10
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition: {a} + {b} = {a + b}")
print(f"Subtraction: {a} - {b} = {a - b}")
print(f"Multiplication: {a} * {b} = {a * b}")
print(f"Division: {a} / {b} = {a / b}")  # Always returns float
print(f"Floor Division: {a} // {b} = {a // b}")  # Rounds down to nearest integer
print(f"Modulus (remainder): {a} % {b} = {a % b}")
print(f"Exponentiation: {a} ** {b} = {a**b}")  # a to the power of b

# ============================================================
# Comparison Operators
# ============================================================
print("\n=== Comparison Operators ===")
# These return True or False

x = 5
y = 10

print(f"x = {x}, y = {y}")
print(f"Equal to: x == y is {x == y}")
print(f"Not equal to: x != y is {x != y}")
print(f"Greater than: x > y is {x > y}")
print(f"Less than: x < y is {x < y}")
print(f"Greater than or equal: x >= y is {x >= y}")
print(f"Less than or equal: x <= y is {x <= y}")

# ============================================================
# Logical Operators
# ============================================================
print("\n=== Logical Operators ===")
# Used to combine conditional statements

p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")  # True if both are True
print(f"p or q: {p or q}")  # True if at least one is True
print(f"not p: {not p}")  # Reverses the boolean value

# Practical examples
age = 20
has_license = True

print(f"\nPractical examples:")
print(f"Age: {age}, Has license: {has_license}")
print(f"Can drive (age >= 18 and has_license): {age >= 18 and has_license}")

temperature = 25
print(f"Temperature: {temperature}°C")
print(f"Comfortable (20 <= temp <= 26): {20 <= temperature <= 26}")

# ============================================================
# Assignment Operators
# ============================================================
print("\n=== Assignment Operators ===")

# Basic assignment
num = 10
print(f"num = {num}")

# Compound assignment operators
num += 5  # Same as: num = num + 5
print(f"After num += 5: {num}")

num -= 3  # Same as: num = num - 3
print(f"After num -= 3: {num}")

num *= 2  # Same as: num = num * 2
print(f"After num *= 2: {num}")

num //= 4  # Same as: num = num // 4
print(f"After num //= 4: {num}")

num %= 3  # Same as: num = num % 3
print(f"After num %= 3: {num}")

# ============================================================
# Operator Precedence
# ============================================================
print("\n=== Operator Precedence ===")
# Python follows the standard mathematical order of operations:
# 1. Parentheses ()
# 2. Exponentiation **
# 3. Multiplication, Division, Floor Division, Modulus *, /, //, %
# 4. Addition, Subtraction +, -

result1 = 2 + 3 * 4
print(f"2 + 3 * 4 = {result1}")  # Multiplication first

result2 = (2 + 3) * 4
print(f"(2 + 3) * 4 = {result2}")  # Parentheses first

result3 = 10 + 5 * 2 - 3
print(f"10 + 5 * 2 - 3 = {result3}")

# ============================================================
# String Operators
# ============================================================
print("\n=== String Operators ===")

first_name = "John"
last_name = "Doe"

# Concatenation (joining strings)
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Repetition
laugh = "ha" * 3
print(f"Laugh: {laugh}")

line = "=" * 30
print(line)

# ============================================================
# Exercise for You
# ============================================================
# Try these:
# 1. Calculate the area of a rectangle (length * width)
# 2. Calculate the average of three numbers
# 3. Check if a number is even (hint: use modulus operator)
# 4. Create a program that converts temperature from Celsius to Fahrenheit
#    Formula: F = (C * 9/5) + 32

# Your code here:
