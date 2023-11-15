#!/bin/python
# Python Modules - Pytest Suite

import application

def test_modules():
    myNums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
    myPrimes = [1,2,3,5,7,11,13]
    myFunc = application.myFunction
    
    theirPrimes = myFunc(myNums)
    assert myPrimes == theirPrimes, "Incorrect prime numbers returned. Address errors and retry."
