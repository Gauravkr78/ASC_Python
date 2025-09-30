# Fibonacci sequence generator with user input

# Take number of terms from the user
n = int(input("Enter the number of terms for Fibonacci sequence: "))

# First two Fibonacci numbers
a, b = 0, 1

# Check if the number of terms is valid
if n <= 0:
    print("Please enter a positive integer")
elif n == 1:
    print("Fibonacci sequence up to", n, "term:")
    print(a)
else:
    print("Fibonacci sequence up to", n, "terms:")
    print(a, b, end=' ')
    for i in range(2, n):
        c = a + b
        print(c, end=' ')
        a, b = b, c
