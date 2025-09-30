# Creating and modifying lists

numbers = [1, 2, 3, 4, 5]

print(f"Original list: {numbers}")


# Adding elements

numbers.append(6) # Add to end

numbers.insert(0, 0) # Insert at beginning

print(f"After adding elements: {numbers}")


# Removing elements

numbers.remove(3) # Remove specific value

popped = numbers.pop() # Remove and return last element

print(f"After removals: {numbers}")

print(f"Popped element: {popped}")


# List operations

fruits = ["apple", "banana"]

vegetables = ["carrot", "potato"]

grocery = fruits + vegetables # Concatenation

print(f"Grocery list: {grocery}")


# List slicing

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(f"First 3: {numbers[:3]}")

print(f"Last 3: {numbers[-3:]}")

print(f"Middle: {numbers[3:7]}")

print(f"Every second element: {numbers[::2]}")


# List comprehension (advanced but useful)

squares = [x**2 for x in range(1, 6)]

even_numbers = [x for x in range(10) if x % 2 == 0]

print(f"Squares: {squares}")

print(f"Even numbers: {even_numbers}")