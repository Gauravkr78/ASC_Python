def greet():
    """Simple greeting function"""
    print("Hello, World!")

# Call the function
greet()



def greet(name):
    """Greet a specific person"""
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")


def add(a, b):
    """Add two numbers and return the result"""
    return a + b

result = add(5, 3)
print(f"5 + 3 = {result}")


# Multiple return values
def calculate(a, b):
    """Perform multiple calculations"""
    sum_result = a + b
    product = a * b
    difference = a - b
    return sum_result, product, difference

s, p, d = calculate(10, 5)
print(f"Sum: {s}, Product: {p}, Difference: {d}")
