PI = 3.14

# Function to add two numbers
def add(a, b):
    """Return the sum of a and b"""
    return a + b

# Function to multiply two numbers
def multiply(a, b):
    """Return the product of a and b"""
    return a * b

# Function to check if number is even
def is_even(number):
    """Return True if number is even"""
    return number % 2 == 0

# This code runs only when the module is executed directly
if __name__ == "__main__":
    print("Testing simple_math module:")
    print(f"add(5, 3) = {add(5, 3)}")
    print(f"multiply(4, 5) = {multiply(4, 5)}")
    print(f"is_even(10) = {is_even(10)}")
    print(f"PI = {PI}")
"""
MODULES EXPLANATION:

- Modules are reusable Python files
- import: bring module functions into your program
- from module import function: import specific functions
- __name__ == "__main__": code that runs only when file is executed directly
"""

def simple_module_demo():
    # Import the entire module
    import simple_math as math

    # Use module functions
    result1 = math.add(10, 5)
    result2 = math.multiply(3, 7)

    print("Using simple_math module:")
    print(f"10 + 5 = {result1}")
    print(f"3 * 7 = {result2}")
    print(f"Is 8 even? {math.is_even(8)}")
    print(f"PI value: {math.PI}")

    # Import specific functions only
    from simple_math import add, is_even

    # Now we can use them directly
    print(f"\nDirect import: 20 + 15 = {add(20, 15)}")
    print(f"Is 7 even? {is_even(7)}")

# Run the module demo
simple_module_demo()
