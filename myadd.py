def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 3:
        print("Usage: python myadd.py num1 num2")
        sys.exit(1)

    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
    except ValueError:
        print("Please provide two integer numbers.")
        sys.exit(1)

    add(num1, num2)
