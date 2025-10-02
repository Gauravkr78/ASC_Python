def simple_tuples():
    # Creating a tuple of days
    days = ("Monday", "Tuesday", "Wednesday")
    print("Original tuple:", days)

    # Convert tuple to list to perform operations
    days_list = list(days)

    # Add an element
    days_list.append("Thursday")
    print("After adding Thursday:", tuple(days_list))

    # Insert an element at a specific position
    days_list.insert(1, "Sunday")
    print("After inserting Sunday at index 1:", tuple(days_list))

    # Update an element
    days_list[2] = "Monday Updated"
    print("After updating element at index 2:", tuple(days_list))

    # Delete an element
    days_list.remove("Wednesday")
    print("After deleting Wednesday:", tuple(days_list))

    # Tuple unpacking (only works if you match number of elements)
    day1, day2, day3 = days
    print("Unpacked:", day1, day2, day3)

    # Convert back to tuple
    days = tuple(days_list)
    print("Final tuple:", days)


# Run the function
simple_tuples()
