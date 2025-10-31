"""
Lesson 06: Functions
====================

This lesson covers:
- Defining functions
- Parameters and arguments
- Return values
- Default parameters
- Keyword arguments
- Variable-length arguments
- Scope
"""

# ============================================================
# Basic Function Definition
# ============================================================
print("=== Basic Function Definition ===")


def greet():
    """This is a simple function that prints a greeting."""
    print("Hello, World!")


# Call the function
greet()


# ============================================================
# Functions with Parameters
# ============================================================
print("\n=== Functions with Parameters ===")


def greet_person(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")


def add_numbers(a, b):
    """Adds two numbers and prints the result."""
    result = a + b
    print(f"{a} + {b} = {result}")


add_numbers(5, 3)
add_numbers(10, 20)


# ============================================================
# Return Values
# ============================================================
print("\n=== Return Values ===")


def multiply(a, b):
    """Multiplies two numbers and returns the result."""
    return a * b


result = multiply(4, 5)
print(f"4 * 5 = {result}")

# You can use the return value directly
print(f"6 * 7 = {multiply(6, 7)}")


def is_even(number):
    """Returns True if number is even, False otherwise."""
    return number % 2 == 0


print(f"Is 4 even? {is_even(4)}")
print(f"Is 7 even? {is_even(7)}")


# ============================================================
# Multiple Return Values
# ============================================================
print("\n=== Multiple Return Values ===")


def get_min_max(numbers):
    """Returns both minimum and maximum from a list."""
    return min(numbers), max(numbers)


nums = [5, 2, 9, 1, 7]
minimum, maximum = get_min_max(nums)
print(f"List: {nums}")
print(f"Min: {minimum}, Max: {maximum}")


# ============================================================
# Default Parameters
# ============================================================
print("\n=== Default Parameters ===")


def greet_with_title(name, title="Mr."):
    """Greets a person with an optional title."""
    print(f"Hello, {title} {name}!")


greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Overrides default
greet_with_title("Davis", "Ms.")


def power(base, exponent=2):
    """Raises base to the power of exponent (default is 2)."""
    return base**exponent


print(f"5^2 = {power(5)}")  # Uses default exponent
print(f"2^3 = {power(2, 3)}")  # Custom exponent


# ============================================================
# Keyword Arguments
# ============================================================
print("\n=== Keyword Arguments ===")


def describe_pet(animal_type, pet_name):
    """Displays information about a pet."""
    print(f"I have a {animal_type} named {pet_name}.")


# Positional arguments
describe_pet("dog", "Buddy")

# Keyword arguments (order doesn't matter)
describe_pet(pet_name="Whiskers", animal_type="cat")
describe_pet(animal_type="hamster", pet_name="Fluffy")


# ============================================================
# Variable-Length Arguments (*args)
# ============================================================
print("\n=== Variable-Length Arguments (*args) ===")


def sum_all(*numbers):
    """Sums any number of arguments."""
    total = 0
    for num in numbers:
        total += num
    return total


print(f"Sum of 1, 2, 3: {sum_all(1, 2, 3)}")
print(f"Sum of 10, 20, 30, 40: {sum_all(10, 20, 30, 40)}")
print(f"Sum of 5: {sum_all(5)}")


def print_names(*names):
    """Prints all names provided."""
    print("Names:")
    for name in names:
        print(f"  - {name}")


print_names("Alice", "Bob", "Charlie")


# ============================================================
# Keyword Variable-Length Arguments (**kwargs)
# ============================================================
print("\n=== Keyword Variable-Length Arguments (**kwargs) ===")


def print_info(**info):
    """Prints key-value pairs of information."""
    for key, value in info.items():
        print(f"{key}: {value}")


print_info(name="Alice", age=25, city="New York")
print()
print_info(product="Laptop", price=999, brand="TechCo")


# ============================================================
# Combining Different Parameter Types
# ============================================================
print("\n=== Combining Different Parameter Types ===")


def make_profile(name, age, *hobbies, **details):
    """Creates a user profile with various types of information."""
    print(f"Name: {name}")
    print(f"Age: {age}")

    if hobbies:
        print("Hobbies:")
        for hobby in hobbies:
            print(f"  - {hobby}")

    if details:
        print("Additional details:")
        for key, value in details.items():
            print(f"  {key}: {value}")


make_profile(
    "Alice", 25, "reading", "hiking", "coding", city="New York", occupation="Developer"
)


# ============================================================
# Variable Scope
# ============================================================
print("\n=== Variable Scope ===")

# Global variable
global_var = "I'm global"


def test_scope():
    # Local variable
    local_var = "I'm local"
    print(f"Inside function: {global_var}")
    print(f"Inside function: {local_var}")


test_scope()
print(f"Outside function: {global_var}")
# print(local_var)  # This would cause an error!

# Modifying global variables
counter = 0


def increment():
    global counter  # Declare that we want to use the global variable
    counter += 1


print(f"Counter: {counter}")
increment()
print(f"Counter: {counter}")
increment()
print(f"Counter: {counter}")


# ============================================================
# Lambda Functions (Anonymous Functions)
# ============================================================
print("\n=== Lambda Functions ===")


# Regular function
def square(x):
    return x**2


# Equivalent lambda function
square_lambda = lambda x: x**2

print(f"square(5) = {square(5)}")
print(f"square_lambda(5) = {square_lambda(5)}")

# Lambda with multiple arguments
multiply = lambda x, y: x * y
print(f"multiply(3, 4) = {multiply(3, 4)}")

# Lambdas are useful with functions like map(), filter(), sorted()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(f"Original: {numbers}")
print(f"Squared: {squared}")


# ============================================================
# Docstrings
# ============================================================
print("\n=== Docstrings ===")


def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Parameters:
    length (float): The length of the rectangle
    width (float): The width of the rectangle

    Returns:
    float: The area of the rectangle
    """
    return length * width


# Access docstring
print("Function docstring:")
print(calculate_area.__doc__)


# ============================================================
# Practical Examples
# ============================================================
print("\n=== Practical Examples ===")


def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit."""
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius."""
    return (fahrenheit - 32) * 5 / 9


temp_c = 25
temp_f = celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

temp_f = 77
temp_c = fahrenheit_to_celsius(temp_f)
print(f"{temp_f}°F = {temp_c}°C")


def is_palindrome(text):
    """Check if a string is a palindrome (reads same forwards and backwards)."""
    text = text.lower().replace(" ", "")
    return text == text[::-1]


print(f"Is 'racecar' a palindrome? {is_palindrome('racecar')}")
print(f"Is 'hello' a palindrome? {is_palindrome('hello')}")


def factorial(n):
    """Calculate factorial of n using recursion."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(f"5! = {factorial(5)}")


# ============================================================
# Exercise for You
# ============================================================
# Try these:
# 1. Create a function that checks if a number is prime
# 2. Write a function that takes a list and returns a new list with duplicates removed
# 3. Create a function that calculates the average of any number of arguments
# 4. Write a function that takes a string and returns it reversed
# 5. Create a function that generates the Fibonacci sequence up to n terms

# Your code here:
