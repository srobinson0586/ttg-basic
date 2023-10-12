#!/bin/python
# Python Competency 6A Json Parser - Pytest Suite
import parse
import json

def test_competency_6a_json_parser():
    assert json.load(open('network.json')) == parse.parse_json('network.json'), 'parse.parse_json(); Incorrect Python dictionary returned'
