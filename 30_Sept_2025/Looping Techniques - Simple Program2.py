def simple_loops():
    # For loop with list
    fruits = ["apple", "banana", "cherry"]
    print("For loop with list:")
    for fruit in fruits:
        print("I like", fruit)

    # For loop with range
    print("\nCounting with range:")
    for i in range(3):  # 0, 1, 2
        print("Number:", i)

    # While loop
    print("\nWhile loop example:")
    count = 1
    while count <= 3:
        print("Count is:", count)
        count += 1  # Important: don't forget to update counter!

    # Loop control with break and continue
    print("\nLoop control:")
    for i in range(5):
        if i == 2:
            continue  # Skip number 2
        if i == 4:
            break  # Stop at number 4
        print("Processing:", i)

# Call the function
simple_loops()
