import os
import time
from datetime import datetime

#++++++++++++++++++++++++++++++++++++++++++++++#
#         BEGIN INTRODUCTION FUNCTIONS         #
#++++++++++++++++++++++++++++++++++++++++++++++#

###########################################################
#                  STRING PRACTICE                        #
#         Refer to CodingBat.com 's String Basics         #
###########################################################

def greet(name):
    """ Given a string `name`, return a greeting of the form "Hello <name>!"

    E.g.,
     greet('Bob') -> 'Hello Bob!'
     greet('Alice') -> 'Hello Alice!'
     greet('X') -> 'Hello X!' """
    pass

def abba(a, b):
    """ Given two strings, `a` and `b`, return the result of concatenating
    them in the order of abba.

    E.g.,
     abba('Hi', 'Bye') -> 'HiByeByeHi' """
    pass

def split_and_insert(outer, inner):
    """ Given a string `outer` of even length and a string `inner`, return
    the result of splitting `outer` in half and inserting `inner` in the
    middle.

    E.g.,
     split_and_insert('<<>>', 'stuff') -> '<<stuff>>'
     split_and_insert('..**', 'hi') -> '..hi**' """
    pass

def dup_last_2(s, n):
    """ Given a string `s` and an integer `n`, return a new string made of
    `n` copies of the last 2 characters of `s`.

    E.g.,
     dup_last_2('word', 4) -> 'rdrdrdrd'
     dup_last_2('mocha', 3) -> 'hahaha' """
    pass

def short_long_short(s1, s2):
    """ Given 2 strings, return a new string in the form of shortlongshort.

    E.g.,
     shortlongshort('a big string', 'hi') -> 'hia big stringhi'
     shortlongshort('hi', 'a big string') -> 'hia big stringhi' """
    pass


#########################################################
#                    INTEGER PRACTICE                   #
#########################################################

def adding(a, b):
    """ Return the sum of `a` and `b`, unless `a` and `b` are equal;
    if they are, return twice their sum. """
    pass

def abs_diff(n):
    """ Given an int `n`, if `n` is less than or equal to 21, return
    the absolute value of the difference between `n` and 21; if
    `n` is greater than 21, return twice the absolute value of that
    difference. """
    pass

def tens(a, b):
    """ Given 2 integers, return True if one of them is 10, or if their
    sum is 10; otherwise return False. """
    pass

def hundreds(n):
    """ Given an integer `n`, return True if its absolute difference from 100
    is less than or equal to 10. """
    pass

def negatives(a, b, negative):
    """ Given 2 integer values `a` and `b` and the boolean `negative`:
     (a) if `negative` is True, return True if both integers are negative.
     (b) if `negative` is False, return True if exactly 1 integer is negative.
    Otherwise return False in both cases. """
    pass


#######################################################
#                     LIST PRACTICE                   #
#######################################################


def ends_are_the_same(lst):
    """ Given an list `lst` of integers, return True if the list has length
    greater than 1 and if the first and last elements are equal. Otherwise
    return False.

    E.g.,
     ends_are_the_same([1, 2, 3, 4]) -> False
     ends_are_the_same([1, 2, 1]) -> True
     ends_are_the_same([1]) -> False
     ends_are_the_same([]) -> False """
    pass

def count_sixes(lst):
    """ Given a list of integers, return the total number of times the
    value 6 occurs in it. """
    pass

def sum_list(lst):
    """ Given an list `lst` of integers, return the sum of those integers.

    You can do this however you want, but there's a shortcut available.
    Inspect the output of 'dir(__builtins__)' in the Python shell to see
    all the built-in Python variables. """
    pass

def rotate_2_spaces_left(lst):
    """ Given a list, rotate it left by 2 spaces and return the result.

    E.g.,
     rotate_2_spaces_left([1, 2, 3, 4, 5, 6]) -> [3, 4, 5, 6, 1, 2]
     rotate_2_spaces_left([1, 2, 3, 4]) -> [3, 4, 1, 2]
     rotate_2_spaces_left([5, 6]) -> [5, 6]
    You may assume the list has at least 2 elements in it. """
    pass

def append_product_and_sum(lst):
    """ Given a list of integers, do the following, in order:
    1. Remove the last 2 items from the list.
    2. Append the product of the removed values.
    3. Append the sum of the current first 2 items in the list.
    4. Return the resulting list.

    You may assume that the list has at least 3 elements at the beginning.
    E.g.,
     append_product_and_sum([1, 2, 3]) -> [1, 6, 7] """
    pass


#########################################
#           BOOLEAN PRACTICE            #
#########################################

def count_trues(a, b, c):
    """ Given three booleans, return the number of them that are True. """
    pass


def positive_product(a, b):
    """ Given 2 integers, return True if their product is positive;
    otherwise return False. """
    pass


def has_7_before_6(lst):
    """ Given a list, return True if 7 appears in it before 6. If 6 appears
    before 7 or if there is no 7, return False. """
    pass


def greater_than_both(a, b, c):
    """ Given 3 integers `a`, `b`, and `c`, using a SINGLE return statement
    (and no other lines of code) return True if `a` is greater than `b` and
    `a` is greater than `c`. Otherwise, return False. """
    pass


def close_and_far(a, b, c):
    """ Given 3 integers `a`, `b`, and `c`, using a SINGLE return
    statement, return True if both:
    (a) `a` or `b` has a difference of less than or equal to 1 from `c`
    (b) `a` or `b` has a difference of 2 or more from the other 2 integers.
    Otherwise, return False. """
    pass


##################################################
#              LOOPING AND ITERATION             #
##################################################

def copy_xkcd_to_calvin(lst):
    """ Given a list of strings, return a new list in with all the same
    strings, except that the strings that began with "xkcd" have
    that prefix replaced with the prefix "calvin".

    E.g.,
     copy_xkcd_to_calvin(['cow', 'xkcdabc', 'xkcd ball', 'donkey']) ->
     -> ['cow', 'calvinabc', 'calvin ball', 'donkey'] """
    pass

def even_odd_product(lst):
    """ Given a list of integers, sum up all the even numbers and all
    the odd numbers, and return the product of the 2 sums.

    E.g.,
     even_odd_product([1, 2, 3, 4, 6]) -> 48 (i.e., (2 + 4 + 6)*(1 + 3)) """
    pass

def pop_while(lst):
    """ Given a list, `lst`, of integers, compute the sum of all its elements.

    To experience a different loop pattern, use a while loop whose
    condition is `lst` (i.e., 'while lst:'; this will continue iterating
    while `lst` is non-empty) and perform a `lst.pop` at each iteration. """
    pass


###############################################
#               FUNCTIONS!                    #
###############################################

""" Write a function named `my_affirmer` that takes no  arguments and
always returns True. """

""" Write a function named `my_product` that takes 2 arguments (`a` and `b`)
and returns their product. """

#++++++++++++++++++++++++++++++++++++++++++++++#
#           END INTRODUCTION FUNCTIONS         #
#++++++++++++++++++++++++++++++++++++++++++++++#

#######################
### File operations ###
#######################

def initialize_file(filename, contents):
    """ Create a file named `filename` containing the string `contents`. """
    pass

def edit_existing_file(filename):
    """ Capitalize the contents on disk of the file named `filename`. """
    pass

def append_to_file(filename, to_append):
    """ Append the string `to_append` to the file named `filename`.
    Return the original size of the file, in bytes.

    Hint: Open the file in append mode, and get the file size before
    appending the string. """
    pass

def get_file_info(filename):
    """ Print the file size, time of creation, and last modification time.

    Use the datetime module and the formatting string below. """
    pass

    datetime_fmt = "%H:%M:%S on %d/%m/%Y"
def delete_file(filename):
    """ Delete the file named `filename`. """
    pass

#####################
### Generic logic ###
#####################

def return_multiple_values(a, b):
    """ Return both arguments. """
    pass

def recursive_multiplication(x, y):
    """ Use recursion to find the result of multiplying `x` and `y`. """
    pass

def parity(x):
    """ Return 0 if `x` is even and 1 if `x` is odd. """
    pass

def compare(x, y):
    """ Return -1, 0, or 1 if `x` is less than, equal to, or greater than,
    respectively, `y`. """
    pass
