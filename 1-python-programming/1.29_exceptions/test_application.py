#!/bin/python
# Python Exceptions - Pytest Suite
import application

def test_exceptions():
    # Test the ValueTooSmallError Exception
    assert issubclass(application.ValueTooSmallError, ValueError), 'ValueTooSmallError needs to inherit from the ValueError class'
    assert not isinstance(application.ValueTooSmallError, ValueError), 'ValueTooSmallError can\'t be of type ValueError, it needs to inherit'
    
    # Test the check_value function
    assert not application.check_value(20, 10)  # No exception should be raised
    try:
        application.check_value(10, 20)
    except Exception as e:
        assert isinstance(e, application.ValueTooSmallError)

    # Test the calculate_average function
    assert application.calculate_average([10, 20, 30, 40]) == 25.0
    assert application.calculate_average([1, 2, 3, 4, 5]) == 3.0
    try:
        application.calculate_average([1, 2, 'a', 4, 5])  # Non-numeric value should raise TypeError
    except Exception as e:
        assert isinstance(e, TypeError), "calculate_average(): Incorrect; Expected TypeError Exception."
    try:
        application.calculate_average([])  # Empty list should raise ZeroDivisionError
    except Exception as e:
        assert isinstance(e, ZeroDivisionError), "calculate_average(): Incorrect; Expected ZeroDivisionError Exception."

    # Test the count_lines_in_file function
    # NOTE: IF YOU ADD ANY LINES TO THE REAMDE, YOU NEED TO UPDATE THIS CHECK
    assert application.count_lines_in_file('./README.md') == 8
    try:
        application.count_lines_in_file('nonexistent.txt')  # Nonexistent file should raise FileNotFoundError
    except Exception as e:
        assert isinstance(e, FileNotFoundError), "calculate_average(): Incorrect; Expected FileNotFoundError Exception."
