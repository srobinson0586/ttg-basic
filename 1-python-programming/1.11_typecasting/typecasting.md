# Python Typecasting

[Back to README](README.md)

Typecasting, also known as type conversion, is the process of changing the data type of a value in Python. It allows you to convert variables from one type to another, depending on your requirements. Python provides several built-in functions for typecasting. Let's explore a few commonly used ones:

1. `int()`: This function is used to convert a value to an integer (whole number) type. For example:
```python
num_str = "10"
num_int = int(num_str)
print(num_int)  # Output: 10
```

2. `float()`: Use this function to convert a value to a floating-point (decimal) type. Here's an example:
```python
num_str = "3.14"
num_float = float(num_str)
print(num_float)  # Output: 3.14
```

3. `str()`: It converts a value to a string type. For instance:
```python
num_int = 42
num_str = str(num_int)
print(num_str)  # Output: "42"
```

4. `list()`, `tuple()`, and `set()`: These functions are used to convert values to list, tuple, and set types, respectively. They are covered more in depth in [1.12_lists_tuples_and_sets](../1.12_lists_tuples_and_sets/lists_tuples_and_sets.md). Here's an example of converting a string to a list:
```python
fruits_str = "apple,banana,orange"
fruits_list = fruits_str.split(",")
print(fruits_list)  # Output: ['apple', 'banana', 'orange']
```

5. `bytes()`: Constructs an immutable array of bytes from: an iterable yielding integers in range(256), a text string encoded using the specified encoding, any object implementing the buffer API, or an integer. You only really need to worry about the encoded text string conversion (for now), an example is shown below:
```python
>>> my_bytes = 'This will be byte stuff'
>>> print(my_bytes)
This will be byte stuff
>>> type(my_bytes)
<class 'str'>
>>> my_bytes = bytes(my_bytes, 'utf-8')
>>> print(my_bytes)
b'This will be byte stuff'
>>> type(my_bytes)
<class 'bytes'>
```

6. `chr()`, `ord()`: These functions convert integer values to a unicode character, and convert a unicode character to its code point (integer value) respectively. They're reciprocal.
```python
>>> my_val = 65
>>> chr(my_val)
'A'
>>> ord('A')
65
```

It's important to note that typecasting may not always be successful. For example, converting a string that doesn't represent a valid number to an integer will raise a `ValueError`.
```python
>>> bad_str = "bad string"
>>> bad_int = int(bad_str)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'bad string'
```

Therefore, it's essential to handle exceptions appropriately, which is covered more in depth in [1.28_exceptions](../1.28_exceptions/README.md).

Additionally, Python provides implicit type conversion in certain situations. For example, if you perform arithmetic operations involving different data types, Python automatically performs type conversion to obtain the result.

Typecasting is a useful tool for manipulating and working with different types of data in Python. Understanding how to convert between types will allow you to perform various operations efficiently.

Remember to explore the official Python documentation and experiment with different examples to deepen your understanding of typecasting. 

## References

- [Tutorialspoint Variable Types](https://www.tutorialspoint.com/python3/python_variable_types.htm)