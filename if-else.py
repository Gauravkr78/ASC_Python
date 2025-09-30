# Simple if statement
age = 10

if age >= 18:
    print("You are an adult")

# if-elif-else chain
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
else:
    grade = "F"

print(f"Your grade is: {grade}")

# Multiple conditions
temperature = 25
humidity = 70

if temperature > 30 and humidity > 80:
    print("Very hot and humid")
elif temperature > 30 or humidity > 80:
    print("Either hot or humid")
else:
    print("Comfortable weather")
