#!/bin/python
# Python Functions - Pytest Suite
import application
from base64 import b64decode

enc_name = b'VE9QIEdVTiwgTUFWRVJJQ0s='
enc_greet = b'SGVsbG8gVE9QIEdVTiwgTUFWRVJJQ0s='
enc_fact = b'AF83AA=='

def test_functions():
    # Challenge 1.1: Setup Global Variable `counter`
    application.setup_increment_counter()
    try:
        assert application.counter == 0, 'setup_increment_counter(); Counter != 0'
    except AttributeError:
        assert False, 'setup_increment_counter(); Unable to find "counter" in global namespace'

    # Challenge 1.2: Function with Global Variable
    for i in range(10):
        application.increment_counter()
    first = application.increment_counter()
    assert first == 11, 'increment_counter(); Incorrect return value.'

    # Challenge 2: Function with Default Argument
    dec_name = b64decode(enc_name).decode()
    second = application.greet_person(name=dec_name)
    assert second == b64decode(enc_greet).decode(), 'greet_person(); Incorrect return value'

    # Challenge 3: Recursive Function
    dec_fac = int.from_bytes(b64decode(enc_fact), 'little', signed=False)
    third = application.calculate_factorial(10)
    assert third == dec_fac, 'calculate_factorial(); Incorrect return value'

    # Challenge 4: Function with Variable-Length Arguments
    fourth_1 = application.sum_numbers(10)
    assert fourth_1 == 10, 'sum_numbers(); Incorrect return value'
    fourth_2 = application.sum_numbers(92, 20, 42, 520, 23, 10, 243212)
    assert fourth_2 == 243919, 'sum_numbers(); Incorrect return value'
