# ----------------------------
# Example 1: Using break
# ----------------------------
numbers = [1, 3, 5, 8, 10, 13]

print("Searching for the first even number using break:")
for num in numbers:
    if num % 2 == 0:  # Check if number is even
        print(f"Found even number: {num}")
        break  # Exit the loop immediately
    print(f"Checking {num}...")

# ----------------------------
# Example 2: Searching for a value in a list
# ----------------------------
names = ["Alice", "Bob", "Charlie", "David"]
search_name = "Charlie"

print("\nSearching for a name using break:")
for name in names:
    if name == search_name:
        print(f"Found {search_name}!")
        break
else:
    # Executed only if the loop completes without break
    print(f"{search_name} not found")

# ----------------------------
# Example 3: Using continue to skip iterations
# ----------------------------
print("\nSkipping even numbers using continue:")
for i in range(10):
    if i % 2 == 0:  # Skip even numbers
        continue
    print(f"Odd number: {i}")

# ----------------------------
# Example 4: Process only positive numbers
# ----------------------------
data = [5, -2, 8, -1, 10, 0, 3]

print("\nProcessing only positive numbers:")
for num in data:
    if num <= 0:  # Skip non-positive numbers
        continue
    print(f"Processing positive number: {num}")
