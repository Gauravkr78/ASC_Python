# Simple List Examples

def simple_lists():
    # Creating a list of fruits
    fruits = ["apple", "banana", "cherry"]
    print("My fruits:", fruits)

    # Adding an item to the end
    fruits.append("orange")
    print("After adding orange:", fruits)

    # Adding an item in between
    fruits.insert(1, "mango")  # Insert "mango" at index 1
    fruits.insert(3, "pineapple")  # Insert "pineapple" at index 3
    print("After inserting mango and pineapple:", fruits)

    # Removing an item
    fruits.remove("banana")
    print("After removing banana:", fruits)

    # Changing an item
    fruits[0] = "grape"
    print("After changing first item:", fruits)

    # Getting the length
    print("Number of fruits:", len(fruits))


# Run the program
simple_lists()
