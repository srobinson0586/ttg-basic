import os
import time
import datetime

#######################
### File operations ###
#######################

def initialize_file(filename, contents):
    """ Create a file named `filename` containing the string `contents`. """
def edit_existing_file(filename):
    """ Capitalize the contents on disk of the file named `filename`. """
def append_to_file(filename, to_append):
    """ Append the string `to_append` to the file named `filename`.
    Return the original size of the file, in bytes.

    Hint: Open the file in append mode, and get the file size before
    appending the string. """
def get_file_info(filename):
    """ Print the file size, time of creation, and last modification time.

    Use the datetime module and the formatting string below. """
    datetime_fmt = "%H:%M:%S on %d/%m/%Y"
def delete_file(filename):
    """ Delete the file named `filename`. """
#####################
### Generic logic ###
#####################

def return_multiple_values(a, b):
    """ Return both arguments. """
def recursive_multiplication(x, y):
    """ Use recursion to find the result of multiplying `x` and `y`. """
def parity(x):
    """ Return 0 if `x` is even and 1 if `x` is odd. """
def compare(x, y):
    """ Return -1, 0, or 1 if `x` is less than, equal to, or greater than,
    respectively, `y`. """
##########################
### Exception handling ###
##########################

def exception_handling():
    """ Cause an exception and catch it. Once you catch it, print a
    message saying what exception you caught. """