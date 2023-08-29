#!/bin/python
# Python Dictionaries - Pytest Suite
import application
import base64

# Encoded vals
enc_dict1 = {b'YQ==': 1, b'Yg==': 2, b'Yw==': 3}
enc_dict2 = {b'Yg==': 4, b'ZA==': 5}
enc_merged = {b'YQ==': 1, b'Yg==': 2, b'Yw==': 3, b'Yg==': 4, b'ZA==': 5}
enc_dict2 = {b'Yg==': 4, b'ZA==': 5}
enc_keys_to_filter = [b'YQ==', b'Yw==', b'ZQ==']
enc_keys_to_rm = [b'Yg==', b'ZA==']

def test_dictionaries():
    # Challenge 1: Merge Dictionaries
    dict1 = {}
    for a,b in enc_dict1.items():
        dict1.update({(base64.b64decode(a)).decode() : b})
    dict2 = {}
    for a,b in enc_dict2.items():
        dict2.update({(base64.b64decode(a)).decode() : b})
    value_counts = {1: 1, 4: 1, 3: 1, 5: 1}
    merged_dict = {}
    for a,b in enc_merged.items():
        merged_dict.update({(base64.b64decode(a)).decode() : b})
    first = application.merge_dictionaries(dict1, dict2)
    assert merged_dict == first, 'merge_dictionaries(); Incorrect return value'

    # Challenge 2: Filter Dictionary
    keys_to_filter = [(base64.b64decode(a)).decode() for a in enc_keys_to_filter]
    filtered_dict = {}
    for a,b in merged_dict.items():
        if (a in merged_dict) and (a in keys_to_filter):
            filtered_dict.update({a : b})
    second = application.filter_dictionary(merged_dict, keys_to_filter)
    assert second == filtered_dict, 'filter_dictionary(); Incorrect return value'

    # Challenge 3: Count Values
    third = application.count_values(merged_dict)
    assert third == value_counts, 'count_values(); Incorrect return value'

    # Challenge 4: Remove Keys
    keys_to_remove = [(base64.b64decode(a)).decode() for a in enc_keys_to_rm]
    application.remove_keys(merged_dict, keys_to_remove)
    assert merged_dict == filtered_dict, 'remove_keys(); Incorrect return value'
