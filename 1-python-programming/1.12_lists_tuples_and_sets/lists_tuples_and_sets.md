# Python Lists Tuples And Sets


## Lists

The most basic *data structure* in Python is the **sequence**. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.

Python has six built-in types of sequences, but the most common ones are lists and tuples.

There are certain things you can do with all the sequence types. These operations include *indexing, slicing, adding, multiplying*, and *checking for membership*. In addition, Python has built-in functions for finding the length of a sequence and for finding its largest and smallest elements.

The list is the most versatile datatype available in Python, which can be written as a list of comma-separated values (items) between square brackets. An important thing about a list is that the items in a list need not be of the same type.

For more information, check out [Python Docs- Lists](https://docs.python.org/3/library/stdtypes.html#lists). 

Creating a list is as simple as putting different comma-separated values between square brackets. For example:

```py
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];
```

Similar to string indices, list indices start at 0, and lists can be sliced, concatenated and so on.

### Accessing Values in Lists

To access values in lists, use the square brackets for slicing along with the index or indices to obtain the value available at that index. For example:
```py
list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7]

print ("list1[0]:", list1[0])
print ("list2[1:5]:", list2[1:5])
```

When the above code is executed, it produces the following result:
```
list1[0]: physics
list2[1:5]: [2, 3, 4, 5]
```

### List Slicing

Since lists are sequences, indexing and slicing work the same way for lists as they do for strings. In Python, list slicing is a technique used to extract a portion of a list. It allows you to create a new list containing elements from the original list based on specified `start`, `stop`, and `step` values. The general syntax for list slicing is:
```
new_list = original_list[start:stop:step]
```

Where:
- `start`: The index of the element where the slice starts (inclusive). If omitted, it starts from the beginning of the list (index 0).
- `stop`: The index of the element where the slice ends (exclusive). If omitted, it goes till the end of the list.
- `step`: The number of steps to take between elements in the slice. If omitted, it defaults to 1, which means consecutive elements are included in the slice.
Here are some examples to illustrate list slicing:
```py
# (in the interpreter)
>>> my_list = ['C++', 'Java', 'Python', 'NCWDG', 'TG-5', 0xdeadbeef]
>>> print(my_list[0]) # Indexing (first element at index 0)
C++
>>> print(my_list[2]) # Indexing 
Python
>>> print(my_list[2:]) # Forward slicing - doesn't specify stop/step
['Python', 'NCWDG', 'TG-5', 3735928559]
>>> print(my_list[:2]) # Backward slicing - doesn't specify start/step, only stop
['C++', 'Java']

# Negative indexing starts counting from the right
>>> print(my_list[-2])
TG-5
>>> print(my_list[-2:5]) # Start @ 2nd-to-last, Stop before the 6th element
['TG-5']
>>> print(my_list[-2:])  # Start @ 2nd-to-last, No stop/step
['TG-5', 3735928559]

# Steps dictate by how much the iterator moves at a time
>>> print(my_list[2::1]) # Step 1 at a time (default)
['Python', 'NCWDG', 'TG-5', 3735928559]
>>> print(my_list[2::2]) # Step 2 at a time
['Python', 'TG-5']

# You can create new lists with slicing
>>> cool_list = my_list[3:] # Don't take the first 3 elements of my_list
>>> print(cool_list)
['NCWDG', 'TG-5', 3735928559]

# You can easily reverse lists with a -1 step
>>> reverse_list = my_list[::-1] # New list from the reverse of the my_list 
>>> print(reverse_list)
[3735928559, 'TG-5', 'NCWDG', 'Python', 'Java', 'C++']
```

Keep in mind that list slicing creates a new list with the specified elements, and it does not modify the original list. If you modify the new list, it won't affect the original list and vice versa.

Just to expound on it, when you use negative indeces, the index is interpreted as starting from the end and moving towards the beginning.
```py
>>> a = [1, 2, 3, 4, 5, 6, 7]
>>> a[-2]
6
>>> a[-2:6]
[6]
>>> a[-2:]
[6, 7]
```

### Updating Lists

You can update single or multiple elements of lists by giving the slice on the left-hand side of the assignment operator, and you can add to elements in a list with the `append()` method. For example:

```py
my_list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2:", my_list[2])

my_list[2] = 2001  # here we tell the python interpreter to update the [2] slice of my_list
print ("New value available at index 2:", my_list[2])

my_list[1:3] = [1337, 'Cyb3r 0p5'] # update slice [1:3] with the new list value
print("New list is:", my_list)

my_list.append(0xdeadbeef) # append adds to the end of the list
print("New list is:", my_list)
```

When the above code is executed, it produces the following result:

```
Value available at index 2: 1997
New value available at index 2: 2001
New list is: ['physics', 1337, 'Cyb3r 0p5', 2000]
New list is: ['physics', 1337, 'Cyb3r 0p5', 2000, 3735928559]
```


### Delete List Elements

To remove a list element, you can use the **`del`** statement, or the `list.pop()` method if you know exactly which element(s) you are deleting. You can use the `remove()` method if you do not know exactly which items to delete. For example −

```py
my_list = ['physics', 'chemistry', 1997, 2000, 2000]
print (my_list)

del my_list[2]
print ("After deleting value at index 2:", my_list)

my_list.remove(2000)                                 
print("After the remove() operation:", my_list)

my_phys = my_list.pop(0)
print(my_phys)
print("After the pop() operation:", my_list)
```

When the above code is executed, it produces the following result −
```
['physics', 'chemistry', 1997, 2000, 2000]
After deleting value at index 2: ['physics', 'chemistry', 2000, 2000]
After the remove() operation: ['physics', 'chemistry', 1997, 2000]
physics
After the pop() operation: ['chemistry', 2000]
```

As seen above, `pop()` is a *method* of the `list` class so it is called with the `.` operator on the `my_list` variable. `del` is a python keyword, so you don't need to use the `.` operator, and you pass the target object to delete as opposed to its index in `my_list`. 

Keep in mind that you don't *have to use* the return value from `list.pop()`, but the function will always return a value. So keep in mind the extra overhead for `pop()` and only use it if you need the returned value.


### Basic List Operations

Lists respond to the `+` and `*` operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string.

In fact, lists respond to all of the general basic operations that can be used on strings.


|Python Expression                         |Results                     |Description  |
|------------------------------------------|----------------------------|-------------|
| `len([1, 2, 3])`                         | 3                          |Length       |
| `[1, 2, 3] + [4, 5, 6]`                  | [1, 2, 3, 4, 5, 6]         |Concatenation|
| `['Hi!'] * 4`                            |['Hi!', 'Hi!', 'Hi!', 'Hi!']|Repetition   |
| `3 in [1, 2, 3]`                         | True                       |Membership   |
| `for x in [1,2,3] : print (x,end = ' ')` | 1 2 3                      |Iteration    |

### Built-in List Functions and Methods

Python includes the following list functions:

|Sr.No.|Function & Description                             |
|------|---------------------------------------------------|
|1     |`len(list)`: Gives the total length of the list.       |
|2     |`max(list)`: Returns item from the list with max value.|
|3     |`min(list)`: Returns item from the list with min value.|
|4     |`list(seq)`: Converts a tuple into list.               |


Python includes the following list methods:

|Sr.No.|Methods & Description                                                   |
|------|------------------------------------------------------------------------|
|1     |`list.append(obj)`: Appends object obj to list                              |
|2     |`list.count(obj)`: Returns count of how many times obj occurs in list       |
|3     |`list.extend(seq)`: Appends the contents of seq to list                     |
|4     |`list.index(obj)`: Returns the lowest index in list that obj appears        |
|5     |`list.insert(index, obj)`: Inserts object obj into list at offset index     |
|6     |`list.pop(obj = list[-1])`: Removes and returns last object or obj from list|
|7     |`list.remove(obj)`: Removes object obj from list                            |
|8     |`list.reverse()`: Reverses objects of list in place                         |
|9     |`list.sort([func])`: Sorts objects of list, use compare func if given       |

**Note**
> You can see all this and more by running `help(list)`. If you just want a brief list of `list` class members and methods, run `dir(list)`

### List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list. It allows you to execute for loops and conditionals in a single line. Take for example:
```py
nums = [1, 2, 3, 4, 5, 6, 7]
newlist = []

for x in nums:
  if x %2 == 0:
    newlist.append(x * 74)

print(newlist)
# [148, 296, 444]
```

You can do all that in 2 lines!
```py
nums = [1, 2, 3, 4, 5, 6, 7]     
newlist = [x*74 for x in nums if (x % 2 == 0)]
```

List comprehension syntax is:

> newlist = [*expression* for *item* in *iterable* if *condition* == True]

- Condition
    - A filter than only acccepts the items that evaluate to `True`
    - Above, it was: `x % 2 == 0`
- Iterable
    - Any iterable python object list `list`, `tuple`, `set`, etc
    - Above, it was: `nums`
- Item
    - The current item in the iteration
    - Above, it was: `x`
- Expression
    - The statements you would like done to the *item* before it ends up as a list item in the new list
    - Above, it was: `x * 74`

If you are still having trouble understanding List Comprehension, I recommend checking out this [Python Tutorial on List Comprehension](https://youtu.be/3dt4OGnU5sM).

## Tuples

A tuple is a sequence of **immutable** Python objects. Tuples can be used much like lists. *The main difference between the tuples and the lists is that the tuples cannot be changed (immutable) unlike lists*. Tuples use parentheses `()`, whereas lists use square brackets `[]`.

For more information, check out [Python Docs- Tuples](https://docs.python.org/3/library/stdtypes.html#tuples).

Creating a tuple is as simple as putting different comma-separated values. Optionally, you can put these comma-separated values between parentheses also. For example:

```py
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5 )
tup3 = "a", "b", "c", "d"
```

The empty tuple is written as two parentheses containing nothing:
```py
tup1 = ();
```

To write a tuple containing a single value you have to include a comma, even though there is only one value −
```py
tup1 = (50,)
```

Like string indices, tuple indices start at 0, and they can be sliced, concatenated, and so on.

### Accessing Values in Tuples

To access values in tuples, use the square brackets for *slicing* along with the index or indices to obtain the value available at that index. For example:
```py
tup1 = ('physics', 'chemistry', 1997, 2000)
tup2 = (1, 2, 3, 4, 5, 6, 7 )

print ("tup1[0]: ", tup1[0])
print ("tup2[1:5]: ", tup2[1:5])
```

When the above code is executed, it produces the following result:
```py
tup1[0]:  physics
tup2[1:5]:  (2, 3, 4, 5)
```

### Updating Tuples

Tuples are immutable, which means you cannot update or change the values of tuple elements. You are able to take portions of the existing tuples to create new tuples as the following example demonstrates:

```py
tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following is not valid for tuples
# tup1[0] = 100;

# So let's create a new tuple as follows
tup3 = tup1 + tup2
print (tup3)
```

When the above code is executed, it produces the following result:
```
(12, 34.56, 'abc', 'xyz')
```


### Delete Tuple Elements

Removing individual tuple elements is not possible. There is, of course, nothing wrong with putting together another tuple with the undesired elements discarded.

To explicitly remove an entire tuple, just use the **del** statement. For example:
```py
tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
del tup;
print ("After deleting tup:")
print (tup)
```

This produces the following result:
```
('physics', 'chemistry', 1997, 2000)
After deleting tup:
Traceback (most recent call last):
   File "test.py", line 9, in <module>
      print tup;
NameError: name 'tup' is not defined
```

**Note**
> An exception is raised. This is because after `del tup`, the tuple does not exist any more.

### Basic Tuples Operations

Tuples respond to the `+` and `*` operators much like lists; they mean concatenation and repetition here too, except that the result is a new tuple, not a list. Indexing, Slicing, Matrixes, and basic operations all work the same as they do on lists as shown above.

If you would like specifics, run `help(tuple)`.

### Tuple Unpacking

Basically the most important use case for a tuple is when you want to be able to group together a bunch of variables without creating an entire Class for them. This is often the case for return values from functions (covered in [1.15_functions](../1.15_functions/functions.md)).
```py
>>> def get_coordinates( ship ): 
...     if ship == 'CVN-69':
...             return (132.3, 201)
...     elif ship == 'CVN-73':
...             return (124.4, 021.3)
...     elif ship == 'CVN-70':
...             return (19, 234.2)
...
>>> vinson_x, vinson_y = get_coordinates('CVN-70')  # tuple unpacking
>>> vinson_x
19
>>> vinson_y
234.2
>>> eisenhower_x, _ = get_coordinates('CVN-69')     # if you don't want one of them, use an _
>>> eisenhower_x
132.3
>>> washington_x = get_coordinates('CVN-73')        # insufficient l-values, gets set as a tuple
>>> washington_x
(124.4, 21.3)
```

As seen above, usually tuple unpacking is done by specifying an amount of variables equal to the size of the expected return tuple.

If you don't want to use one of them, you can specify an empty slot with `_` as seen in example 2. 

If you don't use the same amount of variables as the function's return size, one of the variables will be set to a tuple as seen in example 3 above.

### Built-in Tuple Functions


Python includes the following tuple functions:  

|Sr.No.|Function & Description                               |
|------|-----------------------------------------------------|
|1     |`cmp(tuple1, tuple2)`: Compares elements of both tuples. |
|1     |`len(tuple)`: Gives the total length of the tuple.       |
|2     |`max(tuple)`: Returns item from the tuple with max value.|
|3     |`min(tuple)`: Returns item from the tuple with min value.|
|4     |`tuple(seq)`: Converts a list into tuple.                |


## Sets

A set is a collections, or sequence, much like lists and tuples except that sets:
- Are **unordered**
    - Items in a set do not have a defined order.
    - Can appear in a different order every time you use them
- Are **unchangeable**
    - Set *items* themselves are unchangeable but you can remove and add items
- Are **unindexed**
    - Cannot be referred to by index or key

For more, reference the [Python Docs- Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset) page.

Sets are written with curly brackets `{}` and do not allow duplicate values for items:
```py
>>> thisset = {"apple", "banana", "cherry", "apple"}
>>> print(thisset)
{'cherry', 'banana', 'apple'}
```

### Set Items

Set items can be of any data type, and a set can contain different data types:
```py
>>> set1 = {"apple", "banana", "cherry"}
>>> set2 = {1, 5, 7, 9, 3}
>>> set3 = {True, False,"abc", 34, True, 40, "male"}
>>> set3
{False, True, 34, 40, 'abc', 'male'}
```

### Accessing Items

Set can't be referred to by index or key:
```py
>>> set3
{False, True, 34, 40, 'abc', 'male'}
>>> set3[3]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'set' object is not subscriptable
```

*However*, you can loop through the set items using a `for` loop, or ask if a specified value is present in a set, by using the `in` keyword:
```py
>>> thisset = {"apple", "banana", "cherry"}
>>> for x in thisset:
...   print(x, end=',') # instead of a newline each time, put a comma

cherry,banana,apple,
>>> print("banana" in thisset)
True
```

### Adding & Removing Items

You can add items, to a set using its `add()` method. You can use the `update()` method to add items from another set or *any iterable like tuples, lists, etc*.
```py
>>> thisset = {"apple", "banana", "cherry"}
>>> thisset.add("orange")
>>> thisset
{'orange', 'apple', 'cherry', 'banana'}

>>> tropical = {"pineapple", "mango", "papaya"}
>>> thisset.update(tropical)
>>> thisset
{'pineapple', 'orange', 'cherry', 'mango', 'papaya', 'apple', 'banana'}

>>> mylist = ['orange', 'mango', 8, 9]
>>> thisset.update(mylist)
>>> thisset
{8, 9, 'pineapple', 'orange', 'cherry', 'mango', 'papaya', 'banana', 'apple'}
```

Notice how `thisset` didn't duplicate any values that were present both in itself and `mylist`. This ability to maintain *unique* items can be useful in situations like maintaining password lists for bruteforcing.

## Resources
- [Python- List Comprehensions](https://youtu.be/3dt4OGnU5sM).
- [W3 Schools- List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
- [Python Docs- Lists](https://docs.python.org/3/library/stdtypes.html#lists)
- [Python Docs- Sets](https://docs.python.org/3/library/stdtypes.html#set-types-set-frozenset)
- [Python Docs- Tuples](https://docs.python.org/3/library/stdtypes.html#tuples)

## Sources
- [Tutorialspoint- Lists](https://www.tutorialspoint.com/python3/python_lists.htm)
- [Tutorialspoint- Tuples](https://www.tutorialspoint.com/python3/python_tuples.htm)
- [W3 Schools- Sets](https://www.w3schools.com/python/python_sets.asp)

[Back to README](README.md)