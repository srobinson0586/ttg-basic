#!/bin/python
# Python Competency 6A Json Parser

""" This module implements functions for parsing JSON files.

For this project, you may assume that there is a new line after each:
- opening curly brace of an object
- opening square bracket of an array
- key-value pair in an object
- value in an array.

Look at how the data in `network.json` is formatted as a reference.


###################
# Module structure
###################

There are 5 main functions in this module:
1. `parse_json`
2. `parse_object`
3. `parse_array`
4. `parse_value`
5. `parse_string`

Each function's docstring gives an extensive explanation of its purpose
and the functions on which it depends.
"""

def parse_string(string):
  """ Parse a Python string that represents a JSON string.

  For example, if `string` is '"hello"', this function will return
  the Python string "hello". 
  """
  # TODO: Implement the function
  pass

def parse_array(f):
  """ Parse an array from a JSON file.

  Return a list of the values that appear in the JSON array. Each
  value can be any of the following:
  - an integer
  - a string
  - an object
  - an array

  The stream `f` is positioned on the line immediately following the
  opening square bracket.

  This function should basically read lines from the file until it reaches
  a closing square bracket. It should pass each line to `parse_value`
  """
  # TODO: Implement the function
  pass

def parse_object(f):
  """ Parse an object from a JSON file.

  Return a dictionary with a key-value pair for each field of the JSON
  object. The keys will all be JSON strings. Each value can be any of the following:
  - an integer
  - a string
  - an object
  - an array

  The stream `f` is positioned on the line immediately following the
  opening curly brace.

  This function should basically read lines from the file until it reaches
  a closing curly brace. For each line, it should:
  1. split it on the colon
  2. call `parse_string` on the left side to get the key
  3. call `parse_value` on the right side to get the value
      - This might end up processing many additional lines from the file
        if the value is an object or an array
  """
  # TODO: Implement the function
  pass

def parse_value(value, f):
  """ Parse a JSON value that could be an object, array, string, or int.

  `value` will be a string read from the JSON file `f`.
  - It may include arbitrary whitespace.
  - It may include a trailing comma.

  The stream `f` is positioned on the line after the line `value` was
  read from.

  Examples:
  - " 356," represents the integer 356. In this case, this function must
    return the Python integer 356.

  - '"hello!",' represents the string "hello!". In this case it will be
    useful to call `parse_string`.

  - " [" represents the start of a new array. This function will have to
    call `parse_array` on `f` to get the contents of the array from the
    following lines of `f`.

  - "{" represents the start of a new object. This function will have to
    call `parse_object` on `f` to get the contents of the object from the
    following lines of `f`. 
  """
  # TODO: Implement the function
  pass

def parse_json(filename):
  """ Open a JSON file by name and parse it.

  You may assume all the contents are contained in a single object whose
  opening curly brace is on the first line of the file. 
  """
  # TODO: Implement the function
  pass

if __name__ == "__main__":
  """ 
  Test your implementation on "network.json".
  If you're having any trouble, create a much smaller, simpler JSON
  file and test it on that to debug. 
  """
  # TODO: Implement the function
  pass
