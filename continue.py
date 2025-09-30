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
