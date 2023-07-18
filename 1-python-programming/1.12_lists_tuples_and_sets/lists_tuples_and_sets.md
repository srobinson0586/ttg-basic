# Python Lists Tuples And Sets

[Back to README](README.md)

## Lists

The most basic data structure in Python is the **sequence**. Each element of a sequence is assigned a number - its position or index. The first index is zero, the second index is one, and so forth.

Python has six built-in types of sequences, but the most common ones are lists and tuples.

There are certain things you can do with all the sequence types. These operations include *indexing, slicing, adding, multiplying*, and *checking for membership*. In addition, Python has built-in functions for finding the length of a sequence and for finding its largest and smallest elements.

The list is the most versatile datatype available in Python, which can be written as a list of comma-separated values (items) between square brackets. Important thing about a list is that the items in a list need not be of the same type.

Creating a list is as simple as putting different comma-separated values between square brackets. For example −

```py
list1 = ['physics', 'chemistry', 1997, 2000];
list2 = [1, 2, 3, 4, 5 ];
list3 = ["a", "b", "c", "d"];

```

Similar to string indices, list indices start at 0, and lists can be sliced, concatenated and so on.

### Accessing Values in Lists

To access values in lists, use the square brackets for slicing along with the index or indices to obtain the value available at that index. For example:
```py
#!/usr/bin/python3

list1 = ['physics', 'chemistry', 1997, 2000]
list2 = [1, 2, 3, 4, 5, 6, 7 ]

print ("list1[0]: ", list1[0])
print ("list2[1:5]: ", list2[1:5])
```

When the above code is executed, it produces the following result:
```
list1[0]:  physics
list2[1:5]:  [2, 3, 4, 5]
```

When you use negative indeces, the index is interpreted as starting from the end to the beggining.
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
#!/usr/bin/python3

list = ['physics', 'chemistry', 1997, 2000]
print ("Value available at index 2 : ", list[2])

list[2] = 2001
print ("New value available at index 2 : ", list[2])
```

When the above code is executed, it produces the following result −

```
Value available at index 2 :  1997
New value available at index 2 :  2001
```


### Delete List Elements

To remove a list element, you can use the **`del`** statement if you know exactly which element(s) you are deleting. You can use the `remove()` method if you do not know exactly which items to delete. For example −

```py
#!/usr/bin/python3

list = ['physics', 'chemistry', 1997, 2000]
print (list)

del list[2]
print ("After deleting value at index 2 : ", list)

```

When the above code is executed, it produces the following result −
```
['physics', 'chemistry', 1997, 2000]
After deleting value at index 2 :  ['physics', 'chemistry', 2000]

```

**Note** − remove() method is discussed in subsequent section.

### Basic List Operations

Lists respond to the `+` and `*` operators much like strings; they mean concatenation and repetition here too, except that the result is a new list, not a string.

In fact, lists respond to all of the general sequence operations we used on strings in the prior chapter.


|Python Expression                         |Results                     |Description  |
|------------------------------------------|----------------------------|-------------|
| `len([1, 2, 3])`                         | 3                          |Length       |
| `[1, 2, 3] + [4, 5, 6]`                  | [1, 2, 3, 4, 5, 6]         |Concatenation|
| `['Hi!'] * 4`                            |['Hi!', 'Hi!', 'Hi!', 'Hi!']|Repetition   |
| `3 in [1, 2, 3]`                         | True                       |Membership   |
| `for x in [1,2,3] : print (x,end = ' ')` | 1 2 3                      |Iteration    |


### Indexing, Slicing and Matrixes

Since lists are sequences, indexing and slicing work the same way for lists as they do for strings.

Assuming the following input:

```py
L = ['C++', 'Java', 'Python']
```

|Python Expression   |Results           |Description                   |
|--------------------|------------------|------------------------------|
| `L[2]`             |'Python'          |Offsets start at zero         |
| `L[-2]`            |'Java'            |Negative: count from the right|
| `L[1:]`            |['Java', 'Python']|Slicing fetches sections      |


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


## Tuples

A tuple is a sequence of **immutable** Python objects. Tuples are sequences, just like lists. *The main difference between the tuples and the lists is that the tuples cannot be changed (immutable) unlike lists*. Tuples use parentheses, whereas lists use square brackets.

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
#!/usr/bin/python3

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
#!/usr/bin/python3

tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')

# Following action is not valid for tuples
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
#!/usr/bin/python3

tup = ('physics', 'chemistry', 1997, 2000);

print (tup)
del tup;
print ("After deleting tup : ")
print (tup)
```

This produces the following result:
```
('physics', 'chemistry', 1997, 2000)
After deleting tup :
Traceback (most recent call last):
   File "test.py", line 9, in <module>
      print tup;
NameError: name 'tup' is not defined
```

**Note**
> An exception is raised. This is because after `del tup`, the tuple does not exist any more.

### Basic Tuples Operations

Tuples respond to the `+` and `*` operators much like strings; they mean concatenation and repetition here too, except that the result is a new tuple, not a string.

In fact, tuples respond to all of the general sequence operations we used on strings in the previous chapter. Indexing, Slicing, Matrixes, and basic operations all work the same as they do on lists shown above.

If you would like specifics, run `help(tuple)`.

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

Sets are written with curly brackets and do not allow duplicate values for items:
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
...
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

## References
- [Tutorialspoint- Lists](https://www.tutorialspoint.com/python3/python_lists.htm)
- [Tutorialspoint- Tuples](https://www.tutorialspoint.com/python3/python_tuples.htm)
- [W3 Schools- Sets](https://www.w3schools.com/python/python_sets.asp)
- [W3 Schools- List Comprehension](https://www.w3schools.com/python/python_lists_comprehension.asp)
