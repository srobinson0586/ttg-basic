#!/bin/python
# Python Variable Types - Pytest Suite
import application
from base64 import b64decode

def test_variable_types():
    number = b64decode(''.join(
        'MzgxNTY4MTE3MzM4MzgxMDk' + 
        '3NDIxNTY5MjkxMzQyMTE3MD' +
        'c1NDA1NjE4NDY3Njc2MDk1O' +
        'Tg3MDk2OTUw')
    )
    assert getattr(application, 'name', '') == 'Bob', '"name" variable incorrect'
    assert not getattr(application, 'gone', None), '"gone" variable exists'
    assert getattr(application, 'solution', 0) == int(number), '"solution" variable incorrect'
    things = getattr(application, 'things', None)
    assert type(things) is list, '"things" variable not list'
    assert (len(things) == 3), 'Things: incorrect length'
    assert type(things[0]) is int, 'Things: first element is not an integer'
    assert type(things[1]) is str, 'Things: second element is not a string'
    assert type(things[2]) is list, 'Things: third element is not a list'
        