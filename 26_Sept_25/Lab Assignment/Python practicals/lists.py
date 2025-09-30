# ---------------------------------------
# Lists: Indexing, Slicing, Concatenation
# ---------------------------------------
squares = [1, 4, 9, 16, 25]
print("Squares List:", squares)

# Indexing
print("First element (squares[0]):", squares[0])
print("Last element (squares[-1]):", squares[-1])

# Slicing
print("Last three elements (squares[-3:]):", squares[-3:])

# Concatenation
new_squares = squares + [36, 49, 64, 81, 100]
print("After concatenation:", new_squares)

# ---------------------------------------
# Mutability of Lists
# ---------------------------------------
cubes = [1, 8, 27, 65, 125]  # wrong cube of 4
print("\nOriginal cubes:", cubes)
print("Correct cube of 4 is:", 4 ** 3)

cubes[3] = 64  # fix the wrong value
print("Corrected cubes:", cubes)

# Adding new items using append()
cubes.append(216)     # cube of 6
cubes.append(7 ** 3)  # cube of 7
print("Cubes after appending 6³ and 7³:", cubes)

# ---------------------------------------
# Assignment in Lists
# ---------------------------------------
rgb = ["Red", "Green", "Blue"]
rgba = rgb  # no copy, just reference
print("\nIDs same?", id(rgb) == id(rgba))  # True

rgba.append("Alph")  # change through rgba
print("RGB after append through RGBA:", rgb)

# Create a shallow copy using slicing
correct_rgba = rgba[:]
correct_rgba[-1] = "Alpha"  # only changes the copy
print("Correct RGBA copy:", correct_rgba)
print("Original RGBA still:", rgba)

# ---------------------------------------
# Assignment to Slices
# ---------------------------------------
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("\nOriginal Letters:", letters)

# Replace some values
letters[2:5] = ['C', 'D', 'E']
print("After replacing slice [2:5]:", letters)

# Remove some values
letters[2:5] = []
print("After removing slice [2:5]:", letters)

# Clear entire list
letters[:] = []
print("After clearing all letters:", letters)

# ---------------------------------------
# len() function
# ---------------------------------------
letters = ['a', 'b', 'c', 'd']
print("\nLength of letters list:", len(letters))

# ---------------------------------------
# Nested Lists
# ---------------------------------------
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]  # nested list
print("\nNested List x:", x)
print("First sublist (x[0]):", x[0])
print("Second element of first sublist (x[0][1]):", x[0][1])
