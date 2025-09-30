def calculate_grade(percentage):
    if percentage >= 90:
        return 'A'
    elif percentage >= 80:
        return 'B'
    elif percentage >= 70:
        return 'C'
    elif percentage >= 60:
        return 'D'
    elif percentage >= 50:
        return 'E'
    else:
        return 'F'


def is_pass(marks):
    return all(mark >= 35 for mark in marks)


students = []
student_count = 0

while True:
    print(f"\nEnter details for Student {student_count + 1}")
    name = input("Enter student's name (or press Enter to stop): ").strip()
    if name == "":
        break
    city = input("Enter student's city: ").strip()

    marks = []
    for i in range(5):
        while True:
            try:
                mark = int(input(f"Enter marks for subject {i + 1}: "))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Marks must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")

    total = sum(marks)
    percentage = total / 5
    grade = calculate_grade(percentage)
    passed = is_pass(marks)

    student_data = {
        "name": name,
        "city": city,
        "marks": marks,
        "total": total,
        "percentage": percentage,
        "grade": grade,
        "status": "Pass" if passed else "Fail"
    }

    students.append(student_data)
    student_count += 1

# Output results
print("\n--- Student Results ---")
for student in students:
    print(f"\nName: {student['name']}")
    print(f"City: {student['city']}")
    print(f"Marks: {student['marks']}")
    print(f"Total: {student['total']}")
    print(f"Percentage: {student['percentage']:.2f}%")
    print(f"Grade: {student['grade']}")
    print(f"Result: {student['status']}")

# Calculate and show average if students exist
if students:
    average_percentage = sum(s['percentage'] for s in students) / len(students)
    print(f"\nAverage PGauravercentage of Class: {average_percentage:.2f}%")
else:
    print("\nNo students entered. Nothing to calculate.")
