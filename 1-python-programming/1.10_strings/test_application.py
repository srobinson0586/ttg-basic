#!/bin/python
# Python Strings - Pytest Suite

import application

def test_strings():
    assert getattr(application, "str1", "") == "foo", "str1 was not set to 'foo'"
    assert getattr(application, "str2", "") == "bar", "str2 was not set to 'bar'"
    assert getattr(application, "str3", "") == "foobar", "str3 is not 'foobar'"
    assert getattr(application, "vowel_count", 0) == sum(1 for c in application.sentence if c in "aeiouAEIOU"), "incorrect vowel_count"
    assert getattr(application, "food", "") == "I want a hamburger because I am hungry.", "'sandwich' not changed to 'hamburger'"
    assert getattr(application, "all_caps", "") == application.sentence.upper(), "transformation of 'sentence' was incorrect"
