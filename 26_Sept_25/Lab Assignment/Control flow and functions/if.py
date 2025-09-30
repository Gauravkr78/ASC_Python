# ----------------------------
# Conditional Statements with User Input
# ----------------------------

# Get user age and check life stage
age = int(input("Enter your age: "))

if age < 13:
    print("You are a child")
elif 13 <= age < 18:
    print("You are a teenager")
elif 18 <= age < 60:
    print("You are an adult")
else:
    print("You are a senior citizen")

# Get exam score and assign grade
score = float(input("\nEnter your exam score (0-100): "))

if score > 100 or score < 0:
    print("Invalid score! Must be between 0 and 100.")
else:
    if score >= 90:
        grade = "A"
        remark = "Excellent"
    elif score >= 80:
        grade = "B"
        remark = "Very Good"
    elif score >= 70:
        grade = "C"
        remark = "Good"
    elif score >= 50:
        grade = "D"
        remark = "Pass"
    else:
        grade = "F"
        remark = "Fail"

    print(f"Your grade is: {grade} ({remark})")

    # Bonus: Check if score is distinction or just pass
    if score >= 75:
        print("You got distinction!")
    elif score >= 50:
        print("You passed the exam.")
    else:
        print("You failed. Better luck next time!")

# Get temperature and humidity to determine weather comfort
temperature = float(input("\nEnter current temperature (°C): "))
humidity = float(input("Enter current humidity (%): "))

# Multiple conditions using logical operators
if temperature > 40 and humidity > 80:
    print("Extremely hot and humid! Stay hydrated!")
elif temperature > 35 or humidity > 70:
    print("It's hot or humid. Take care!")
elif 20 <= temperature <= 30 and 30 <= humidity <= 60:
    print("Comfortable weather")
elif temperature < 0:
    print("Freezing cold! Wear warm clothes")
else:
    print("🌤️ Weather is moderate but check local conditions")



