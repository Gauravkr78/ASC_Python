#Method -01
def simple_dictionaries():


    # Creating a student dictionary

    student = {

        "name": "Alice",

        "age": 20,

        "grade": "A"

    }

    print("Student information:", student)

    # Accessing values by key

    print("Student name:", student["name"])

    print("Student age:", student.get("age"))

    # Adding new key-value pair

    student["city"] = "New York"

    print("After adding city:", student)

    # Changing a value

    student["grade"] = "A+"

    print("After grade change:", student)

    # Looping through dictionary

    print("\nAll student details:")

    for key, value in student.items():

     print(f"{key}: {value}")

simple_dictionaries()



# # Method -02
# def simple_dictionaries():
#     # Creating a student dictionary
#     student = {
#         "name": "Alice",
#         "age": 20,
#         "grade": "A"
#     }
#
#     print("Current student dictionary:", student)
#     print("\nSelect an operation:")
#     print("1. Access value by key")
#     print("2. Add new key-value pair")
#     print("3. Change a value")
#     print("4. Display all key-value pairs")
#
#     choice = input("Enter your choice (1-4): ")
#
#     if choice == "1":
#         key = input("Enter the key to access: ")
#         value = student.get(key, "Key not found")
#         print(f"{key}: {value}")
#
#     elif choice == "2":
#         key = input("Enter new key: ")
#         value = input("Enter value for the key: ")
#         student[key] = value
#         print(f"Added {key}: {value}")
#
#     elif choice == "3":
#         key = input("Enter the key to update: ")
#         if key in student:
#             value = input("Enter new value: ")
#             student[key] = value
#             print(f"Updated {key} to {value}")
#         else:
#             print("Key not found!")
#
#     elif choice == "4":
#         print("\nAll student details:")
#         for key, value in student.items():
#             print(f"{key}: {value}")
#
#     else:
#         print("Invalid choice. Exiting...")
#
#     # Print the full dictionary at the end
#     print("\nFinal student dictionary:", student)
#
# # Run the function
# simple_dictionaries()
