# For loop examples

print("Counting from 1 to 5:")

for i in range(1, 6):
    print(i)


print("\nFruits list:")

fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
    print(f"I like {fruit}")


print("\nMultiplication table of 5:")

for i in range(1, 11):
    print(f"5 × {i} = {5 * i}")


# While loop example

print("\nCountdown:")

count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast off!")


# Break and continue

print("\nNumbers 1-10 (skip 5):")

for i in range(1, 11):
    if i == 5:
        continue  # Skip 5
    if i == 8:
        break  # Stop at 8
    print(i)
