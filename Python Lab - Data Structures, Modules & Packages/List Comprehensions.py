# 1. Squares numbers 1-10
squares = [x**2 for x in range(1, 11)]
print("1. Squares of 1-10:", squares)

# 2. Extracts even numbers from a list
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = [x for x in nums if x % 2 == 0]
print("2. Even numbers:", evens)

# 3. Converts strings to uppercase
words = ["hello", "world", "python"]
uppercased = [word.upper() for word in words]
print("3. Uppercased words:", uppercased)

# 4. Filters out negative numbers
numbers = [-5, 3, -1, 7, 0, -2]
non_negatives = [x for x in numbers if x >= 0]
print("4. Non-negative numbers:", non_negatives)

# 5. Gets the length of each word in a list
word_list = ["apple", "banana", "cherry"]
lengths = [len(word) for word in word_list]
print("5. Lengths of words:", lengths)

# 6. Creates pairs (number, square)
pairs = [(x, x**2) for x in range(1, 11)]
print("6. Pairs (number, square):", pairs)

# 7. Extracts first characters of words
phrases = ["data", "science", "rocks"]
first_chars = [word[0] for word in phrases]
print("7. First characters:", first_chars)

# 8. Multiplies each element by 3
values = [2, 4, 6, 8]
tripled = [x * 3 for x in values]
print("8. Tripled values:", tripled)

# 9. Removes vowels from strings
text = "list comprehensions are powerful"
no_vowels = ''.join([char for char in text if char.lower() not in 'aeiou'])
print("9. Text without vowels:", no_vowels)

# 10. Creates a list of tuples (index, value)
items = ["a", "b", "c", "d"]
indexed = [(i, item) for i, item in enumerate(items)]
print("10. Indexed tuples:", indexed)
