def greet(name, greeting="Hello"):
    """Greet with optional custom greeting"""
    print(f"{greeting}, {name}!")


greet("Alice")  # Uses default greeting
greet("Bob", "Hi")  # Uses custom greeting
greet("Charlie", greeting="Hey")  # Keyword argument
