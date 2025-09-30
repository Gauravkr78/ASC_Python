# Break when condition is met
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
