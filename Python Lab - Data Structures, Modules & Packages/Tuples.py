# 1. Create a tuple of 5 colors and print each color
colors = ("red", "blue", "green", "yellow", "purple")
print("Colors:")
for color in colors:
    print(color)

print("\n" + "-"*30)

# 2. Write a program to find the length of a tuple
length = len(colors)
print(f"Length of colors tuple: {length}")

print("\n" + "-"*30)

# 3. Create a tuple of numbers and find their sum
numbers = (10, 20, 30, 40, 50)
total = sum(numbers)
print(f"Sum of numbers tuple: {total}")

print("\n" + "-"*30)

# 4. Write a function that converts a tuple to a list and back
def tuple_list_convert(t):
    lst = list(t)
    print(f"List: {lst}")
    t_back = tuple(lst)
    print(f"Tuple again: {t_back}")
    return t_back

tuple_list_convert(numbers)

print("\n" + "-"*30)

# 5. Create a tuple with mixed data types and print each element's type
mixed = (1, "apple", 3.14, True, None)
print("Element types in mixed tuple:")
for elem in mixed:
    print(f"{elem} -> {type(elem)}")

print("\n" + "-"*30)

# 6. Write a program that finds the index of a specific element in a tuple
search_element = "green"
if search_element in colors:
    idx = colors.index(search_element)
    print(f"Index of '{search_element}' in colors tuple: {idx}")
else:
    print(f"'{search_element}' not found in colors tuple")

print("\n" + "-"*30)

# 7. Create two tuples and concatenate them
tuple1 = (1, 2, 3)
tuple2 = ("a", "b", "c")
concatenated = tuple1 + tuple2
print(f"Concatenated tuple: {concatenated}")

print("\n" + "-"*30)

# 8. Write a function that counts how many times an element appears in a tuple
def count_element(t, elem):
    return t.count(elem)

sample_tuple = (1, 2, 2, 3, 4, 2, 5)
element_to_count = 2
count = count_element(sample_tuple, element_to_count)
print(f"Element {element_to_count} appears {count} times in {sample_tuple}")

print("\n" + "-"*30)

# 9. Create a tuple and try to modify an element (handle the error)
immutable_tuple = (10, 20, 30)
try:
    immutable_tuple[1] = 99
except TypeError as e:
    print(f"Error: {e}")

print("\n" + "-"*30)

# 10. Write a program that unpacks a tuple into separate variables
person = ("Alice", 30, "Engineer")
name, age, profession = person
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Profession: {profession}")
