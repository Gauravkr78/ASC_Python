def simple_user_input():

    # Basic input

    name = input("What is your name? ")

    print(f"Hello, {name}!")


    # Input with conversion to number

    age = input("How old are you? ")

    age = int(age) # Convert string to integer

    print(f"Next year you will be {age + 1} years old")


    # Simple calculator with input

    print("\nSimple Calculator:")

    num1 = float(input("Enter first number: "))

    num2 = float(input("Enter second number: "))


    print(f"{num1} + {num2} = {num1 + num2}")

    print(f"{num1} - {num2} = {num1 - num2}")

    print(f"{num1} * {num2} = {num1 * num2}")


    if num2 != 0:

        print(f"{num1} / {num2} = {num1 / num2}")

    else:

        print("Cannot divide by zero!")


    # Run user input demo

simple_user_input()