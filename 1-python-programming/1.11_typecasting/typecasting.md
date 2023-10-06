# Python Typecasting


Typecasting, also known as type conversion, is the process of changing the data type of a value in Python. It allows you to convert variables from one type to another, depending on your requirements. 

Classes and Data Types are joined at the hip in Python and there will be many references to Classes in this module. Unfortunately, they aren't covered until [1.20_classes_and_objects](../1.20_classes_and_objects/README.md) so if you want to read ahead, feel free to do so. You could also check out this [Python Classes & Instances Tutorial](https://www.youtube.com/watch?v=ZDa-Z5JzLYM).

Remember to explore the official Python documentation and experiment with different examples to deepen your understanding of typecasting. 

## Helpful Functions

Python has several useful builtin functions to help you navigate typecasting. The most important are: `type()`, `help()`, and `dir()`.

### `type()`

The `type()` function returns the underlying Data Type (Class in Python) of the variable you pass in. It can be useful when attempting to debug complex functions where you sometimes lose track of a variable's type:
```py
>>> a = 1
>>> b = "hello"
>>> type(a)
<class 'int'>
>>> type(b)
<class 'str'>
```

### `dir()`

The `dir()` function returns a list of the attributes of the passed in object, and of attributes reachable from it. Basically, it tells you everything that you can do with whatever you pass in. Its useful for when you're trying to find built-in Class methods that help you convert to different data types, or when you want to see everything available.

Below we explore some of the builtin methods for several common data type. Note that any data type attributes that don't help with type conversion have been removed from the below program output to avoid clutter. Feel free to run the code yourself to see everything:
```py
>>> dir(int)
[from_bytes, to_bytes] # ... etc
>>> dir(str)
[encode]  # ... etc
>>> dir(bytes)
[decode, fromhex, hex] # ... etc
```

### `help()`

The `help()` function is a wrapper around `pydoc.help` that provides the Docstring (covered in [1.15_functions](../1.15_functions/functions.md)) for whatever you pass in. Its a way around having to look around for class or function's documentation. **Its by far the most useful python function you will ever learn about!**

Its used below to look at the documentation for some of the useful built-in type conversion functions above in the `dir()` output. Again, the output is heavily cut, so run it on your own terminal to see more:
```py
>>> help(int.to_bytes)  # convert an int to bytes
Help on method_descriptor:

to_bytes(self, /, length=1, byteorder='big', *, signed=False)
    Return an array of bytes representing an integer.
....... etc .......

>>> help(str.encode)  # convert a string to bytes
Help on method_descriptor:

encode(self, /, encoding='utf-8', errors='strict')
    Encode the string using the codec registered for encoding.
....... etc .......

>>> help(bytes.decode)  # convert a byte sequence to a string
Help on method_descriptor:

decode(self, /, encoding='utf-8', errors='strict')
    Decode the bytes using the codec registered for encoding.
....... etc .......
```


## Explicit Typecasting

In most programming languages, there are generally two different forms of typecasting: Explicit and Implicit. In **Explicit Typecasting**, you manually add some code that tells the interpreter how you want a variable to be treated. Python provides several built-in functions for typecasting. Below are a few commonly used ones:

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
fruits_str = "apple,banana,orange,orange"
fruits_list = fruits_str.split(",")
print(fruits_list)  # Output: ['apple', 'banana', 'orange', 'orange']
fruits_set = set(fruits_list)
print(fruits_set)  # Output: {'apple', 'banana', 'orange'}
```
5. `bytes()`: Constructs an immutable array of bytes from any of: 
 - An iterable yielding integers in range(256), 
 - A text string encoded using the specified encoding, 
 - Any object implementing the buffer API, or 
 - An integer. 

    You only really need to worry about the encoded text string conversion (for now), an example is shown below:
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

## Implicit Typecasting

**Implicit Typecasting** occurs when you don't add any extra code and assume the interpreter will be able to handle the type conversion on its own. Python provides implicit type conversion in certain situations. Below are some examples:
```py
>>> a = 58
>>> b = 3.14
>>> c = a * b
>>> c
182.12

>>> d = a // b # Floor Division covered in 1.04_operators
>>> d
18.0
```

## Typecasting Errors

It's important to note that typecasting may not always be successful. For example, converting a string that doesn't represent a valid number to an integer will raise a `ValueError`.
```python
>>> bad_str = "bad string"
>>> bad_int = int(bad_str)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: invalid literal for int() with base 10: 'bad string'
```

Therefore, it's essential to handle exceptions appropriately, which is covered more in depth in [1.28_exceptions](../1.28_exceptions/README.md).


## References

- [Python Classes & Instances Tutorial](https://www.youtube.com/watch?v=ZDa-Z5JzLYM)

## Sources
- [Tutorialspoint Variable Types](https://www.tutorialspoint.com/python3/python_variable_types.htm)

[Back to README](README.md)
