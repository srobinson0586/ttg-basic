#!/bin/python
# Python Basic Syntax - Pytest Suite
import subprocess

def test_basic_syntax():
    function_output = subprocess.check_output('python application.py'.split()) 
    assert function_output.strip() == b'Hello World', 'Incorrect output, try again!'