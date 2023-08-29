#!/bin/python
# Python Operators - Solution

def multiply_and_divide(a, b, c):
    """
    Calculates the result of multiplying a by b, then dividing the result by c

    Args:
        a (float or int): The first operand.
        b (float or int): The second operand.
        c (float or int): The divisor.

    Returns:
        float: The result of multiplying a by b, then dividing the result by c
    """
    return float(a * b) / c

def concatenate_strings(str1, str2):
    """
    Concatenates two strings based on certain conditions.

    If the lengths of the two strings are equal, it returns "SameLength".
    If str1 is an empty string, it returns str2.
    If str2 is an empty string, it returns str1.
    Otherwise, it concatenates str1 and str2 and returns the result.

    Args:
        str1 (str): The first string.
        str2 (str): The second string.

    Returns:
        str: The concatenated string or "SameLength" based on conditions.
    """
    if len(str1) == len(str2):
        return "SameLength"
    else:
        return str1 + str2
