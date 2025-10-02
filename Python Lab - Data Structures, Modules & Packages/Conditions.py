# 1. Check if a number is positive, negative, or zero
def check_number(num):
    if num > 0:
        return "Positive"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"

print("1.", check_number(10), check_number(-5), check_number(0))

print("\n" + "-"*30)

# 2. Function to determine even or odd
def even_or_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

print("2.", even_or_odd(7), even_or_odd(8))

print("\n" + "-"*30)

# 3. Largest of three numbers
def largest_of_three(a, b, c):
    return max(a, b, c)

print("3.", largest_of_three(10, 25, 15))

print("\n" + "-"*30)

# 4. Check if a year is a leap year
def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

print("4.", is_leap_year(2020), is_leap_year(1900), is_leap_year(2000))

print("\n" + "-"*30)

# 5. Determine student grade based on score
def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("5.", grade(85), grade(72), grade(59))

print("\n" + "-"*30)

# 6. Check if string is palindrome
def is_palindrome(s):
    s_clean = s.lower().replace(" ", "")
    return s_clean == s_clean[::-1]

print("6.", is_palindrome("Racecar"), is_palindrome("Hello"))

print("\n" + "-"*30)

# 7. Basic email format validation
def validate_email(email):
    return "@" in email and "." in email.split("@")[-1]

print("7.", validate_email("test@example.com"), validate_email("invalidemail"))

print("\n" + "-"*30)

# 8. Determine triangle type by sides
def triangle_type(a, b, c):
    if a == b == c:
        return "Equilateral"
    elif a == b or b == c or a == c:
        return "Isosceles"
    else:
        return "Scalene"

print("8.", triangle_type(3, 3, 3), triangle_type(3, 3, 4), triangle_type(3, 4, 5))

print("\n" + "-"*30)

# 9. Calculate BMI and categorize
def bmi_category(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

print("9.", bmi_category(70, 1.75), bmi_category(90, 1.75))

print("\n" + "-"*30)

# 10. Check voting eligibility by age
def can_vote(age):
    return age >= 18

print("10.", can_vote(20), can_vote(16))
