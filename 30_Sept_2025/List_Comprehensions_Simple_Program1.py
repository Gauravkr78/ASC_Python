def simple_comprehensions():

    numbers = [1, 2, 3, 4, 5]


    # Traditional way to create squared list

    squares_old = []

    for num in numbers:

        squares_old.append(num * num)


    # Using list comprehension (much shorter!)

    squares_new = [num * num for num in numbers]


    print("Original numbers:", numbers)

    print("Squares (old way):", squares_old)

    print("Squares (comprehension):", squares_new)


    # Comprehension with condition

    even_numbers = [num for num in numbers if num % 2 == 0]

    print("Even numbers only:", even_numbers)


    # Simple transformation

    names = ["alice", "bob", "charlie"]

    capitalized_names = [name.title() for name in names]

    print("Capitalized names:", capitalized_names)


simple_comprehensions()