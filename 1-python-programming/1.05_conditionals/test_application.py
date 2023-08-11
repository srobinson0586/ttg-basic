#!/bin/python
# Python Conditionals - Pytest Suite
import application

def my_conditionals():
    # Test challenge 1
    assert application.nested_conditionals(15) == '1337 or below', 'nested_conditionals(); incorrect return value'
    assert application.nested_conditionals(1337) == '1337 or below', 'nested_conditionals(); incorrect return value'
    assert application.nested_conditionals(4444) == 'Between 1338 and 4444', 'nested_conditionals(); incorrect return value'
    assert application.nested_conditionals(4445) == 'Above 4444', 'nested_conditionals(); incorrect return value'

    # Test challenge 2
    assert application.max_number(10, 15, 5) == 15, 'max_number(); incorrect return value'
    assert application.max_number(100, 50, 75) == 100, 'max_number(); incorrect return value'
    assert application.max_number(1923849843, 12931, -1234123) == 1923849843, 'max_number(); incorrect return value'
    
def test_conditionals():
    try:
        my_conditionals()
    except AssertionError as e:
        print(f"[-] Test FAILED: '{e}'")
        exit()

    print("[+] ALL TESTS PASSED!\n")
