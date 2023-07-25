#!/bin/python
# Python Dictionaries - Application


# 1: Merge Dictionaries
# Implement a function that takes two dictionaries as input and merges them into a single dictionary.
# If there are any common keys, the value from the second dictionary should overwrite the value from the first dictionary.
def merge_dictionaries(dict1, dict2):
    merged_dict = dict1.copy()
    merged_dict.update(dict2)
    return merged_dict

# 2: Filter Dictionary
# Implement a function that takes a dictionary and a list of keys as input.
# The function should return a new dictionary that only contains the key-value pairs from the original dictionary
# whose keys are present in the given list.
def filter_dictionary(dictionary, keys):
    filtered_dict = {key: dictionary[key] for key in keys if key in dictionary}
    return filtered_dict

# 3: Count Values
# Implement a function that takes a dictionary as input and returns a new dictionary
# where the keys are the unique values from the original dictionary and the values are the count of occurrences of each value.
def count_values(dictionary):
    count_dict = {}
    for value in dictionary.values():
        if value in count_dict:
            count_dict[value] += 1
        else:
            count_dict[value] = 1
    return count_dict

# 4: Remove Keys
# Implement a function that takes a dictionary and a list of keys as input.
# The function should remove the key-value pairs from the dictionary for the keys present in the given list.
def remove_keys(dictionary: dict, keys: list):
    for key in keys:
        dictionary.pop(key, None)
