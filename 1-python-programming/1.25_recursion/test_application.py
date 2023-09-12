#!/bin/python
# Python Recursion - Pytest Suite

import application
import random

def test_recursion():
    # Staging
    myInteger = random.randint(1, 131071)
    myBinaryString = bin(myInteger)

    # Checking user-implemented function for correct execution
    theirBinaryString = application.myIntToBinary("",myInteger)
    
    # Checking if the strings match
    assert myBinaryString == theirBinaryString, f"Your recursive call did not return the correct value of {myBinaryString}"