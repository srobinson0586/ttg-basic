# Python File I/O

[Back to README](README.md)

There are three main types of File I/O within python:
- Text I/O: expect and produce str objects to the user
- Binary I/O: expects and produces bytes-like objects (bytestrings)
- Raw I/O: used as a low-level building block for binary and text streams

## Text I/O

When you want to open a file descriptor object and interface using string objects, use _open()_ method.
```py 
myFile = open("myfile.txt", "r")
```

The second parameter defines where, and how, you will interface with the file object.

The options for interfacing are:
- "r": read, starting from the beginning of the file
- "w": write, starting at the beginning of the file.
- "a": append, starting at the end of the file
- "+": Open a file for updating. This allows you to read and write at the same time, if used in conjunction with the "r" and "w" options. 

## Binary I/O

This form is most useful when you are trying to directly handle and process bytes-like objects from a file. This means no decoding, encoding, or newline transformation is done. 

We recommend to use this if you would like some manual control over the handling of text data.

To open a file for Binary I/O, use the following implementation:
```py 
myFile = open("myfile.txt", "rb")
```

This would open a file for _reading_ data in from _myfile.txt_, starting at the beginning of the file.

If you instead wanted to open a file for binary writing, appending data at the end of the file, you could use the following:
```py 
myFile = open("myfile.txt", "ab")
```
## Raw I/O

This is typically called unbuffered I/O, and is rarely used to manipulate a raw stream from user code. 

Implement raw I/O in the following manner:
```py
myFile = open("myfile.txt", "rb", buffering=0)
```

## Reading and Writing with Files

Reading and writing to files in Python are common operations when you want to interact with file contents. Here's a brief explanation of both:

1. **Reading from Files:**
   Reading from a file involves retrieving the content stored in the file. This is useful for extracting data, processing information, and more. To read from a file:

   ```python
   with open('filename.txt', 'r') as file:
       content = file.read()  # Reads the entire file content as a string
       # Process or use 'content' as needed
   ```

2. **Writing to Files:**
   Writing to a file involves adding content to the file or creating a new file if it doesn't exist. This is useful for saving data, logs, or any kind of output. To write to a file:

   ```python
   with open('output.txt', 'w') as file:
       file.write("Hello, world!")  # Writes the given string to the file
       # You can write multiple times to add more content
   ```

Remember that `'r'` is the mode for reading, and `'w'` is the mode for writing. If the file you're opening for writing already exists, the `'w'` mode will overwrite its contents. If you want to append to an existing file without overwriting, you can use `'a'` mode.

Always make sure to close files when you're done, either by explicitly calling the `close()` method or, preferably, by using the `with` statement, which automatically manages the opening and closing of the file for you.

These are basic explanations, and there are additional options and methods available for more advanced file handling tasks in Python.

## Closing Files

Closing a file in Python refers to the process of releasing the resources associated with an open file, allowing other processes or programs to access the file. When you're done working with a file, it's important to close it to prevent resource leaks and potential issues.

You can close a file using the `close()` method of a file object. For example:

```python
file = open('example.txt', 'r')
# Perform operations on the file
file.close()  # Close the file when you're done
```

## The Context Manager

In the context of working with files, the `with` statement in Python is used to simplify the process of opening, reading, writing, or manipulating files. It ensures that the file is properly opened and automatically closed after you're done working with it, regardless of whether the code inside the `with` block completes normally or an exception is raised. This helps prevent resource leaks and ensures proper cleanup.

Here's how the `with` statement is typically used with files:

```python
with open('filename.txt', 'mode') as file:
    # Code to work with the file
    # Read, write, or manipulate the file's content
# File is automatically closed when exiting the 'with' block
```

In this context:
- `'filename.txt'` is the name of the file you want to open. You can replace this with the actual file path.
- `'mode'` specifies the mode in which you want to open the file. It can be `'r'` for reading, `'w'` for writing (creates a new file or overwrites an existing one), `'a'` for appending, and more.
- `file` is the file object that you can use within the `with` block to interact with the file's content.

Here's a practical example of reading the contents of a file using the `with` statement:

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
# File is automatically closed after this block
```

In this example, the `open()` function is used to open the file 'example.txt' in read mode. The `with` statement ensures that the file is properly closed when the code inside the block is executed.

Similarly, you can use the `with` statement for writing to files:

```python
with open('output.txt', 'w') as file:
    file.write("Hello, world!")
# File is automatically closed after this block
```

The `with` statement is particularly useful when working with files because it handles potential exceptions or errors gracefully. For instance, if an exception occurs while working with the file inside the `with` block, the file will still be closed properly, and any resources associated with the file will be released.

In summary, when used in the context of files, the `with` statement simplifies the process of opening, reading, writing, and managing files, while also ensuring that files are properly closed to prevent resource leaks and maintain code readability.

## Resources
- [Python Docs | File I/O](https://docs.python.org/3/library/io.html)
- [YouTube | File Handling in Python](https://www.youtube.com/watch?v=DmHSwTiD5Tk)

## Sources
- [TutorialsPoint | Python File I/O](https://www.tutorialspoint.com/python/python_files_io.htm)
  
[Back to README](README.md)

