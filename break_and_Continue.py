# Break - Exit the Loop

numbers = [1, 3, 5, 8, 10, 13]
for num in numbers:
    if num % 2 == 0:
        print(f"Found even number: {num}")
        break
    print(f"Checking {num}")

# Search for a value
names = ["Alice", "Bob", "Charlie", "David"]
search_name = "Charlie"
for name in names:
    if name == search_name:
        print(f"Found {search_name}!")
        break
else:
    print(f"{search_name} not found")


# Continue - Skip Current Iteration

# Skip even numbers
for i in range(10):
    if i % 2 == 0:
        continue  # Skip even numbers
    print(f"Odd number: {i}")

# Process only valid data
data = [5, -2, 8, -1, 10, 0, 3]
for num in data:
    if num <= 0:
        continue  # Skip non-positive numbers
    print(f"Processing positive number: {num}")
