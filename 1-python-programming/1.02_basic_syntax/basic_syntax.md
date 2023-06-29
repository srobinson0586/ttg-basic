# Python Basic Syntax

[Back to README](README.md)

First Python Program
--------------------

Let us execute the programs in different modes of programming.

### Interactive Mode Programming

Invoking the interpreter without passing a script file as a parameter brings up the following prompt −

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

```python
>>> print("Hello, Python!")
```


### Script Mode Programming

Invoking the interpreter with a script parameter begins execution of the script and continues until the script is finished. When the script is finished, the interpreter is no longer active.

Let us write a simple Python program in a script. Python files have the extension **.py**. Type the following source code in a test.py file −

[Live Demo](http://tpcg.io/GBhBAj)

```python
print("Hello, Python!")
```


We assume that you have the Python interpreter set in **PATH** variable. Now, try to run this program as follows −

**On Linux**

```bash
$ python test.py 
```


This produces the following result −

```
Hello, Python!
```


**On Windows**

```
C:\Python34>Python test.py
```


This produces the following result −

```
Hello, Python!
```


Let us try another way to execute a Python script in Linux. Here is the modified test.py file −

[Live Demo](http://tpcg.io/LheT18)

```python
#!/usr/bin/python3
print("Hello, Python!")
```


We assume that you have Python interpreter available in the /usr/bin directory. Now, try to run this program as follows −

```bash
$ chmod +x test.py     # This is to make file executable
$./test.py
```


This produces the following result −

```
Hello, Python!
```


Python Identifiers
------------------

A Python identifier is a name used to identify a variable, function, class, module or other object. An identifier starts with a letter A to Z or a to z or an underscore (\_) followed by zero or more letters, underscores and digits (0 to 9).

Python does not allow punctuation characters such as @, $, and % within identifiers. Python is a case sensitive programming language. Thus, **Manpower** and **manpower** are two different identifiers in Python.

Here are naming conventions for Python identifiers −

*   Class names start with an uppercase letter. All other identifiers start with a lowercase letter.
*   Starting an identifier with a single leading underscore indicates that the identifier is private.
*   Starting an identifier with two leading underscores indicates a strong private identifier.
*   If the identifier also ends with two trailing underscores, the identifier is a language-defined special name.
    

Reserved Words
--------------

The following list shows the Python keywords. These are reserved words and you cannot use them as constants or variables or any other identifier names. All the Python keywords contain lowercase letters only.


|and     |exec   |not   |
|--------|-------|------|
|as      |finally|or    |
|assert  |for    |pass  |
|break   |from   |print |
|class   |global |raise |
|continue|if     |return|
|def     |import |try   |
|del     |in     |while |
|elif    |is     |with  |
|else    |lambda |yield |
|except  |       |      |


Lines and Indentation
---------------------

Python does not use braces({}) to indicate blocks of code for class and function definitions or flow control. Blocks of code are denoted by line indentation, which is rigidly enforced.

The number of spaces in the indentation is variable, but all statements within the block must be indented the same amount. For example −

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
   print ("True")
else:
   print "(Answer") # BAD SYNTAX!
   print ("False")
```


Thus, in Python all the continuous lines indented with the same number of spaces would form a block. The following example has various statement blocks −

**Note** − Do not try to understand the logic at this point of time. Just make sure you understood the various blocks even if they are without braces.

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
data = ' '.join([str(elem) for elem in contents])  
print(data)
file.write(data)
file.close()
file_name = input("Enter filename: ")

if len(file_name) == 0:
   print("Next time please enter something")
   sys.exit()

try:
   file = open(file_name, "r")

except IOError:
   print("There was an error reading file")
   sys.exit()
file_text = file.read()
file.close()
print(file_text)
```


Multi-Line Statements
---------------------

Statements in Python typically end with a new line. Python, however, allows the use of the line continuation character (\\) to denote that the line should continue. For example −

```python
total = item_one + \
   item_two + \
   item_three
```


The statements contained within the \[\], {}, or () brackets do not need to use the line continuation character. For example −

```python
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
```


Quotation in Python
-------------------

Python accepts single ('), double (") and triple (''' or """) quotes to denote string literals, as long as the same type of quote starts and ends the string.

The triple quotes are used to span the string across multiple lines. For example, all the following are legal −

```python
word = 'word'
sentence = "This is a sentence."
paragraph = """This is a paragraph. It is
made up of multiple lines and sentences."""
```


Comments in Python
------------------

A hash sign (#) that is not inside a string literal is the beginning of a comment. All characters after the #, up to the end of the physical line, are part of the comment and the Python interpreter ignores them.

[Live Demo](http://tpcg.io/e9zmst)

```python
#!/usr/bin/python3

# First comment
print("Hello, Python!") # second comment
```


This produces the following result −

```
Hello, Python!
```


You can type a comment on the same line after a statement or expression −

```python
name = "Madisetti" # This is again comment
```


Python does not have multiple-line commenting feature. You have to comment each line individually as follows −

```python
# This is a comment.
# This is a comment, too.
# This is a comment, too.
# I said that already.
```


Using Blank Lines
-----------------

A line containing only whitespace, possibly with a comment, is known as a blank line and Python totally ignores it.

In an interactive interpreter session, you must enter an empty physical line to terminate a multiline statement.

Waiting for the User
--------------------

The following line of the program displays the prompt and, the statement saying “Press the enter key to exit”, and then waits for the user to take action −

```python
#!/usr/bin/python3

input("\n\nPress the enter key to exit.")
```


Here, "\\n\\n" is used to create two new lines before displaying the actual line. Once the user presses the key, the program ends. This is a nice trick to keep a console window open until the user is done with an application.

Multiple Statements on a Single Line
------------------------------------

The semicolon ( ; ) allows multiple statements on a single line given that no statement starts a new code block. Here is a sample snip using the semicolon −

```python
import sys; x = 'foo'; sys.stdout.write(x + '\n')
```


Multiple Statement Groups as Suites
-----------------------------------

Groups of individual statements, which make a single code block are called **suites** in Python. Compound or complex statements, such as if, while, def, and class require a header line and a suite.

Header lines begin the statement (with the keyword) and terminate with a colon ( : ) and are followed by one or more lines which make up the suite. For example −

```python
if expression: 
   suite
elif expression: 
   suite 
else: 
   suite
```


Command Line Arguments
----------------------

Many programs can be run to provide you with some basic information about how they should be run. Python enables you to do this with -**h** −

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

You can also program your script in such a way that it should accept various options. [Command Line Arguments](https://www.tutorialspoint.com/python3/python_command_line_arguments.htm) is an advanced topic. Let us understand it.

# Summary
After reading this, you should have a basic understanding of:
- Print statements using `print()`
- Getting input from the user using `input()`
- Comments
- Reserved words
- Spacing and indenting

# Sources
- [tutorialspoint - Basic Syntax](https://www.tutorialspoint.com/python3/python_basic_syntax.htm)