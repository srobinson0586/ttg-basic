# Python Variable Types

[Back to README](README.md)

Variables are nothing but reserved memory locations to store values. It means that when you create a variable, you reserve some space in the memory.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to the variables, you can store integers, decimals or characters in these variables.

Assigning Values to Variables
-----------------------------

Python variables do not need explicit declaration to reserve memory space. The declaration happens automatically when you assign a value to a variable. The equal sign (`=`) is used to assign values to variables.

The operand to the left of the `=` operator is the name of the variable and the operand to the right of the = operator is the value stored in the variable. For example −

```python
counter = 100  # An integer assignment
miles = 1000.0 # A floating point
name = "John"  # A string

print(counter)
print(miles)
print(name)
```

Here, `100`, `1000.0` and `"John"` are the values assigned to `counter`, `miles`, and `name` variables, respectively. This produces the following result −

```
100
1000.0
John
```


Multiple Assignment
-------------------

Python allows you to assign a single value to several variables simultaneously.

For example −

```python
a = b = c = 1
```


Here, an integer object is created with the value 1, and all the three variables are assigned to the same memory location. You can also assign multiple objects to multiple variables. For example −

```python
a, b, c = 1, 2, "john"
```


Here, two integer objects with values 1 and 2 are assigned to the variables a and b respectively, and one string object with the value "john" is assigned to the variable c.

Standard Data Types
-------------------

The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

There are different types of data types in Python. Some built-in Python data types are:
* **Numeric data types**: `int`, `float`, `complex`
* **Boolean type**: `bool`
* **String data types**: `str`
* **Sequence types**: `list`, `tuple`, `range`
* **Mapping data type**: `dict`
* **Binary types**: `bytes`, `bytearray`, `memoryview`
* **Set data types**: `set`, `frozenset`

Python Numbers
--------------

Number data types store numeric values. Number objects are created when you assign a value to them. For example −

```python
var1 = 1
var2 = 10
```

You can also delete the reference to any object by using the `del` statement. The syntax of the `del` statement is −

```python
del var1[,var2[,var3[....,varN]]]]
```


You can delete a single object or multiple objects by using the `del` statement.

For example −

```python
del var
del var_a, var_b
```


Python supports three different numerical types −

*   `int` (signed integers)
*   `float` (floating point real values)
*   `complex` (complex numbers)

All integers in Python3 are represented as long integers. Hence, there is no separate number type as "long".

### Examples

Here are some examples of numbers −


|int     |float       |complex     |
|--------|------------|------------|
|`10`    |`0.0`       |`3.14j`     |
|`100`   |`15.20`     |`45.j`      |
|`-786`  |`-21.9`     |`9.322e-36j`|
|`080`   |`32.3+e18`  |`.876j`     |
|`-0490` |`-90.`      |`-.6545+0J` |
|`-0x260`|`-32.54e100`|`3e+26J`    |
|`0x69`  |`70.2-E12`  |`4.53e-7j`  |


A complex number consists of an ordered pair of real floating-point numbers denoted by x + yj, where x and y are real numbers and j is the imaginary unit.

Python Strings
--------------

Strings in Python are identified as a contiguous set of characters represented in the quotation marks. Python allows either pair of single or double quotes. Subsets of strings can be taken using the slice operator (`[ ]` and `[:]`) with indexes starting at 0 in the beginning of the string and working their way from -1 to the end.

The plus (`+`) sign is the string concatenation operator and the asterisk (`*`) is the repetition operator. For example −

```python
str = 'Hello World!'

print(str)          # Prints complete string
print(str[0])       # Prints first character of the string
print(str[2:5])     # Prints characters starting from 3rd to 5th
print(str[2:])      # Prints string starting from 3rd character
print(str * 2)      # Prints string two times
print(str + "TEST") # Prints concatenated string
```


This will produce the following result −

```
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
```

Python Lists
------------

Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets (`[]`). To some extent, lists are similar to arrays in C. One of the differences between them is that all the items belonging to a list can be of different data type.

The values stored in a list can be accessed using the slice operator (`[ ]` and `[:]`) with indexes starting at 0 in the beginning of the list and working their way to end -1. The plus (`+`) sign is the list concatenation operator, and the asterisk (`*`) is the repetition operator. For example −

```python
lst = ['abcd', 786 , 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(lst)            # Prints complete list
print(lst[0])         # Prints first element of the list
print(lst[1:3])       # Prints elements starting from 2nd till 3rd 
print(lst[2:])        # Prints elements starting from 3rd element
print(tinylist * 2)   # Prints list two times
print(lst + tinylist) # Prints concatenated lists
```


This produces the following result −

```
['abcd', 786, 2.23, 'john', 70.200000000000003]
abcd
[786, 2.23]
[2.23, 'john', 70.200000000000003]
[123, 'john', 123, 'john']
['abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john']
```


Python Tuples
-------------

A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parenthesis.

The main difference between lists and tuples are − Lists are enclosed in brackets ( `[ ]` ) and their elements and size can be changed, while tuples are enclosed in parentheses ( `( )` ) and cannot be updated. Tuples can be thought of as **read-only** lists. For example −

```python
big_tuple = ('abcd', 786 , 2.23, 'john', 70.2 )
tiny_tuple = (123, 'john')

print(big_tuple)           # Prints complete tuple
print(big_tuple[0])        # Prints first element of the tuple
print(big_tuple[1:3])      # Prints elements starting from 2nd till 3rd 
print(big_tuple[2:])       # Prints elements starting from 3rd element
print(tiny_tuple * 2)      # Prints tuple two times
print(big_tuple + tiny_tuple)   # Prints concatenated tuple
```


This produces the following result −

```
('abcd', 786, 2.23, 'john', 70.200000000000003)
abcd
(786, 2.23)
(2.23, 'john', 70.200000000000003)
(123, 'john', 123, 'john')
('abcd', 786, 2.23, 'john', 70.200000000000003, 123, 'john')

```


The following code is invalid with tuple, because we attempted to update a tuple, which is not allowed. Similar case is possible with lists −

```python
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
tuple[2] = 1000    # Invalid syntax with tuple
list[2] = 1000     # Valid syntax with list
```


Python Dictionary
-----------------

Python's dictionaries are kind of hash-table type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. A dictionary key can be almost any Python type, but are usually numbers or strings. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces (`{ }`) and values can be assigned and accessed using square braces (`[]`). For example −

```python
my_dict = {}
my_dict['one'] = "This is one"
my_dict[2]     = "This is two"

tiny_dict = {'name': 'john','code':6734, 'dept': 'sales'}

print(my_dict['one'])       # Prints value for 'one' key
print(my_dict[2])           # Prints value for 2 key
print(tiny_dict)          # Prints complete dictionary
print(tiny_dict.keys())   # Prints all the keys
print(tiny_dict.values()) # Prints all the values
```


This produces the following result −

```
This is one
This is two
{'name': 'john', 'dept': 'sales', 'code': 6734}
dict_keys(['name', 'dept', 'code'])
dict_values(['john', 'sales', 6734])
```

Dictionaries have no concept of order among the elements. It is incorrect to say that the elements are "out of order": they are simply unordered.

Duck Typing
-----------

Duck typing in computer programming is an application of the _duck test_ -- "If it walks like a duck and it quacks like a duck, then it must be a duck". This means that you can perform operations or use methods on these objects based on their behavior, without explicitly stating or checking their types.

Let's consider these examples -
```python
# Duck typing with strings:
name = "Alice"
length = len(name) # len gets the length of a string
print(length)

# Duck typing with integers:
num1 = 10
num2 = 5
sum_result = num1 + num2
print(sum_result)
```

This produces the following output -
```
5
15
```

In these examples, we don't need to check if `name` is a string or if `num1` and `num2` are integers.  Because `name` is assigned with `""`, it will accept the `len()` method; because `num1` and `num2` are valid numbers, they will accept the `+` operation. Duck typing thus allows us to work with objects without requiring explicit type checks or conversions. Instead, we rely on the behavior of the objects and assume that they support the necessary operations or methods. If an object behaves like a string, an integer, or a list, we can treat it as such, regardless of its specific type.

# Recap
After reading this, you should have a basic understanding of:
- Creating and assigning variables
- The `del` keyword
- Working with Numbers and Strings
- A basic familiarity with Lists, Tuples, and Dictionaries
- Duck typing

# Sources
- [tutorialspoint - Variable Types](https://www.tutorialspoint.com/python3/python_variable_types.htm)