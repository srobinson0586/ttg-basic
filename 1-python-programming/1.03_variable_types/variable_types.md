# Python Variable Types

[Back to README](README.md)

In programming, we use something called "variables." Variables are like named storage containers in a computer's memory. Think of them as labeled boxes that can hold different types of information, such as numbers or words. When we create a variable, we're reserving a specific area in the computer's memory to store data.

Think of it this way: Instead of remembering the exact location in memory where your data is stored, you can use a variable name to access and manipulate that data easily. This simplifies coding and makes our programs more organized and manageable.

Based on the data type of a variable, the interpreter allocates memory and decides what can be stored in the reserved memory. Therefore, by assigning different data types to the variables, you can store integers, decimals or characters in these variables.

**Note**
> Objects in memory, memory allocation, garbage collection, and object "id"s in Python are a bit advanced topics for now. However if you are interested in it, and as CNO developer you should be, there is a decent video at "[How variables work in Python](https://www.youtube.com/watch?v=0Om2gYU6clE)." If you are having trouble grasping what a variable is, the video is highly recommended.

## Assigning Values to Variables

When using the `=` operator, the operation stores the value on the right side of the `=` symbol into the variable on the left side. For example:
```python
counter = 100  # An integer assignment
miles = 1000.0 # A floating point
name = "John"  # A string

print(counter)
print(miles)
print(name)
```

Here, `100`, `1000.0` and `"John"` are the values assigned to `counter`, `miles`, and `name` variables, respectively. This produces the following result:
```
100
1000.0
John
```


## Multiple Assignment

Python allows you to assign a single value to several variables simultaneously. For example:
```python
a = b = c = 1
```

Here, an integer object is created with the value 1, and all the three variables are assigned to the same memory location. This can be confirmed with the `id()` function, which returns the memory address of the variable:
```python-repl
>>> a = b = c = 1
>>> hex(id(a))   # hex() just returns the hexadecimal representation of an integer
'0x7ffd42f6e328'
>>> hex(id(b)) 
'0x7ffd42f6e328'
>>> if id(a) == id(b) and id(b) == id(c):
...     print("Yup, They're all the same object!")
...
Yup, They're all the same object!
```

You can also assign multiple objects to multiple variables. For example:
```python-repl
>>> a, b, c = 1, 2, "john"
>>> a
1
>>> b
2
>>> c
'john'
```

Here, two integer objects with values 1 and 2 are assigned to the variables a and b respectively, and one string object with the value "john" is assigned to the variable c.

## Standard Data Types

The data stored in memory can be of many types. For example, a person's age is stored as a numeric value and his or her address is stored as alphanumeric characters. Python has various standard data types that are used to define the operations possible on them and the storage method for each of them.

There are different types of data types in Python. Some built-in Python data types are:
* **Numeric data types**: `int`, `float`, `complex`
* **Boolean type**: `bool`
* **String data types**: `str`
* **Sequence types**: `list`, `tuple`, `range`
* **Mapping data type**: `dict`
* **Binary types**: `bytes`, `bytearray`, `memoryview`
* **Set data types**: `set`, `frozenset`

## Python Numbers

Number data types store numeric values. Number objects are created when you assign a value to them. For example:

```python
var1 = 1
var2 = 10
```

You can also delete the reference to any object by using the `del` statement. The syntax of the `del` statement is:

```python
del var1[,var2[,var3[....,varN]]]
```


You can delete a single object or multiple objects by using the `del` statement. For example:
```python
del var
del var_a, var_b
```

Python supports three different numerical types −
- `int` (signed integers)
- `float` (floating point real values)
- `complex` (complex numbers)

All integers in Python3 are represented as long integers. Hence, there is no separate number type like "long". Numbers are covered more in [1.09_numbers](../1.09_numbers/numbers.md).


## Python Strings

Strings in Python are identified as a contiguous set of characters represented in quotation marks. You can use a pair of either single or double quotes. Subsets of strings can be taken using the slice operator (`[ ]` and `[:]`) with indeces starting at 0 in the beginning of the string and working their way from -1 to the end.

The plus (`+`) sign is the string concatenation operator and the asterisk (`*`) is the repetition operator. For example:
```python
string = 'Hello World!'

print(string)          # Prints complete string
print(string[0])       # Prints first character of the string
print(string[2:5])     # Prints characters starting from 3rd to 5th
print(string[2:])      # Prints string starting from 3rd character
print(string * 2)      # Prints string two times
print(string + "TEST") # Prints concatenated string
```

This will produce the following result:
```
Hello World!
H
llo
llo World!
Hello World!Hello World!
Hello World!TEST
```

Strings are covered more in [1.10_strings](../1.10_strings/strings.md).


## Python Lists

Lists are the most versatile of Python's compound data types. A list contains items separated by commas and enclosed within square brackets (`[]`). To some extent, lists are similar to arrays in C. One of the differences between them is that all the items belonging to a list can be of different data types.

The values stored in a list can be accessed using the slice operator (`[ ]` and `[:]`) with indeces starting at 0 in the beginning of the list and working their way to the end -1. The plus (`+`) sign is the list concatenation operator, and the asterisk (`*`) is the repetition operator. For example:
```python
lst = ['NCWDG', 786 , 2.23, 'john', 70.2]
tinylist = [123, 'john']

print(lst)            # Prints complete list
print(lst[0])         # Prints first element of the list
print(lst[1:3])       # Prints elements starting from 2nd till 3rd 
print(lst[2:])        # Prints elements starting from 3rd element
print(tinylist * 2)   # Prints list two times
print(lst + tinylist) # Prints concatenated lists
```

This produces the following result:
```
['NCWDG', 786, 2.23, 'john', 70.200000000000003]
NCWDG
[786, 2.23]
[2.23, 'john', 70.200000000000003]
[123, 'john', 123, 'john']
['NCWDG', 786, 2.23, 'john', 70.200000000000003, 123, 'john']
```

Lists are covered more in [1.12_lists_tuples_and_sets](../1.12_lists_tuples_and_sets/lists_tuples_and_sets.md)


## Python Tuples

A tuple is another sequence data type that is similar to the list. A tuple consists of a number of values separated by commas. Unlike lists, however, tuples are enclosed within parenthesis.

The main difference between lists and tuples are: Lists are enclosed in brackets ( `[]` ) and their elements and size can be changed, while tuples are enclosed in parentheses ( `()` ) and cannot be updated. Tuples can be thought of as **read-only** lists. For example:

```python
big_tuple = ('NCWDG', 786 , 2.23, 'john', 70.2 )
tiny_tuple = (123, 'john')

print(big_tuple)                # Prints complete tuple
print(big_tuple[0])             # Prints first element of the tuple
print(big_tuple[1:3])           # Prints elements starting from 2nd till 3rd 
print(big_tuple[2:])            # Prints elements starting from 3rd element
print(tiny_tuple * 2)           # Prints tuple two times
print(big_tuple + tiny_tuple)   # Prints concatenated tuple
```

This produces the following result:
```
('NCWDG', 786, 2.23, 'john', 70.200000000000003)
NCWDG
(786, 2.23)
(2.23, 'john', 70.200000000000003)
(123, 'john', 123, 'john')
('NCWDG', 786, 2.23, 'john', 70.200000000000003, 123, 'john')
```

The following code is invalid on the tuple, because we attempted to update a tuple, which is not allowed. However, a similar operation is valid with lists:
```python
my_tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
my_list = [ 'abcd', 786 , 2.23, 'john', 70.2  ]
my_tuple[2] = 1000    # Invalid syntax with tuple
my_list[2] = 1000     # Valid syntax with list
```

Tuples are covered more in [1.12_lists_tuples_and_sets](../1.12_lists_tuples_and_sets/lists_tuples_and_sets.md)


## Python Dictionary

Python's dictionaries are also a sequence type. They work like associative arrays or hashes found in Perl and consist of key-value pairs. Dictionary keys can be any **immutable** data type. Values, on the other hand, can be any arbitrary Python object.

Dictionaries are enclosed by curly braces (`{}`). Values can be assigned and accessed using square braces (`[]`). For example:
```python
my_dict = {}
my_dict['one'] = "This is one"
my_dict[2]     = "This is two"

tiny_dict = {'name': 'john','code':6734, 'dept': 'sales'}

print(my_dict['one'])     # Prints value for 'one' key
print(my_dict[2])         # Prints value for 2 key
print(tiny_dict)          # Prints complete dictionary
print(tiny_dict.keys())   # Prints all the keys
print(tiny_dict.values()) # Prints all the values
```

That code produces the following result when ran:
```
This is one
This is two
{'name': 'john', 'code': 6734, 'dept': 'sales',}
dict_keys(['name', 'code', 'dept'])
dict_values(['john', 6734, 'sales'])
```

**As of Python 3.7, dictionaries are ordered**, meaning that their elements will keep the same order as they are inserted into the dictionary. Before 3.7, dictionaries had no concept of order among the elements.

Dictionaries are covered more in [1.13_dictionaries](../1.13_dictionaries/dictionaries.md)


## Duck Typing

Duck typing in computer programming is an application of the _duck test_, "If it walks like a duck and it quacks like a duck, then it must be a duck". This means that you can perform operations or use methods on these objects based on their behavior, without explicitly stating or checking their types.

Let's consider these examples:
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

This produces the following output:
```
5
15
```

In these examples, we don't need to check if `name` is a string or if `num1` and `num2` are integers.  Because `name` is assigned with `""`, it will accept the `len()` method. Because `num1` and `num2` are valid numbers, they will accept the `+` operation. Duck typing thus allows us to work with objects without requiring explicit type checks or conversions.

Instead, we rely on the behavior of the objects and assume that they support the necessary operations or methods. If an object behaves like a string, an integer, or a list, we can treat it as such, regardless of its specific type.

## Mutable vs. Immutable Data Types

This module has discussed mutability vs. immutability briefly; this section will delve into that further. In Python, data types can be categorized as either **mutable** or **immutable**. Understanding this distinction is crucial for writing efficient and error-free Python code.

> NOTE: We will discuss lists, sets, and tuples in this section regarding their immutability vs. mutability. Don't worry if you don't fully understand them yet; later sections will cover them in much more depth.

### Immutable Data Types

Immutable data types, as the name suggests, are **unchangeable** once they are created. This means that any attempt to modify their values will result in the creation of a new object. The following are some common examples of immutable data types in Python:

- `int` - Integer values are immutable. If you perform an operation that changes an integer's value, a new integer object is created.
    ```py
    x = 5
    x = x + 1  # Creates a new integer object, x now holds 6
    ```
- `float` - Floating-point numbers, like integers, are immutable.
    ```py
    y = 3.14
    y = y * 2  # Creates a new float object, y now holds 6.28
    ```
- `str` - Strings are also immutable. Any operation that changes a string creates a new string object.
    ```py
    name = "Alice"
    name += " Smith"  # Creates a new string object, name now holds "Alice Smith"
    ```
- `tuple` - Tuples are ordered collections of items, and they are immutable. You cannot change the elements once a tuple is created.
    ```py
    point = (2, 3)
    # Attempting to change an element will result in an error:
    # point[0] = 1  # This will raise a TypeError
    ```

### Mutable Data Types

Mutable data types, on the other hand, **can be modified** after their creation. Any changes made to these objects do not create new objects; they modify the existing ones. Here are some common examples of mutable data types in Python:

- `list` - Lists are ordered collections of items, and they are mutable. You can add, remove, or modify elements within a list.
    ```py
    numbers = [1, 2, 3]
    numbers.append(4)  # Modifies the existing list by adding 4
    numbers[0] = 5     # Modifies the first element to be 5
    ```
- `dict` - Dictionaries are mutable mappings of keys to values. You can add, remove, or change key-value pairs within a dictionary.
    ```py
    person = {"name": "Bob", "age": 30}
    person["age"] = 31  # Modifies the age value to 31
    ```
- `set` - Sets are unordered collections of unique elements, and they are mutable. You can add and remove elements from a set.
    ```py
    colors = {"red", "green", "blue"}
    colors.add("yellow")  # Adds "yellow" to the existing set
    colors.remove("red")  # Removes "red" from the set
    ```
- Most other objects in Python are also immutable.

Understanding whether a data type is mutable or immutable is essential for effective Python programming. It can help you avoid unexpected side effects when passing data between functions and ensure that your code behaves as intended.

Remember that when working with immutable data types, any operation that appears to modify the data will create a new object. In contrast, with mutable data types, modifications are made in place, affecting the original object. Choose the appropriate data type based on your specific programming needs.

## Resources
- [YouTube | How variables work in Python](https://www.youtube.com/watch?v=0Om2gYU6clE)
- [RealPython | Mutable vs. Immutable Types](https://realpython.com/python-mutable-vs-immutable-types/)

## Sources

- [TutorialsPoint | Python Variable Types](https://www.tutorialspoint.com/python3/python_variable_types.htm)

[Back to README](README.md)
