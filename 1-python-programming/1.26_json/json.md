# Python JSON

## JSON

JSON (**J**ava**S**cript **O**bject **N**otation) is a lightweight data-interchange format. It is easy for humans to read and write, and its easy to write code that parses and generates it.

JSON is built on two structures.
- A collection of name/value pairs, which is called an *object*
    - `{ <key> : <value> }`
- An ordered list of values, which allows an object's key to map to many values
    - ```json
        { 
            "my_key" : [
                "val1",
                "val2",
                ]
        }
      ```

In Python, JSON exists as a string, and is extremely similar in structure to `dictionaries`. For example:
```py
p = '{"name": "Bob", "languages": ["Python", "Java"]}'
```

The table below shows some Python types and their equivalent conversion to JSON.

| Python                | JSON Equivalent |
| --------------------- | --------------- |
| `dict`                | object          |
| `list`, `tuple`       | array           |
| `str`                 | string          |
| `int`, `float`, `int` | number          |
| `True`                | true            |
| `False`               | false           |
| `None`                | null            |

## Python `json` Module

To work with JSON, you can use Python's `json` module. It provides several useful functions, the most important of which are `loads()`, `dumps()`, `load()`, and `dump()`.
```py
import json
```

Keep in mind that in the examples that follow, we use a string that is defined within the script itself. However, in the real world, you would use the `json` module when you're working with data originating from external sources. Some examples would be: a Rest API's response, a project's JSON configuration file, and a website's POST request responses.

### Reading JSON

#### `loads()`
You can parse a JSON string using the `json.loads()` method. The method returns a dictionary, so that you can work more easily with the underlying data. Below is an example:
```py
>>> import json
>>> timmy_pii = '{"Name" : {"First" : "Sailor", "Second" : "Timmy"}, "Address" : "9800 Savage Rd #6623, Fort Meade, MD 20755", "SSN" : 123456789 }'
>>> timmy_pii['Name']       # Can't index the string like we need to
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: string indices must be integers, not 'str'

>>> timmy_json = json.loads(timmy_pii)
>>> timmy_json['Name']
{'First': 'Sailor', 'Second': 'Timmy'}
>>> timmy_json['Name']['Second']
'Timmy'
>>> timmy_json['SSN']
123456789
```

*Note*
> Notice that all the string JSON keys and values are defined using double quotes (`" "`). This is the JSON standard. If you use single quotes, then try to convert that to a dictionary using `json.loads`, you will get an error! 

#### `load()`

You can use the `json.load()` method to read a file containing JSON objects. Suppose, you have a file named `timmy.json` in your current directory that contains a JSON object:
```json
{
  "Name": {
    "First": "Sailor",
    "Second": "Timmy"
  },
  "Address": "9800 Savage Rd #6623, Fort Meade, MD 20755",
  "SSN": 123456789
}
```

To work with that data, you would do the following:
```py
import json

with open('timmy.json', 'r') as file:
    data = json.load(file)

print(data['Name']['First'])
# Sailor
```

Note that the file had to be *opened before* we were able to call `json.load`. That's because `json.load` takes a `.read()`-supporting, file-like, object (i.e. a file stream like that returned from `open()`).

### Writing JSON

#### `dumps()`

You can convert a dictionary to a JSON string using the `json.dumps()` method. 

When printing JSON strings with `dumps()` or `dump()` (covered next), there are two important argument that help to pretty-print the output. If you specify the `ident` argument it tells the methods to pretty-print the JSON object with that indentation level. The `sort_keys` argument tells the methods to sort the output based on the keys.

For example:
```py
>>> import json
>>> timmy_dict = {'Name': {'First': 'Sailor', 'Second': 'Timmy'}, 'Address': '9800 Savage Rd #6623, Fort Meade, MD 20755', 'SSN': 123456789}

>>> timmy_str = json.dumps(timmy_dict)
>>> print(timmy_str)                         # not easily readable
{"Name": {"First": "Sailor", "Second": "Timmy"}, "Address": "9800 Savage Rd #6623, Fort Meade, MD 20755", "SSN": 123456789}

>>> timmy_str = json.dumps(timmy_dict, indent=2) 
>>> print(timmy_str)                         # easily readable!
{
  "Name": {
    "First": "Sailor",
    "Second": "Timmy"
  },
  "Address": "9800 Savage Rd #6623, Fort Meade, MD 20755",
  "SSN": 123456789
}

>>> timmy_str = json.dumps(timmy_dict, indent=2, sort_keys=True)
>>> print(timmy_str)                         # even more easy to debug output
{
  "Address": "9800 Savage Rd #6623, Fort Meade, MD 20755",
  "Name": {
    "First": "Sailor",
    "Second": "Timmy"
  },
  "SSN": 123456789
}
```

#### `dump()`

To write JSON to a file in Python, you can use the `json.dump()` method.
```py
import json

timmy_dict = { 
    'Name': 
        {   'First': 'Sailor',
            'Second': 'Timmy'
        },
    'Address': '9800 Savage Rd #6623, Fort Meade, MD 20755',
    'SSN': 123456789
}

with open('timmy.json', 'w') as file:
  json.dump(timmy_dict, file, indent=2, sort_keys=True)     # don't forget the indent!
```

## Resources

- [Python JSON & APIs](https://realpython.com/api-integration-in-python/)

## Sources

- [JSON.org](https://www.json.org/json-en.html)

[Back to README](README.md)
