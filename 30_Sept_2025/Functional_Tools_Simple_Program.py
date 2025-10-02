def simple_functional_tools():

    numbers = [1, 2, 3, 4, 5]


    # Using map to apply a function

    def double(x):

        return x * 2


    doubled = list(map(double, numbers))

    print("Original:", numbers)

    print("Doubled:", doubled)


    # Using filter to select items

    def is_even(x):

        return x % 2 == 0


    evens = list(filter(is_even, numbers))

    print("Even numbers:", evens)


    # Using lambda (anonymous functions)

    # Lambda syntax: lambda arguments: expression

    squared = list(map(lambda x: x * x, numbers))

    odds = list(filter(lambda x: x % 2 != 0, numbers))


    print("Squared (lambda):", squared)

    print("Odd numbers (lambda):", odds)


    # Combining map and filter

    doubled_evens = list(map(double, filter(is_even, numbers)))

    print("Doubled even numbers:", doubled_evens)


simple_functional_tools()