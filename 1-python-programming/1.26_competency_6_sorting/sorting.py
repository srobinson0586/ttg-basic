#!/bin/python
# Python Competency 4 Sorting

def bubble_sort(lst):
    """
    Implements the Bubble Sort algorithm to sort a list of data in ascending order.

    The algorithm should compare adjacent elements of the input list and swap their positions if they are not
    in order. Changes to the list should be done in place.

    Parameters:
        - lst: list; A python list composed entirely of strings or entirely of numbers to be sorted.

    Returns:
        This function returns a sorted list.

    Example:
    >>> lst = [6, 1, 5, 2, 3, 9, 7, 8, 4, 0]
    >>> bubble_sort(lst)
    >>> print(lst)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
    """
    # TODO: Implement
    pass

def insertion_sort(lst):
    """
    Implements the Insertion Sort algorithm to sort a list of data in ascending order.

    The algorithm should maintain sorted and unsorted sublists. Unsorted elements should be inserted into
    the correct position of the sorted sublist until the entire input list is sorted. Changes to the list should be done in place.

    Parameters:
        - lst: list; A python list composed entirely of strings or entirely of numbers to be sorted.

    Returns:
        This function returns a sorted list.

    Example:
    >>> lst = [6, 1, 5, 2, 3, 9, 7, 8, 4, 0]
    >>> insertion_sort(lst)
    >>> print(lst)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
    """
    # TODO: Implement
    pass

def selection_sort(lst):
    """
    Implements the Selection Sort algorithm to sort a list of data in ascending order.

    The algorithm should maintain sorted and unsorted sublists. The minimum value of the unsorted list should 
    be found and placed in the correct position of the sorted sublist until the entire input list is sorted. 
    Changes to the list should be done in place.

    Parameters:
        - lst: list; A python list composed entirely of strings or entirely of numbers to be sorted.

    Returns:
        This function returns a sorted list.

    Example:
    >>> lst = [6, 1, 5, 2, 3, 9, 7, 8, 4, 0]
    >>> insertion_sort(lst)
    >>> print(lst)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
    """
    # TODO: Implement
    pass

def merge_sort(lst):
    """
    Implements the Merge Sort algorithm to sort a list of data in ascending order.

    The algorithm should recursively split the input list in half until its sublists each contain a single 
    element. The algorithm should then merge all sublists back together in sorted order until the result is
    the sorted version of the input list. Changes to the list should be done in place.

    Hint: Many implementations of Merge Sort utilize a helper function called `merge` to implement the logic 
    for merging sublists back together. You may want to define your own `merge` function as well.

    Parameters:
        - lst: list; A python list composed entirely of strings or entirely of numbers to be sorted.

    Returns:
        This function returns a sorted list.

    Example:
    >>> lst = [6, 1, 5, 2, 3, 9, 7, 8, 4, 0]
    >>> insertion_sort(lst)
    >>> print(lst)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]    
    """
    # TODO: Implement
    pass


def test():
    """
    ***OPTIONAL***
    Tests your sorting algorithms.

    This function is where you can write some tests for your sorting algorithms. You will want to test 
    each algorithm using different lists as input. You can initialize some generic lists in this function 
    that represent random, already sorted, or nearly sorted data to check if your algorithms can handle each 
    case of input. You have complete control over what you put in this function.
    """
    pass

if __name__ == "__main__":
    """
    The tests in the `test` function will run if you execute the script on the command line as follows:

    $> python sorting.py
    """
    test()
