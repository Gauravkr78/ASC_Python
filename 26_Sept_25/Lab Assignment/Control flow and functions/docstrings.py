# ==================================
# Basic Docstring Example
# ==================================

def calculate_area(length, width):
    """
    Calculate the area of a rectangle.

    Args:
        length (float): The length of the rectangle
        width (float): The width of the rectangle

    Returns:
        float: The area of the rectangle
    """
    return length * width


# Access the docstring directly
print("Docstring of calculate_area:\n")
print(calculate_area.__doc__)  # Prints the docstring text

# Access help documentation (interactive)
print("\nHelp on calculate_area:\n")
help(calculate_area)


# ==================================
# Comprehensive Docstring Example
# ==================================

def process_data(data, threshold=0, method='average'):
    """
    Process numerical data with various methods.

    This function can filter and process numerical data using
    different statistical methods.

    Args:
        data (list): List of numerical values to process
        threshold (float, optional): Minimum value to include. Defaults to 0.
        method (str, optional): Processing method. Options: 'average', 'sum', 'max'.
                                Defaults to 'average'.

    Returns:
        float: Processed result based on the chosen method

    Raises:
        ValueError: If data is empty or method is invalid
    """

    if not data:
        raise ValueError("Data cannot be empty")

    # Filter data above threshold
    filtered_data = [x for x in data if x > threshold]

    if not filtered_data:
        return 0

    # Choose processing method
    if method == 'average':
        return sum(filtered_data) / len(filtered_data)
    elif method == 'sum':
        return sum(filtered_data)
    elif method == 'max':
        return max(filtered_data)
    else:
        raise ValueError("Invalid method")


# Example usage:
data = [5, 10, 15, 20]

print("\nProcessing Data Examples:")
print("Average above threshold 10:", process_data(data, threshold=10, method='average'))
print("Sum above threshold 10:", process_data(data, threshold=10, method='sum'))
print("Max above threshold 10:", process_data(data, threshold=10, method='max'))
