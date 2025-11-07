"""
06: Functions

- Defining functions
- Parameters and arguments
- Return values
"""


# ------------------------------------------------------------------------------
# Basic Function
# ------------------------------------------------------------------------------


def greet():
    """A simple function that prints a greeting."""
    print("Hello, World!")


greet()


# ------------------------------------------------------------------------------
# Functions with Parameters
# ------------------------------------------------------------------------------


def greet_person(name):
    """Greets a person by name."""
    print(f"Hello, {name}!")


greet_person("Alice")
greet_person("Bob")


# ------------------------------------------------------------------------------
# Functions with Return Values
# ------------------------------------------------------------------------------


def add(a, b):
    """Adds two numbers and returns the result."""
    return a + b


result = add(5, 3)
print(f"\n5 + 3 = {result}")


# ------------------------------------------------------------------------------
# Functions with Default Parameters
# ------------------------------------------------------------------------------


def power(base, exponent=2):
    """Raises base to the power of exponent (default is 2)."""
    return base**exponent


print(f"5^2 = {power(5)}")  # Uses default exponent
print(f"2^3 = {power(2, 3)}")  # Custom exponent
