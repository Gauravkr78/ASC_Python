# 1. Create a set of 5 numbers and print it
numbers_set = {1, 2, 3, 4, 5}
print("Set of numbers:", numbers_set)

print("\n" + "-"*30)

# 2. Write a program to add and remove elements from a set
numbers_set.add(6)
print("After adding 6:", numbers_set)
numbers_set.remove(3)
print("After removing 3:", numbers_set)

print("\n" + "-"*30)

# 3. Create two sets and find their union
set_a = {1, 2, 3}
set_b = {3, 4, 5}
union_set = set_a.union(set_b)
print("Union of set_a and set_b:", union_set)

print("\n" + "-"*30)

# 4. Write a function that finds the intersection of two sets
def intersection_sets(s1, s2):
    return s1.intersection(s2)

intersection = intersection_sets(set_a, set_b)
print("Intersection of set_a and set_b:", intersection)

print("\n" + "-"*30)

# 5. Create a program that finds the difference between two sets
difference = set_a.difference(set_b)
print("Difference (set_a - set_b):", difference)

print("\n" + "-"*30)

# 6. Write a function that checks if a set is a subset of another
def is_subset(small, big):
    return small.issubset(big)

subset_check = is_subset({1, 2}, set_a)
print("{1, 2} is subset of set_a:", subset_check)

print("\n" + "-"*30)

# 7. Create a set from a list with duplicates and observe duplicates removed
list_with_duplicates = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(list_with_duplicates)
print("Set created from list (duplicates removed):", set_from_list)

print("\n" + "-"*30)

# 8. Write a program that finds the length of a set
length = len(set_from_list)
print("Length of set_from_list:", length)

print("\n" + "-"*30)

# 9. Create a set and check if an element exists in it
check_set = {10, 20, 30}
element = 20
exists = element in check_set
print(f"Does {element} exist in check_set? {exists}")

print("\n" + "-"*30)

# 10. Write a function that clears all elements from a set
def clear_set(s):
    s.clear()

print("Before clearing check_set:", check_set)
clear_set(check_set)
print("After clearing check_set:", check_set)
