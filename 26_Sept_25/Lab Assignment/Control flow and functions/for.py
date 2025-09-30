# ----------------------------
# Take user input to create a list
# ----------------------------
fruits = []  # empty list to store fruits
n = int(input("How many fruits do you want to enter? "))

# Loop to take n inputs
for i in range(n):
    fruit = input(f"Enter fruit {i+1}: ")
    fruits.append(fruit)

# Display the list
print("\nYour fruit list:")
for fruit in fruits:
    print(fruit)

# ----------------------------
# Iterating through a string
# ----------------------------
word = input("\nEnter a word to iterate through its characters: ")
print("Characters in the word:")
for char in word:
    print(char)

# ----------------------------
# Using range() with user-defined numbers
# ----------------------------
start = int(input("\nEnter start number for range: "))
end = int(input("Enter end number for range: "))
step = int(input("Enter step value: "))

print(f"Numbers from {start} to {end} with step {step}:")
for i in range(start, end, step):
    print(i)
# ----------------------------
# Using range() - Basic examples
# ----------------------------

# Basic range: 0 to 4
print("\nBasic range 0 to 4:")
for i in range(5):
    print(i)

# Range with start and end: 2 to 5
print("\nRange from 2 to 5:")
for i in range(2, 6):
    print(i)

# Range with step: 0, 2, 4, 6, 8
print("\nRange with step 2 (0 to 8):")
for i in range(0, 10, 2):
    print(i)

# Descending range: 5, 4, 3, 2, 1
print("\nDescending range from 5 to 1:")
for i in range(5, 0, -1):
    print(i)