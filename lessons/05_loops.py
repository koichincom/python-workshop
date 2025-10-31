"""
Lesson 05: Loops
================

This lesson covers:
- for loops
- while loops
- break and continue
- range() function
- Nested loops
"""

# ============================================================
# for Loops
# ============================================================
print("=== for Loops ===")

# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(f"I like {fruit}")

# Loop through a string
message = "Python"
for letter in message:
    print(letter)

# ============================================================
# range() Function
# ============================================================
print("\n=== range() Function ===")
# range() generates a sequence of numbers

# range(stop) - from 0 to stop-1
print("range(5):")
for i in range(5):
    print(i, end=" ")
print()

# range(start, stop) - from start to stop-1
print("\nrange(2, 7):")
for i in range(2, 7):
    print(i, end=" ")
print()

# range(start, stop, step) - from start to stop-1, incrementing by step
print("\nrange(0, 10, 2):")
for i in range(0, 10, 2):
    print(i, end=" ")
print()

# Counting backwards
print("\nrange(10, 0, -1):")
for i in range(10, 0, -1):
    print(i, end=" ")
print()

# ============================================================
# while Loops
# ============================================================
print("\n\n=== while Loops ===")
# Runs as long as a condition is True

count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1

# Be careful with while loops - make sure the condition eventually becomes False!
# Otherwise, you'll create an infinite loop

# ============================================================
# break Statement
# ============================================================
print("\n=== break Statement ===")
# Exits the loop immediately

# Find the first number divisible by 7
for num in range(1, 100):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break

# Using break in a while loop
password = ""
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Enter password (hint: use 'secret'): ")
    attempts += 1

    if password == "secret":
        print("Access granted!")
        break
    else:
        print(f"Wrong password. {max_attempts - attempts} attempts remaining.")
else:
    # This else clause runs if the loop completes without break
    print("Too many failed attempts.")

# ============================================================
# continue Statement
# ============================================================
print("\n=== continue Statement ===")
# Skips the rest of the current iteration and moves to the next one

# Print only odd numbers
print("Odd numbers from 1 to 10:")
for num in range(1, 11):
    if num % 2 == 0:
        continue  # Skip even numbers
    print(num, end=" ")
print()

# Skip specific values
print("\nNumbers 1-10, skipping 5:")
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()

# ============================================================
# Nested Loops
# ============================================================
print("\n\n=== Nested Loops ===")

# Multiplication table
print("Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i}x{j}={i * j:2}", end="  ")
    print()  # New line after each row

# Pattern printing
print("\nTriangle pattern:")
for i in range(1, 6):
    for j in range(i):
        print("*", end=" ")
    print()

# ============================================================
# Loop with else Clause
# ============================================================
print("\n=== Loop with else Clause ===")
# The else clause runs when the loop completes normally (without break)

# Check if a number is prime
number = 17
is_prime = True

for i in range(2, number):
    if number % i == 0:
        print(f"{number} is not prime (divisible by {i})")
        is_prime = False
        break
else:
    print(f"{number} is prime!")

# ============================================================
# Practical Examples
# ============================================================
print("\n=== Practical Examples ===")

# Example 1: Sum of numbers
total = 0
for num in range(1, 11):
    total += num
print(f"Sum of 1 to 10: {total}")

# Example 2: Factorial
n = 5
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(f"{n}! = {factorial}")

# Example 3: Count down
print("\nCountdown:")
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast off!")

# Example 4: Find maximum in a list
numbers = [45, 23, 67, 12, 89, 34]
maximum = numbers[0]
for num in numbers:
    if num > maximum:
        maximum = num
print(f"\nMaximum number in {numbers}: {maximum}")

# Example 5: List filtering
print("\nEven numbers from list:")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for num in numbers:
    if num % 2 == 0:
        print(num, end=" ")
print()

# ============================================================
# enumerate() Function
# ============================================================
print("\n=== enumerate() Function ===")
# Get both index and value when looping

colors = ["red", "green", "blue"]
for index, color in enumerate(colors):
    print(f"Index {index}: {color}")

# Start counting from 1 instead of 0
print("\nStarting from 1:")
for index, color in enumerate(colors, start=1):
    print(f"Color {index}: {color}")

# ============================================================
# zip() Function
# ============================================================
print("\n=== zip() Function ===")
# Iterate over multiple lists simultaneously

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
cities = ["New York", "London", "Tokyo"]

for name, age, city in zip(names, ages, cities):
    print(f"{name} is {age} years old and lives in {city}")

# ============================================================
# Exercise for You
# ============================================================
# Try these:
# 1. Print the Fibonacci sequence up to the 10th number
# 2. Create a program that counts how many vowels are in a string
# 3. Print a multiplication table for a number of your choice
# 4. Create a number guessing game using a while loop
# 5. Print all numbers from 1 to 100, but for multiples of 3 print "Fizz",
#    for multiples of 5 print "Buzz", and for multiples of both print "FizzBuzz"

# Your code here:
