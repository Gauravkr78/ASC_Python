def simple_sets():

    # Creating a set of numbers

    numbers = {1, 2, 3, 3, 4, 4, 5}

    print("Numbers set (duplicates removed):", numbers)


    # Adding items

    numbers.add(6)

    print("After adding 6:", numbers)


    # Removing items

    numbers.remove(3)

    print("After removing 3:", numbers)


    # Set operations

    set_a = {1, 2, 3}

    set_b = {3, 4, 5}


    print("Set A:", set_a)

    print("Set B:", set_b)

    print("Union (A | B):", set_a | set_b) # All items from both

    print("Intersection (A & B):", set_a & set_b) # Common items

    # Difference (elements in set_a but not in  set_b)

    print("Difference:",   set_a-set_b )  # or A.difference(B)


simple_sets()