# Python Basic Syntax


## First Python Program

In this section we will execute some python code in different modes.

### Interactive Mode Programming (REPL)

Invoking the interpreter without passing a script file as a parameter brings up the following prompt:
```bash
$ python

Python 3.3.2 (default, Dec 10 2013, 11:35:01)
[GCC 4.6.3] on Linux
Type "help", "copyright", "credits", or "license" for more information.
>>>

On Windows:

Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:43:06) [MSC v.1600 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>>
```

Type the following text at the Python prompt and press Enter −

```py
>>> print("Hello, Python!")
```


### Script Mode Programming

Invoking the interpreter with a script parameter begins execution of the script and continues until the script is finished. When the script is finished, the interpreter is no longer active.

Let us write a simple Python program in a script. Python files have the extension **`.py`**. Type the following source code in a **`test.py`** file:
```python
print("Hello, this is scripted Python!")
```

Now, run the program as follows:
```bash
$ python test.py 
```

This produces the following result:
```
Hello, this is scripted Python!
```

There is another way to execute a Python script in Unix systems, by using a shebang (`#!`). Shebangs are a way to tell the BASH shell (your "terminal") what program it should use to run the file. By adding the below bash comment, you are telling BASH to use the executable at `/usr/bin/python3` to run the proceding code:
```py
#!/usr/bin/python3
print("Hello, this is scripted Python!")
```
However, if you now attempted to run it with `./test.py`, you would likely get a permission denied error. This is because you haven't made the file **executable**. In order to give it execute permission, use the linux `chmod` command first.
```bash
$ chmod +x test.py     # This is to make the file executable
$./test.py
```

This produces the following result:
```
Hello, this is scripted Python!
```

For more on Shebangs, specifically in the context of running python scripts, check out [Python: What is Shebang](https://www.youtube.com/watch?v=zani1BGrSAM).


## Python Identifiers

A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter or an underscore (`[A-Z, a-z, _]`) followed by zero or more alphanumeric characters, underscores, or hyphens (`[A-Z, a-z, _, -, 0-9]`).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, `Manpower` and `manpower` are two different identifiers in Python.

The following are some naming conventions for Python identifiers:
- Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
   - e.g. `My_Class`
- Starting an identifier with a single leading underscore indicates that the identifier is private. *Private* basically means that people unfamiliar with the code shouldn't mess with the identifier because it could break the program.
   - e.g. `_my_private_var`
- Starting an identifier with two leading underscores indicates a strong private identifier.
   - e.g. `__seriously_dont_touch_or_you_will_break_functionality`
- If the identifier also ends with two trailing underscores, the identifier is a language-defined special name. In Python, these are called [Dunder Methods and Variables](https://mathspp.com/blog/pydonts/dunder-methods).
   - e.g. `__main__` is an actual way to identify the main function in a Python program

Often times when you are creating identifiers, you want to be very descriptive and use two different words while keeping it readable. For example, if you want a variable that keeps track of the maximum value, you might want to use a combination of "maximum" and "value" for its name. There are several different kinds of ways to do this in programming, and it differs between languages. Some naming conventions are:

- `camelCase`
   - The first word is lowercase while each new word is capitalized (C uses this convention)
- `PascalCase`
   - All words are capitalized
- `snake_case`
   - All words are lowercase and separated by an underscore

[Python convention](https://peps.python.org/pep-0008/#function-and-variable-names) dictates that function and variable names should use `snake_case` while Classes (covered in [1.21_classes_and_objects](../1.21_classes_and_objects/classes_and_objects.md)) should be `PascalCase`.

Using our max value example from earlier, we would name the variable something like `max_val`. Naming conventions are *extremely important* to be followed, as the code still works fine. But if you want to look like you know what you're doing, you should follow them.
    

## Reserved Words

The following list shows the Python keywords. These are reserved words and you cannot use them as constants or variables or any other identifier names. If you *do use them*, you **will** break essential python functionality. All the Python keywords contain lowercase letters only.

- `and`
- `exec`
- `not`
- `as`
- `finally`
- `or`
- `assert`
- `for`
- `pass`
- `break`
- `from`
- `print`
- `class`
- `global`
- `raise`
- `continue`
- `if`
- `return`
- `def`
- `import`
- `try`
- `del`
- `in`
- `while`
- `elif`
- `is`
- `with` 
- `else`
- `lambda`
- `yield`
- `except`


## Lines and Indentation

Python does not use braces(`{}`) to indicate blocks of code for class and function definitions or control flow. Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example:
```python
if True:
   print("True")
else:
   print("False")
```

However, the following block generates an error −
```python
if True:
   print ("Answer")
      print ("True")  # BAD SYNTAX!
else:
   print ("Answer") 
      print ("False")  # BAD SYNTAX!
```

Thus, in Python all the continuous lines indented with the same number of spaces would form a block. The following example has various statement blocks:

**Note**
> Do not try to understand the logic at this point of time. Just make sure you see the relationship between indentation and how it affects execution.

```python
#!/usr/bin/python3
import sys

file_finish = "end"
file_text = ""
contents = []

file_name = input("Enter filename: ")
if len(file_name) == 0:
   print("Please enter filename")
   sys.exit()

try:
   # open file stream
   file = open(file_name, "w")

except IOError:
   print("There was an error writing to", file_name)
   sys.exit()

print("Enter '", file_finish,)
print("' When finished")

while file_text != file_finish:
   file_text = input("Enter text: ")
   contents.append(file_text)

   if file_text == file_finish:
      # close the file
      file.close()
      break

print(contents)
```


## Multi-Line Statements

Statements in Python typically end with a new line. Python, however, allows the use of the line continuation character (`\`) to denote that the line should continue. For example:
```py
total = item_one + \
   item_two + \
   item_three
```

The statements contained within the `[]`, `{}`, or `()` enclosers do not need to use the line continuation character. For example:
```python
days = ['Monday', 'Tuesday', 
   'Wednesday', 
   'Thursday', 'Friday']
```


## Quotation in Python

Python accepts single (`'`), double (`"`) and triple (`'''` or `"""`) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all the following are legal:
```python
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines 
and sentences."""
```


## Comments in Python

A hash sign (`#`) that is not inside a string literal is the beginning of a comment. All characters after the `#`, up to the end of the physical line, are part of the comment and the Python interpreter ignores them.

```python
# First comment
print("Hello, Python!") # second comment
```

This produces the following result:
```
Hello, Python!
```

Python does not have a multiple-line commenting feature. You have to comment each line individually as follows:
```python
# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.
```

You could technically use triple-quotes to get around this but it isn't good practice. Only use Multi-line strings when writing things like [Python Docstrings](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings).


## Using Blank Lines

A line containing only whitespace, possibly with a comment, is known as a blank line and Python totally ignores it.

In an interactive interpreter session, you must enter an empty physical line to terminate a multiline statement (like a function definition).
```py
>>> def my_func(): 
...     print("Hello")
... 
>>> 
```

## Waiting for the User

The following program displays the prompt “Press the enter key to exit”. Then it waits for the user to input something using the keyboard. For more on the `input()` function, run `help(input)` in the python shell.
```python
input("\n\nPress the enter key to exit.")
```

Here, "`\n\n`" is used to create two new lines before displaying the actual line. Once the user presses the key, the program ends. This is a nice trick to keep a console window open until the user is done with an application.

## Multiple Statements on a Single Line

The semicolon ( `;` ) allows multiple statements on a single line given that no statement starts a new code block. Here is a sample snip using the semicolon:
```python
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```


## Command Line Arguments

Many programs can be run to provide you with some basic information about how they should be run. Python enables you to do this with `-h`:
```bash
$ python -h
usage: python [option] ... [-c cmd | -m mod | file | -] [arg] ...
Options and arguments (and corresponding environment variables):
-c cmd : program passed in as string (terminates option list)
-d     : debug output from parser (also PYTHONDEBUG=x)
-E     : ignore environment variables (such as PYTHONPATH)
-h     : print this help message and exit

[ etc. ]
```

You can also program your script in such a way that it should accept various command line options from the user. [Command Line Arguments](https://www.tutorialspoint.com/python3/python_command_line_arguments.htm) is an advanced topic that isn't covered here.


## Resources

- [Dunder Methods and Variables](https://mathspp.com/blog/pydonts/dunder-methods)
- [Python: What is Shebang](https://www.youtube.com/watch?v=zani1BGrSAM)
- [Command Line Arguments](https://www.tutorialspoint.com/python3/python_command_line_arguments.htm)
- [Python Naming Convention](https://peps.python.org/pep-0008/#function-and-variable-names)
- [Python Docstrings](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings)

## Sources

- [Tutorialspoint - Basic Syntax](https://www.tutorialspoint.com/python3/python_basic_syntax.htm)

[Back to README](README.md)
