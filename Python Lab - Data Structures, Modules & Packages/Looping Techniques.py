# 1. Write a program that prints numbers 1 to 10 using a for loop
print("1. Numbers 1 to 10:")
for i in range(1, 11):
    print(i)

print("\n" + "-"*30)

# 2. Create a while loop that counts down from 5 to 1
print("2. Countdown from 5 to 1:")
i = 5
while i > 0:
    print(i)
    i -= 1

print("\n" + "-"*30)

# 3. Write a program that prints each character in a string
my_string = "Hello"
print("3. Characters in 'Hello':")
for char in my_string:
    print(char)

print("\n" + "-"*30)

# 4. Create a loop that calculates the factorial of a number
num = 5
factorial = 1
print(f"4. Factorial of {num}:")
for i in range(1, num + 1):
    factorial *= i
print(factorial)

print("\n" + "-"*30)

# 5. Write a program that finds the sum of all numbers 1-100
sum_1_to_100 = sum(range(1, 101))
print("5. Sum of numbers from 1 to 100:", sum_1_to_100)

print("\n" + "-"*30)

# 6. Create a loop that prints only even numbers between 1-20
print("6. Even numbers between 1 and 20:")
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

print("\n" + "-"*30)

# 7. Write a program that iterates through a list backwards
my_list = [10, 20, 30, 40, 50]
print("7. Iterating through list backwards:")
for item in reversed(my_list):
    print(item)

print("\n" + "-"*30)

# 8. Create a nested loop that prints a multiplication table
print("8. Multiplication table (1-5):")
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} * {j} = {i * j}")
    print("-" * 10)

print("\n" + "-"*30)

# 9. Write a program that uses break to stop a loop early
print("9. Breaking the loop early (stop at 3):")
for i in range(1, 6):
    if i == 4:
        break
    print(i)

print("\n" + "-"*30)

# 10. Create a loop that uses continue to skip odd numbers
print("10. Skipping odd numbers:")
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
