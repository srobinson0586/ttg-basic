#!/bin/python
# Python Typecasting - Pytest Suite
import application
from base64 import b64decode

to_bytes_val = b64decode(b'OQUAAA==')
val_1 = b64decode(b'Yg==')

def test_variable_types():
    passed = True

    first = application.to_bytes(1337)
    assert first == to_bytes_val, 'to_bytes(); Incorrect return value'
    assert type(first) == bytes,  'to_bytes(); Incorrect return type'
    
    second = application.to_string(to_bytes_val)
    assert (second == to_bytes_val.decode()) or (second == str(to_bytes_val)), 'to_string(); Incorrect return value'
    assert type(second) == str, 'to_string(); Incorrect return type'

    third = application.to_dict(1, val_1, 'z', 78)
    assert third == {1:val_1, 'z':78}, 'to_dict(); Incorrect return value'
    assert type(third) == dict, 'to_dict(); Incorrect return type'
