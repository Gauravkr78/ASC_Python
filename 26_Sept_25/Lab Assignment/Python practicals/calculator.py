def calculator():
    """
    A simple calculator that takes two numbers and an operator.
    It supports +, -, *, /, %, ** and checks for errors.
    """
    while True:  # loop to allow multiple calculations
        try:
            # Taking user inputs
            num1 = float(input("\nEnter first number: "))  # first number
            operator = input("Enter operator (+, -, *, /, %, **): ")  # operator
            num2 = float(input("Enter second number: "))  # second number

            # Performing operations based on operator
            if operator == "+":
                result = num1 + num2
            elif operator == "-":
                result = num1 - num2
            elif operator == "*":
                result = num1 * num2
            elif operator == "/":
                if num2 == 0:  # check for division by zero
                    print("Error: Division by zero!")
                    continue
                result = num1 / num2
            elif operator == "%":
                if num2 == 0:
                    print("Error: Modulus by zero!")
                    continue
                result = num1 % num2
            elif operator == "**":
                result = num1 ** num2  # power operation
            else:
                print("Invalid operator! Please use +, -, *, /, %, **")
                continue

            # Displaying the result
            print(f"Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            # If input is not a number
            print("Please enter valid numbers!")

        # Ask user if they want to continue
        choice = input("Do you want to perform another calculation? (yes/no): ").strip().lower()
        if choice != "yes":
            print("Exiting Calculator. Goodbye!")
            break


# Call the function
calculator()
