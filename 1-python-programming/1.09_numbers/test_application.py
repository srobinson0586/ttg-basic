#!/bin/python
# Python Numbers - Pytest Suite

import application
import math

def test_numerical():
    assert type(getattr(application, 'radius', None)) is int, "'radius' was not set as an integer"
    assert getattr(application, 'radius', -1) >= 1 and getattr(application, 'radius', -1) <= 10, "'radius' is not a value between 1 and 10"
    assert getattr(application, 'circumference', 0.0) == 2 * getattr(application, 'radius', 0.0) * math.pi, "'circumference' calculation is incorrect"
    assert getattr(application, 'area', 0.0) == math.pi * math.pow(getattr(application, 'radius', 0.0), 2), "'area' calculation is incorrect"
    assert type(getattr(application, 'scores', None)) is list, "'scores' was not properly initialized as a list"
    assert len(getattr(application, 'scores', [])) >= 5, "'scores' does not contain at least five values"
    for i in getattr(application, 'scores', []):
        assert type(i) == float, "element in 'scores' is not a float"
    assert max(getattr(application, 'scores', [])) == getattr(application, 'best_score', -1.0), "'best_score' does not hold the value of the highest score"
    assert type(getattr(application, 'not_rounded', None)) is float, "'not_rounded' was not set as a floating point"
    assert getattr(application, 'rounded', None) == round(getattr(application, 'not_rounded', None))