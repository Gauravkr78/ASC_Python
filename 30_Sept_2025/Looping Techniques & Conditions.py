def simple_conditions():

    # Basic if-else example

    age = 18


    if age >= 18:

        print("You are an adult")

    else:

        print("You are a minor")


    # Multiple conditions with elif

    score = 85


    if score >= 90:

        grade = "A"

    elif score >= 80:

        grade = "B"

    elif score >= 70:

        grade = "C"

    else:

        grade = "F"


    print(f"Score: {score}, Grade: {grade}")


    # Simple condition check

    temperature = 25

    if temperature > 30:

        print("It's hot outside")

    elif 20 <= temperature <= 30:

        print("Weather is pleasant")

    else:

        print("It's cold outside")


simple_conditions()