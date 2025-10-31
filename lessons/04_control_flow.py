"""
Lesson 04: Control Flow
========================

This lesson covers:
- if statements
- if-else statements
- if-elif-else statements
- Nested conditionals
- Ternary operator
"""

# ============================================================
# Basic if Statement
# ============================================================
print("=== Basic if Statement ===")

age = 20

if age >= 18:
    print("You are an adult.")
    print("You can vote!")

# The indented code only runs if the condition is True
# Note: Python uses indentation (4 spaces) to define code blocks

# ============================================================
# if-else Statement
# ============================================================
print("\n=== if-else Statement ===")

temperature = 15

if temperature > 20:
    print("It's warm outside!")
else:
    print("It's cold outside!")

# ============================================================
# if-elif-else Statement
# ============================================================
print("\n=== if-elif-else Statement ===")
# elif = "else if"
# Use when you have multiple conditions to check

score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# ============================================================
# Multiple Conditions
# ============================================================
print("\n=== Multiple Conditions ===")

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
elif age >= 18 and not has_license:
    print("You're old enough, but you need a license.")
else:
    print("You're too young to drive.")

# Using 'or'
day = "Saturday"

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")
else:
    print("It's a weekday.")

# ============================================================
# Nested if Statements
# ============================================================
print("\n=== Nested if Statements ===")

username = "admin"
password = "secret123"

if username == "admin":
    if password == "secret123":
        print("Access granted!")
    else:
        print("Incorrect password.")
else:
    print("Username not found.")

# ============================================================
# Checking Multiple Values
# ============================================================
print("\n=== Checking Multiple Values ===")

fruit = "apple"

# Using 'in' keyword
if fruit in ["apple", "banana", "orange"]:
    print(f"{fruit} is available!")

# Checking if NOT in a list
favorite_color = "green"
available_colors = ["red", "blue", "yellow"]

if favorite_color not in available_colors:
    print(f"Sorry, {favorite_color} is not available.")

# ============================================================
# Ternary Operator (Conditional Expression)
# ============================================================
print("\n=== Ternary Operator ===")
# A shorthand way to write simple if-else statements

age = 20
status = "adult" if age >= 18 else "minor"
print(f"Status: {status}")

# Equivalent to:
# if age >= 18:
#     status = "adult"
# else:
#     status = "minor"

# Another example
num = 7
result = "even" if num % 2 == 0 else "odd"
print(f"{num} is {result}")

# ============================================================
# Truthy and Falsy Values
# ============================================================
print("\n=== Truthy and Falsy Values ===")
# In Python, some values are considered "falsy" in boolean context:
# - False, None, 0, 0.0, empty string "", empty list [], empty dict {}

name = ""
if name:
    print(f"Hello, {name}!")
else:
    print("No name provided.")

count = 0
if count:
    print(f"Count is {count}")
else:
    print("Count is zero or empty")

# ============================================================
# Practical Examples
# ============================================================
print("\n=== Practical Examples ===")

# Example 1: Number sign checker
num = -5
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# Example 2: Login attempt counter
login_attempts = 3
max_attempts = 3

if login_attempts >= max_attempts:
    print("Account locked. Too many failed attempts.")
elif login_attempts >= max_attempts - 1:
    print(f"Warning: Only {max_attempts - login_attempts} attempt remaining!")
else:
    print(f"You have {max_attempts - login_attempts} attempts remaining.")

# Example 3: Discount calculator
purchase_amount = 150
has_coupon = True

if purchase_amount >= 100 and has_coupon:
    discount = 0.20
    print("20% discount applied!")
elif purchase_amount >= 100:
    discount = 0.10
    print("10% discount applied!")
elif has_coupon:
    discount = 0.05
    print("5% discount applied!")
else:
    discount = 0
    print("No discount available.")

final_price = purchase_amount * (1 - discount)
print(f"Final price: ${final_price:.2f}")

# ============================================================
# Exercise for You
# ============================================================
# Try these:
# 1. Write a program that checks if a number is positive, negative, or zero
# 2. Create a simple calculator that takes two numbers and an operator (+, -, *, /)
# 3. Write a program that determines if a year is a leap year
#    (divisible by 4, but not by 100, unless also divisible by 400)
# 4. Create a grade calculator that converts a percentage to a letter grade

# Your code here:
