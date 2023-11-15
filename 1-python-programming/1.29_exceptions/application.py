#!/bin/python
# Python Exceptions - Solution

# Create a custom exception class named `ValueTooSmallError` that inherits from the built-in ValueError class
class ValueTooSmallError(ValueError):
    pass

def check_value(value, threshold):
    """
    This function takes a numeric 'value' and 'threshold' as arguments. It raises a 'ValueTooSmallError'
    exception if the 'value' is smaller than the 'threshold'.

    Args:
        value (float or int): The value to be checked.
        threshold (float or int): The minimum acceptable threshold.

    Raises:
        ValueTooSmallError: If 'value' is smaller than 'threshold'.
    """
    # TODO: Implement the function
    pass

def calculate_average(numbers):
    """
    This function calculates the average of a list of numbers. It handles the following exceptions:
    - TypeError: If an invalid input is encountered (non-numeric values).
    - ZeroDivisionError: If the list is empty.

    Args:
        numbers (list): List of numeric values.

    Returns:
        float: Average of the numbers.
    """
    # TODO: Implement the function
    pass

def count_lines_in_file(filename):
    """
    This function reads the contents of the specified file and returns the number of lines.
    It handles the 'FileNotFoundError' exception if the file does not exist.

    Args:
        filename (str): Name of the file.

    Returns:
        int: Number of lines in the file.
    """
    # TODO: Implement the function
    pass
