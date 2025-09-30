# Basic function
def greet(name):
    """This function greets the person passed as parameter"""
    return f"Hello, {name}! Welcome to Python."


# Function with multiple parameters
def calculate_area(length, width):
    """Calculate area of a rectangle"""
    area = length * width
    return area


# Function with default parameters
def introduce(name, age, city="Unknown"):
    """Introduce a person with optional city"""
    return f"Name: {name}, Age: {age}, City: {city}"


# Using the functions
print(greet("Alice"))
print(f"Area of rectangle: {calculate_area(10, 5)}")
print(introduce("Bob", 25))
print(introduce("Charlie", 30, "London"))


# Function that returns multiple values
def circle_calculations(radius):
    """Calculate diameter, circumference, and area of a circle"""
    diameter = 2 * radius
    circumference = 2 * 3.14159 * radius
    area = 3.14159 * radius ** 2
    return diameter, circumference, area


d, c, a = circle_calculations(7)
print(f"Circle with radius 7: Diameter={d}, Circumference={c:.2f}, Area={a:.2f}")
