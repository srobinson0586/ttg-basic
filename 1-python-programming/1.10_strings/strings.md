# Python - Strings

Strings are amongst the most popular types in Python. We can create them simply by enclosing characters in quotes. Python treats single quotes the same as double quotes. Creating strings is as simple as assigning a value to a variable. For example:

```python
var1 = 'Hello World!'
var2 = "Python Programming"
```
> A quick note on style: although you can use either single or double quotes in Python, consistency is important when choosing between the two. Mixing both types of quotes within the same codebase should be avoided to ensure clean and readable code.

If we wanted to create an empty string to update at a later time, then we could do either of the following:

```python
str1 = ""       # One way to create an empty string
str2 = str()    # Another way to create an empty string
```

## Accessing Values

Python does not support a character type like C; it instead treats individual characters as strings of length one, thus also considered a substring.

To access a single character of a string, use  square brackets and the index of the character in the string. For example:

```python
name = 'H4ck3r'

print("name[0]: ", name[0]) # Get the first character (index 0) of the string
```

**Output**

```
name[0]: H
```

## Accessing Values: Slicing

*Slicing* is another very useful way to access specific characters in a string, though it works for more than just strings.

Slicing in Python refers to the technique of extracting a portion of a sequence, such as a string, list, tuple, or any other iterable object. Slicing allows you to create a new sequence that contains a selected range of elements from the original sequence, without modifying the original sequence itself.

The general syntax for slicing is: `sequence[start:stop:step]`

- `start`: The index where the slice starts (inclusive). If omitted, slicing starts from the beginning of the sequence (index 0).

- `stop`: The index where the slice ends (exclusive). The slice includes elements up to, but not including, the index specified here. If omitted, slicing goes up to the end of the sequence.

- `step`: The interval between elements in the slice. If omitted, the default step is 1, meaning consecutive elements are included.

Here is an example that shows how slicing can be used for a string:

```python
my_string = "BaBaBooey"
print(my_string[2:7])  # Slice from index 2 to 6
print(my_string[:-1])  # Slice from beginning of string to 2nd last character
print(my_string[2:])   # Slice from index to to final character
print(my_string[::2])  # Slice entire string with step=2
print(my_string[::-1]) # Slice entire string with step=-1
```

**Output**

```
BaBoo
BaBaBooe
BaBooey
BBBoy
yeooBaBaB
```

More information on slicing can be found [here](https://www.geeksforgeeks.org/python-list-slicing/).

## Length of a String using `len()`

A very useful function that can be used with strings is `len()`, which simply returns the integer length of a string. This can be useful for determining an upper bound to use for string indexing, which in turn can be useful for things like looping or validation.

```python
my_string = "The quick brown fox jumps over the lazy dog"
x = len(my_string)
print(x)
```

Output

```
43
```

## Concatenating and Repeating Strings

Python supports string concatenation and repetition though the `+` and `*` operators, respectively.  These operations provide flexibility when working with strings, allowing you to combine multiple strings or repeat a string multiple times based on your requirements. The following code snippet shows how you might practice using these operations:

```python
# Using the '+' operator for concatenation
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)

# Using the '*' operator for repetition
str3 = "Python"
repeated_str = str3 * 3
print(repeated_str)
```

The output of the above would be:

```
Hello World
PythonPythonPython
```

## Updating Strings

Python strings are immutable, meaning we cannot change them once they have been created. However, we can "update" an existing string by (re)assigning a variable to another string. The new value can be related to its previous value or to a completely different string altogether. For example:

```python
var1 = 'Hello World!'
var1 = var1[:6] + 'Python'
print("Updated String:", var1)
```

When the above code is executed, it produces the following result:

```
Updated String: Hello Python
```

## Truthiness of Strings

Just like numerical types, we can derive `True` or `False` values from Python strings, making them flexible for use in conditional statements.

Any string with at least one character has a truthiness of `True`. Empty strings (`""`) are `False`. The following code snippet uses conditional statements to demonstrate string truthiness:

```python
# Empty string evaluates to False
empty_string = ""
if empty_string:
    print("This won't be printed.")
else:
    print("Empty string is considered False.")

# Non-empty string evaluates to True
non_empty_string = "Hello, world!"
if non_empty_string:
    print("Non-empty strings are considered True.")
else:
    print("This will not be printed.")
```

Output of the above snippet:

```
Empty string is considered False.
Non-empty strings are considered True.
```

## Iterating through Strings

For some applications it may be necessary to iterate through a string using a loop. This might be the case if you need to count characters, parse for content, manipulate the string, find a specific pattern, etc. 

There are several ways to loop through a string.
A simple way to traverse a string character by character is with a `for` loop set up like the following:

#### Method 1

```python
my_string = "Hello, world!"

for char in my_string:
    print(char)
```

* * *

Another method that you might see is to use the `len()` function to get the length of a string, then to combine that with the `range()` function to generate a sequence of numbers that fall within the bounds of the string. This sequence can be used with a `for` loop to index into every character of the string:

#### Method 2

```python
my_string = "Hello, world!"

for i in range(len(my_string)):
    print(my_string[i])
```

The above method works, but when working using both indices and values with `for` loops, it is often better to use `enumerate` as described in [1.06_loops](../1.06_loops/loops.md).

* * *

Similar to Method 2, we can combine the `len()` function with a `while` loop to iterate through a string. Using this method will require a counter to be set and updated for each iteration of the `while` loop.

#### Method 3

```python
my_string = "Hello, world!"

i = 0   # counter for each iteration
while i < len(my_string):
    print(my_string[i])
    i += 1
```
* * *

All above methods yield the same output:

```
H
e
l
l
o
,

w
o
r
l
d
!
```

## f-Strings

In Python, f-strings (formatted string literals) are a convenient and powerful way to create formatted strings. They were introduced in Python 3.6 and offer a concise and readable syntax for embedding expressions and variables directly into strings.

The f-string syntax is straightforward: you prefix the string with the prefix `f` or `F` and place expressions inside curly braces `{}` within the string. When the f-string is evaluated, the expressions within the curly braces are replaced with their corresponding values.

Here's a basic example:

```python
name = "John"
age = 30

# F-string to create a formatted string
message = f"My name is {name} and I am {age} years old."
print(message)
```

Output

```
My name is John and I am 30 years old.
```

Python f-strings can also support various function calls, arithmetic operations, and methods that access object attributes.

You may encounter formatted strings that use `str.format()` like:

```python
name = "H4ck3r"
print("My name is {}".format(name))
```

or strings formatted with `%` like:

```python
name = "H4ck3r"
print("My name is %s" % name)
```

While still valid for formatting strings, the two examples above are not as readable or clean as using f-strings. In your own code, you should practice using f-strings over other methods.

## Byte Strings

In Python, a byte string is a specific type of string representation that allows you to work with binary data. It was introduced in Python 2 and continues to be supported in Python 3. Working with raw binary data is beneficial in applications that deal with binary files, networking, cryptography, hashing, and encoding.

In Python, a byte string is denoted by the prefix `b` or `B`, followed by the actual bytes data enclosed within single quotes (`'`) or double quotes (`"`). Byte strings can only be created this way in Python 3.

Unlike regular strings (unicode strings), which store text data encoded in UTF-8 by default in Python 3, byte strings store raw binary data as a sequence of bytes. Each byte in the byte string represents an 8-bit value.

Here is an example of how to define and use byte strings:

```python
# Defining a b-string with binary data (ASCII values for "Hello world")
binary_data = b'\x48\x65\x6c\x6c\x6f\x20\x77\x6f\x72\x6c\x64'
print(binary_data)
print(type(binary_data))
```

Output

```
b'Hello world'
<class 'bytes'>
```

A byte string is a textual representation of a `bytes` object. Strings and byte strings can be implicitly converted back and forth between `bytes` objects and a `str` objects using the `encode()` and `decode()` methods respectively.

We can use `decode()` on a byte string to obtain a normal string:

```python
binary_str = b'\x61\x62\x63'
print(binary_str.decode())
```

Output

```
abc
```

We can also convert a string to a bytes object using `encode()`:

```python
my_str = "abc"
print(my_str.encode())
```

Output

```
b'abc'
```

## Raw Strings

In Python, a raw string is a specific type of string representation that treats backslashes (`\`) as literal characters rather than escape characters. Raw strings are denoted by the prefix `r` or `R`, followed by the actual string data enclosed within single quotes (`'`) or double quotes (`"`).

In regular (non-raw) strings, backslashes are used to escape special characters, such as newline (`\n`), tab (`\t`), and others. For example, the string `"Hello\nWorld"` contains a newline character between "Hello" and "World". When printed, it will be displayed as:

```
Hello
World
```

On the other hand, a raw string with the same content, `r"Hello\nWorld"`, will treat the backslash and the following 'n' as literal characters, and the output will be:

```
Hello\nWorld
```

Raw strings are particularly useful when working with regular expressions, Windows file paths (which often use backslashes), and any other situation where you need to include backslashes without the need to escape them.

## Misc Functions and String Methods

When we are dealing with strings, we can simplify our code and get the most out of our programs by using Python's many built-in functions and methods for strings. A more complete list is available at [Tutorialspoint](https://www.tutorialspoint.com/python/python_strings.htm), but some useful functions/methods are shown below:

* **`capitalize()`**: Capitalizes the first letter of string.

* **`count(str)`**: Counts how many times `str` occurs in string.

* **`decode()`**: Decodes the string using the codec registered for encoding. encoding defaults to the default string encoding.

* **`encode()`**: Returns encoded string version of string; on error, default is to raise a ValueError unless errors is given with 'ignore' or 'replace'.

* **`endswith(suffix)`**: Determines if string ends with `suffix`; returns true if so and false otherwise.

* **`find(str)`**: Determine if `str` occurs in string; returns index if found or -1 otherwise.

* **`index(str)`**: Same as `find()`, but raises an exception if `str` not found.

* **`isalnum()`**: Returns `True` if string has at least 1 character and all characters are alphanumeric; otherwise returns `False`.

* **`isalpha()`**: Returns `True` if string has at least 1 character and all characters are alphabetic; otherwise returns `False`.

* **`isdigit()`**: Returns `True` if string contains only digits; otherwise returns `False`.

* **`islower()`**: Returns `True` if string has at least 1 cased character and all cased characters are in lowercase; otherwise returns `False`.

* **`isnumeric()`**: Returns `True` if a unicode string contains only numeric characters; otherwise returns `False`.

* **`isspace()`**: Returns `True` if string contains only whitespace characters; otherwise returns `False`.

* **`isupper()`**: Returns `True` if string has at least one cased character and all cased characters are in uppercase; otherwise returns `False`.

* **`join(seq)`**: Merges (concatenates) the string representations of elements in sequence `seq` into a string, with separator string.

* **`len(string)**`**: Returns the length of `string`

* **`lower()`**: Converts all uppercase letters in string to lowercase.

* **`lstrip()`**: Removes all leading whitespace in string.

* **`max(str)`**: Returns the max alphabetical character from the string `str`.

* **`min(str)`**: Returns the min alphabetical character from the string `str`.

* **`replace(old, new)`**: Replaces all occurrences of `old` in string with `new`.

* **`rstrip()`**: Removes all trailing whitespace of string.

* **`split(str)`**: Splits string according to delimiter `str` (space if not provided) and returns list of substrings.

* **`startswith(str)`**: Determines if string starts with substring `str`; returns true if so and false otherwise.

* **`strip()`**: Performs both `lstrip()` and `rstrip()` on string.

* **`swapcase()`**: Inverts case for all letters in string.

* **`upper()`**: Converts lowercase letters in string to uppercase.

* **`isdecimal()`**: Returns `True` if a unicode string contains only decimal characters; otherwise returns `False`.

Note: The functions `isdecimal()`, `isdigit()`, and `isnumeric()` provide similar functionality, but have different behaviors. To learn more about the differences between them, check out https://www.learnbyexample.org/python-string-isdecimal-method/.

## The `in` Keyword

A quick and very readable way to achieve `find()`-like behavior is to use the `in` keyword. In Python, the `in` keyword is used as a membership operator to check whether a substring exists within a larger string. It allows you to perform substring searching in a concise and straightforward manner. The `in` keyword returns a boolean value (True or False) based on whether the substring is found or not.

#### Example 1

```python
text = "Look at you acing the JQR like an absolute beast"
substring = "absolute"

if substring in text:
    print("Substring found.")
else:
    print("Substring not found.")
```

#### Output

```
Substring found.
```

#### Example 2

```python
text = "Hello, World!"
substring = "Python"

if substring in text:
    print("Substring found.")
else:
    print("Substring not found.")
```

#### Output

```
Substring not found.
```

The `in` keyword is case-sensitive, meaning it considers the case of the characters when performing the substring search. If you need a case-insensitive search, you can convert both the substring and string to lowercase (or uppercase) before using the `in` keyword:

#### Example 3

```python
text = "HELLO, WORLD!"
substring = "world"

if substring.lower() in text.lower():
    print("Substring found (case-insensitive search).")
else:
    print("Substring not found (case-insensitive search).")
```

#### Output

```
Substring found (case-insensitive search).
```

# Resources

- [Python List Slicing | Geeksforgeeks](https://www.geeksforgeeks.org/python-list-slicing/)

# Sources

- [Python Strings | Tutorialspoint](https://www.tutorialspoint.com/python/python_strings.htm)

[Back to README](README.md)