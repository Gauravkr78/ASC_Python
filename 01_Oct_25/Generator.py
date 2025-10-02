# Generator function
def countdown(n):
    while n > 0:
        yield n
        n -= 1

print("Generator countdown:")
for number in countdown(5):
    print(number)

# Generator expression
squares = (x * x for x in range(5))
print("Squares generator:")
for square in squares:
    print(square)

# Generator maintaining state
def simple_generator():
    yield "First"
    yield "Second"
    yield "Third"

gen = simple_generator()
print(next(gen))  # Output: First
print(next(gen))  # Output: Second
print(next(gen))  # Output: Third
