# If-elif-else example
temperature = 25
if temperature > 30:
    print("It's hot outside!")
elif temperature > 20:
    print("The weather is pleasant.")
elif temperature > 10:
    print("It's a bit chilly.")
else:
    print("It's cold outside!")
# Multiple conditions
age = 18
has_license = True
if age >= 18 and has_license:
    print("You can drive!")
else:
    print("You cannot drive.")
# Grade calculator
score = 85
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score: {score}, Grade: {grade}")
