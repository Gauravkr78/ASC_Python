# 1. Create a dictionary of 3 students with their grades
students = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print("Students dictionary:", students)
print("\n" + "-"*30)

# 2. Write a program to access and print all dictionary values
print("Grades:")
for grade in students.values():
    print(grade)

print("\n" + "-"*30)

# 3. Create a dictionary and add a new key-value pair
students["David"] = 88
print("After adding David:", students)

print("\n" + "-"*30)

# 4. Write a function that returns all keys in a dictionary
def get_keys(d):
    return list(d.keys())

keys = get_keys(students)
print("Keys in students dictionary:", keys)

print("\n" + "-"*30)

# 5. Create a program that removes a key from a dictionary
removed = students.pop("Charlie", None)  # removes key if exists, else None
print(f"Removed 'Charlie': {removed}")
print("After removal:", students)

print("\n" + "-"*30)

# 6. Write a function that checks if a key exists in a dictionary
def key_exists(d, key):
    return key in d

check_key = "Alice"
print(f"Does '{check_key}' exist? {key_exists(students, check_key)}")

print("\n" + "-"*30)

# 7. Create a dictionary and update multiple values at once
update_dict = {"Alice": 90, "Bob": 95}
students.update(update_dict)
print("After update:", students)

print("\n" + "-"*30)

# 8. Write a program that prints all key-value pairs
print("All students and grades:")
for student, grade in students.items():
    print(f"{student}: {grade}")

print("\n" + "-"*30)

# 9. Create a dictionary from two lists (keys and values)
keys_list = ["Eve", "Frank", "Grace"]
values_list = [82, 77, 93]
new_dict = dict(zip(keys_list, values_list))
print("Dictionary from lists:", new_dict)

print("\n" + "-"*30)

# 10. Write a function that returns the length of a dictionary
def dict_length(d):
    return len(d)

length = dict_length(students)
print("Length of students dictionary:", length)
