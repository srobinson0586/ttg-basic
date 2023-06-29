#!/bin/python
# Python Basic Syntax - Pytest Suite
import subprocess

def test_basic_syntax():
    function_output = subprocess.check_output('python application.py'.split()) 
    is_correct = function_output == b'Hello World\n'
    assert is_correct, 'Incorrect output, try again!'