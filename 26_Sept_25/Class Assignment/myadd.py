import sys

def add(a, b):
    result = a + b
    print(f"{a} + {b} = {result}")
    return result

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python -m add <num1> <num2>")
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        add(a, b)