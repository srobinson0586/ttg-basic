# Python Dictionaries

[Back to README](README.md)


In dictionaries, each key is separated from its value by a colon (:), the items are separated by commas, and the whole thing is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: `{}`.

*Keys are unique* within a dictionary while values may not be. The *values of a dictionary can be of any type*, but the *keys must be of an immutable data type* such as strings, numbers, or tuples.

### Accessing Values in a Dictionary

To access dictionary elements, you can use the familiar square brackets along with the key to obtain its value. Following is a simple example:

```py
dict = {'Name': 'Tovar', 'Age': 7, 'Class': 'First'}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
```

When the above code is executed, it produces the following result:
```
dict['Name']:  Tovar
dict['Age']:  7
```

If we attempt to access a data item with a key which is not a part of the dictionary, we get an error as follows:
```py
dict = {'Name': 'Tovar', 'Age': 7, 'Class': 'First'};
print ("dict['Alice']: ", dict['Alice'])
```

When the above code is executed, it produces the following result:
```
dict['Alice']:
Traceback (most recent call last):
   File "test.py", line 4, in <module>
      print "dict['Alice']: ", dict['Alice'];
KeyError: 'Alice'
```

### Updating a Dictionary

You can update a dictionary by adding a new entry or a key-value pair, modifying an existing entry, or deleting an existing entry as shown in a simple example given below:
```py
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
dict['Age'] = 8; # update existing entry
dict['School'] = "NCWDG Dev Pipeline" # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

When the above code is executed, it produces the following result:
```
dict['Age']:  8
dict['School']:  NCWDG Dev Pipeline
```

### Deleting Dictionary Elements

You can either remove individual dictionary elements or clear the entire contents of a dictionary. You can also delete entire dictionary in a single operation. To explicitly remove an entire dictionary, just use the **del** statement. Following is a simple example:
```py
dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}

del dict['Name'] # remove entry with key 'Name'
dict.clear()     # remove all entries in dict
del dict         # delete entire dictionary

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

This produces the following result. An exception is raised because after **del dict**, the dictionary does not exist anymore.
```
dict['Age']:
Traceback (most recent call last):
   File "test.py", line 8, in <module>
      print "dict['Age']: ", dict['Age'];
TypeError: 'type' object is unsubscriptable
```

### Properties of Dictionary Keys

Dictionary values have no restrictions. They can be any arbitrary Python object, either standard objects or user-defined objects. *However*, same is not true for the keys.

There are two important points to remember about dictionary keys:

1. **More than one entry per key is not allowed**. This means no duplicate key is allowed. When duplicate keys are encountered during assignment, the last assignment wins:
```py
dict = {'Name': 'Zara', 'Age': 7, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])
# dict['Name']:  Manni
```

2. **Keys must be immutable**. This means you can use strings, numbers or tuples as dictionary keys but something like `['key']` is not allowed:
```py
dict = {['Name']: 'Zara', 'Age': 7}
print ("dict['Name']: ", dict['Name'])
```

When the above code is executed, it produces the following result:
```
Traceback (most recent call last):
   File "test.py", line 3, in <module>
      dict = {['Name']: 'Zara', 'Age': 7}
TypeError: list objects are unhashable
```

### Built-in Dictionary Functions and Methods

Python includes the following dictionary functions:
|Sr.No.| Function & Description |
|------|------------------------|
|  1   | `cmp(dict1,  dict2)`: No longer available in Python 3. |
|  2   | `len(dict)`: Gives the total length of the dictionary  |
|  3   | `str(dict)`: Produces a string representation of a dictionary |
|  4   | `type(variable)`: Returns the type of the passed variable |


Python includes the following dictionary methods:
|Sr.No.| Method & Description |
|------|------------------------|
|  1   |  `dict.clear()`: Removes all elements of dictionary dict |
|  2   |  `dict.copy()`: Returns a shallow copy of dictionary dict |
|  3   |  `dict.fromkeys(iterable, value=None)`: Creates a new dictionary with keys from `iterable` and values all set to `value` |
|  4   |  `dict.get(key, default=None)`: Returns value for key `key`, or `default` if key is not in dictionary |
|  5   |  `dict.items()`: Returns a list of dict's `(key, value)` tuple pairs |
|  6   |  `dict.keys()`: Returns alist of dictionary `dict`'s keys |
|  7   |  `dict.setdefault(key, default = None)`: Similar to `get()`, but will set `dict[key] = default` if key is not already in dict |
|  8   |  `dict.update(dict2)`: Adds dictionary dict2's key-values pairs to dict |
|  9  | `dict.values()`: Returns list of dictionary dict's values |

### Finding Items in Dictionaries

You can easily determine if a dictionary has a certain **key** by using the `in` keyword:
```py
d = {'a': 8, 'b': 9, 'c': 1, 'd': 4}
if 9 in d:
    print("9 is in the dict")
# no print, since 9 is  a value
if 'a' in d:
    print('"a" is in the dict"')
# "a" is in the dict"
```

You can determine if a dictionary has a certain **value** by using the `in` keyword on the return from the `dict.values()` method:
```py
d = {'a': 8, 'b': 9, 'c': 1, 'd': 4}
if 9 in d.values():
    print("9 is in the dict")
# 9 is in the dict
if 'a' in d.values():
    print('"a" is in the dict"')
# no print, "a" is a key
```

### JSON

Python dictionaries are very similar to JavaScript Object Notation (JSON) is an open standard file format and data interchange format that uses human-readable text to store and transmit data objects consisting of attribute–value pairs and arrays. The following is an example:
```json
{
    "API_KEY": "RU5TIFRvdmFyLU1hcnF1ZXogd2F6IGhlcmUgPjopIA==",
    "SEC_LVL": 3,
    "Name" : {
        "First": "Sailor",
        "Last": "Timmy"
    }
}
```

As you can see, JSON is quite similar to python dictionaries. **However**, remember the limitations of python dicts:

> *Keys are unique* within a dictionary while values may not be. The *values of a dictionary can be of any type*, but the *keys must be of an immutable data type* such as strings, numbers, or tuples.

More on the difference between JSON and Python Dictionaries can be read on this [Medium Article](https://medium.com/analytics-vidhya/python-dictionary-and-json-a-comprehensive-guide-ceed58a3e2ed).

There is a python module (modules covered in [1.16_modules](../1.16_modules)) called `json` that can be used to more easily work with JSON. It is covered more in depth in [1.26_json](../1.26_json), but here is a small demo:
```py
import json
my_json = json.loads('{"API_KEY":"RU5TIFRvdmFyLU1hcnF1ZXogd2F6IGhlcmUgPjopIA==","SEC_LVL":3,"Name":{"First": "Sailor","Last":"Timmy"}}')
print(json.dumps(my_json, indent=2))
#{
#  "API_KEY": "RU5TIFRvdmFyLU1hcnF1ZXogd2F6IGhlcmUgPjopIA==",
#  "SEC_LVL": 3,
#  "Name": {
#    "First": "Sailor",
#    "Last": "Timmy"
#  }
#}
```

## References

- [Tutorialspoint- Dictionaries](https://www.tutorialspoint.com/python3/python_dictionary.htm)
- [Wikipedia- JSON](https://en.wikipedia.org/wiki/JSON)