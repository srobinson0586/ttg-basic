#!/bin/python
# Python Competency 7A JSON Parser - Pytest Suite
import parse
import json

def test_competency_7a_json_parser():
    assert json.load(open('network.json')) == parse.parse_json('network.json'), 'parse.parse_json(); Incorrect Python dictionary returned'
