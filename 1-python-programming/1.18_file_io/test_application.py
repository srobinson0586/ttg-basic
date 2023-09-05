#!/bin/python
# Python File IO - Pytest Suite

from application import myFileIO
from base64 import b64decode

def test_file_io():
    correctString = 'SSdtIHN0YXJ0aW5nIHRvIHVuZGVyc3RhbmQgRmlsZUlPIQ=='
    userData = myFileIO()
    passedTest = userData == b64decode(correctString).decode()
    assert passedTest, "Error in FileIO processing. Returned string does not match."

test_file_io()