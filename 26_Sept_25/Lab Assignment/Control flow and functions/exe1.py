# 1. Function to categorize a single number
def categorize_number(num):
    """
    Categorize a number as:
    - Positive Even
    - Positive Odd
    - Negative
    - Zero
    """
    if num > 0:
        if num % 2 == 0:
            return "Positive Even"
        else:
            return "Positive Odd"
    elif num < 0:
        return "Negative"
    else:
        return "Zero"


# 2. Function to process a list of numbers and show summary
def process_numbers(numbers):
    """
    Process a list of numbers:
    - Categorize each
    - Show summary of categories
    """
    summary = {"Positive Even": 0, "Positive Odd": 0, "Negative": 0, "Zero": 0}

    print("\n=== Number Categorization ===")
    for num in numbers:
        category = categorize_number(num)
        print(f"{num}: {category}")
        summary[category] += 1  # count category occurrence

    # Show summary
    print("\n=== Summary ===")
    for category, count in summary.items():
        print(f"{category}: {count}")


# 3. Take input from user
try:
    user_input = input("Enter numbers separated by space: ")
    numbers_list = [int(x) for x in user_input.split()]  # convert to int list
    process_numbers(numbers_list)
except ValueError:
    print("Please enter valid integers!")
