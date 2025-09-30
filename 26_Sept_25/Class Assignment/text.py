# Using single quotes around text that contains double quotes
print('She said "Welcome to Python!"')

# Using double quotes around text that contains single quotes
print("It's a beautiful day to learn Python")

# Escaping double quotes inside double-quoted string
print("He shouted \"Python is awesome!\" loudly")

# Escaping single quotes inside single-quoted string
print('It\'s amazing to code in Python')

# Using triple quotes for both single and double quotes
print("""He said 'Hello' and also "Welcome" to everyone""")

# -------------------------------
# Concatenation of strings
# -------------------------------
str1 = "Python"
str2 = "Programming"
result = str1 + " " + str2  # Concatenation
print("Concatenation Result:", result)

# -------------------------------
# Repetition of string (* operator)
# -------------------------------
repeat_str = str1 * 3  # Repeats 'Python' 3 times
print("Repetition Result:", repeat_str)

# -------------------------------
# Slicing of strings
# -------------------------------
text = "WelcomeToPython"
print("Original text:", text)

# Get first 7 characters
print("First 7 chars:", text[:7])

# Get characters from index 7 to end
print("From index 7 to end:", text[7:])

# Get characters from index 3 to 10
print("Index 3 to 10:", text[3:10])

# Get every second character
print("Every 2nd char:", text[::2])

# Reverse the string
print("Reversed text:", text[::-1])
