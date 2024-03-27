#!/bin/python
# Python File IO - Pytest Suite

from application import myFileIO
from base64 import b64decode

def test_file_io():
    correctString = 'SSBhbSBsZWFybmluZyBtb3JlIGFib3V0IEZpbGVJTw=='
    userData = myFileIO()
    passedTest = userData == b64decode(correctString).decode()
    assert passedTest, "Error in FileIO processing. Returned string does not match."

test_file_io()