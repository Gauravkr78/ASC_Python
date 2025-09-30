# ----------------------------
# Basic Function
# ----------------------------
def greet():
    """Simple greeting function"""
    print("Hello, World!")

# Call the function
greet()

# ----------------------------
# Function with Parameters
# ----------------------------
def greet_person(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

greet_person("Alice")
greet_person("Bob")

# ----------------------------
# Function with Return Value
# ----------------------------
def add(a, b):
    """Add two numbers and return the result"""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")

# ----------------------------
# Function with Multiple Return Values
# ----------------------------
def calculate(a, b):
    """Perform multiple calculations and return sum, product, difference"""
    sum_result = a + b
    product = a * b
    difference = a - b
    return sum_result, product, difference

s, p, d = calculate(10, 5)
print(f"Sum: {s}, Product: {p}, Difference: {d}")

# ----------------------------
# Function with Default Parameters
# ----------------------------
def greet_with_prefix(name, prefix="Mr./Ms."):
    """Greet with a prefix, default is Mr./Ms."""
    print(f"Hello, {prefix} {name}!")

greet_with_prefix("John")
greet_with_prefix("Emily", "Dr.")

# ----------------------------
# Function with Keyword Arguments
# ----------------------------
def introduce(name, age):
    """Introduce a person"""
    print(f"My name is {name} and I am {age} years old.")

introduce(age=25, name="Sophia")
