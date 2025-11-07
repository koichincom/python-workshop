"""
04: Operators & Control Flow

- Arithmetic operators
- Comparison operators with if-else
- Logical operators with if-else
"""

# ------------------------------------------------------------------------------
# Arithmetic Operators
# ------------------------------------------------------------------------------

a = 10
b = 3

add = a + b
sub = a - b
mul = a * b
div = a / b
mod = a % b
exp = a**b

print(f"Addition: {add}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {mul}")
print(f"Division: {div}")
print(f"Modulus: {mod}")
print(f"Exponentiation: {exp}")

# ------------------------------------------------------------------------------
# Comparison Operators with if-else
# ------------------------------------------------------------------------------

x = 5
y = 10

# Using comparison with if-else
age = 20

if age >= 18:
    print("\nYou are an adult")
else:
    print("\nYou are a minor")

# if-elif-else for multiple conditions
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Score: {score}, Grade: {grade}")

# ------------------------------------------------------------------------------
# Logical Operators with if-else
# ------------------------------------------------------------------------------

age = 25
has_license = True

# AND - both conditions must be True
if age >= 18 and has_license:
    print("\nYou can drive")

# OR - at least one condition must be True
is_weekend = True
is_holiday = False

if is_weekend or is_holiday:
    print("No work today!")

# NOT - reverses the boolean value
is_raining = False

if not is_raining:
    print("Let's go outside!")
