# 2. Create a flexible greeting function
def create_greeting(name, time_of_day="day", formal=False):
    """
    Create a greeting message.

    Args:
        name (str): Name of the person
        time_of_day (str): Time of the day (default: 'day')
        formal (bool): Whether to greet formally or informally

    Returns:
        str: Greeting message
    """
    if formal:
        return f"Good {time_of_day}, Mr./Ms. {name}"
    else:
        return f"Hi {name}! Have a great {time_of_day}!"


# Test different combinations:
print(create_greeting("Alice"))  # Default time_of_day & informal
print(create_greeting("Bob", "evening"))  # Custom time_of_day, informal
print(create_greeting("Charlie", formal=True))  # Formal greeting
print(create_greeting("Diana", "morning", True))  # Formal + custom time_of_day
print(create_greeting("Eve", time_of_day="afternoon", formal=False))  # Keyword args
