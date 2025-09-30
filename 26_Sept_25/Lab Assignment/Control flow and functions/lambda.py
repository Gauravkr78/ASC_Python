# ==============================
# Lambda Functions – All Examples
# ==============================

# Basic Lambda vs Traditional Function
def square(x):
    """Return square of a number (Traditional Function)"""
    return x ** 2

# Lambda equivalent (short anonymous function)
square_lambda = lambda x: x ** 2

print("Traditional square(5):", square(5))      # 25
print("Lambda square_lambda(5):", square_lambda(5))  # 25

# Using lambda with map()
numbers = [1, 2, 3, 4, 5]

# Square each number
squared = list(map(lambda x: x ** 2, numbers))
print("\nSquared numbers (map):", squared)  # [1, 4, 9, 16, 25]

# Using lambda with filter()
numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Keep only even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers2))
print("Even numbers (filter):", even_numbers)  # [2, 4, 6, 8, 10]

# Using lambda with sorted()

words = ["apple", "banana", "cherry", "date"]

# Sort by length
sorted_words = sorted(words, key=lambda x: len(x))
print("Sorted by length:", sorted_words)
# ['date', 'apple', 'banana', 'cherry']

# Sort by second character
sorted_by_second = sorted(words, key=lambda x: x[1])
print("Sorted by second char:", sorted_by_second)
# ['banana', 'date', 'cherry', 'apple']
