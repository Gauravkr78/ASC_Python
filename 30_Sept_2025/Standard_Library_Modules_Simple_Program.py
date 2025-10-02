def standard_library_demo():
    # Math module
    import math
    print("Math module examples:")
    print(f"Square root of 16: {math.sqrt(16)}")
    print(f"5 raised to power 3: {math.pow(5, 3)}")
    print(f"Pi constant: {math.pi}")

    # Random module
    import random
    print("\nRandom module examples:")
    print(f"Random number between 1-10: {random.randint(1, 10)}")
    print(f"Random choice from list: {random.choice(['apple', 'banana', 'cherry'])}")

    # Datetime module
    import datetime
    print("\nDatetime module examples:")
    now = datetime.datetime.now()
    print(f"Current date and time: {now}")
    print(f"Today's date: {now.date()}")
    print(f"Current year: {now.year}")

# Run the demo
standard_library_demo()
