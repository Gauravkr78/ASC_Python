# ----------------------------
# Function with Optional Parameters
# ----------------------------
def greet(name, greeting="Hello"):
    """Greet with an optional custom greeting"""
    print(f"{greeting}, {name}!")

# Using default greeting
greet("Alice")

# Using custom greeting
greet("Bob", "Hi")

# Using keyword argument
greet("Charlie", greeting="Hey")


# ----------------------------
# Function with Keyword Arguments
# ----------------------------
def create_person(name, age=0, city="Unknown", country="Unknown"):
    """
    Create a person dictionary with flexible parameters.
    Default values are provided for age, city, and country.
    """
    return {
        "name": name,
        "age": age,
        "city": city,
        "country": country
    }

# Different ways to call the function
person1 = create_person("Alice")  # Only mandatory argument
person2 = create_person("Bob", age=25)  # Using positional argument for age
person3 = create_person("Charlie", country="USA")  # Using keyword argument
person4 = create_person("David", age=30, city="London", country="UK")  # All arguments

# Display the created persons
print("\nPerson 1:", person1)
print("Person 2:", person2)
print("Person 3:", person3)
print("Person 4:", person4)
