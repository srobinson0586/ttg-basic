#!/bin/python
# Python Algorithms - Pytest Suite
import application
        
def test_swap():
    lst1 = [17, 51, 94, 55, 67, 5, 1, 48, 71, 83, 24, 30, 99, 25, 7]
    lst2 = [10, 30, 20, 40, 50, 90, 70, 80, 60, 100]
    rv = application.swap_largest(lst1)
    assert rv == 12, "swap_largest() did not return the correct index where the maximum element was found"
    assert lst1[0] == 99, "swap_largest() did not correctly swap the maximum element to the first index of the list"
    assert lst1[rv] == 17, "swap_largest() did not correctly swap the first element with the maximum element"
    rv = application.swap_largest(lst2)
    assert rv == 9, "swap_largest() did not return the correct index where the maximum element was found"
    assert lst2[0] == 100, "swap_largest() did not correctly swap the maximum element to the first index of the list"
    assert lst2[rv] == 10, "swap_largest() did not correctly swap the first element with the maximum element"

def test_recursion():
    rv = application.recursive_multiply(2, 4)
    assert rv == 8, "recursive_multiply() did not return the correct value for values a=2, b=4"
    rv = application.recursive_multiply(3, 3)
    assert rv == 9, "recursive_multiply() did not return the correct value for values a=3, b=-3"

