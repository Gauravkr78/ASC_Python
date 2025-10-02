# 1. Create a list of 5 fruits and print each fruit on a new line
fruits = ["apple", "banana", "cherry", "mango", "orange"]
print("1. Fruits List:")
for fruit in fruits:
    print(fruit)

print("\n" + "-"*50)

# 2. Write a program to find the length of a given list
my_list = [1, 2, 3, 4, 5]
print("2. Length of list:", len(my_list))

print("\n" + "-"*50)

# 3. Create a list of numbers 1-10 and print only even numbers
numbers = list(range(1, 11))
even_numbers = [num for num in numbers if num % 2 == 0]
print("3. Even numbers from 1 to 10:", even_numbers)

print("\n" + "-"*50)

# 4. Write a function that takes a list and returns the sum of all elements
def sum_list(lst):
    return sum(lst)

print("4. Sum of list elements:", sum_list([1, 2, 3, 4, 5]))

print("\n" + "-"*50)

# 5. Create a program that adds new items to a list and removes the first item
items = ["pen", "pencil", "eraser"]
items.append("sharpener")
items.append("marker")
removed_item = items.pop(0)
print("5. Updated list:", items)
print("Removed item:", removed_item)

print("\n" + "-"*50)

# 6. Write a function to find the maximum and minimum values in a number list
def find_min_max(lst):
    return min(lst), max(lst)

nums = [34, 12, 78, 4, 56]
min_val, max_val = find_min_max(nums)
print("6. Min:", min_val, "Max:", max_val)

print("\n" + "-"*50)

# 7. Create a list of names and sort them alphabetically
names = ["John", "Alice", "Bob", "Diana"]
names.sort()
print("7. Sorted names:", names)

print("\n" + "-"*50)

# 8. Write a program that reverses a list without using the reverse() method
original_list = [1, 2, 3, 4, 5]
reversed_list = original_list[::-1]
print("8. Reversed list:", reversed_list)

print("\n" + "-"*50)

# 9. Create two lists and combine them into one list
list1 = [1, 2, 3]
list2 = [4, 5, 6]
combined = list1 + list2
print("9. Combined list:", combined)

print("\n" + "-"*50)

# 10. Write a function that removes all duplicates from a list
def remove_duplicates(lst):
    return list(set(lst))

duplicates_list = [1, 2, 2, 3, 4, 4, 5]
unique_list = remove_duplicates(duplicates_list)
print("10. List after removing duplicates:", unique_list)
