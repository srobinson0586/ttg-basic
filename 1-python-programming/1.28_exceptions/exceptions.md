# Python Exceptions

A Python program terminates as soon as it encounters an error. In Python, an error can be a syntax error or an exception. In this module, you will learn what an exception is and how it differs from a syntax error. After that, you will learn about raising exceptions and making assertions. Then, you'll finish with a demonstration of the try and except block.

## Exceptions versus Syntax Errors

Syntax errors occur when the parser detects an incorrect statement. Take for example:
```py
>>> print( 0 / 0 ))
  File "<stdin>", line 1
    print( 0 / 0 ))
                  ^
SyntaxError: invalid syntax
```

The arrow indicates where the parser ran into the **syntax error**. In this example, there was one extra parenthesis. If you remove it and run the code again:
```py
>>> print( 0 / 0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: integer division or modulo by zero
```

This time, you ran into an **exception error**. This type of error occurs whenever syntactically correct Python code results in an error. The last line of the message indicated what type of exception error you ran into.

Instead of showing the message `exception error`, Python details what type of exception error was encountered. In this case, it was a `ZeroDivisionError`. Python comes with [various built-in exceptions](https://docs.python.org/3/library/exceptions.html) as well as the possibility to create self-defined exceptions.

## Raising an Exception

You can use the `raise` keyword followed by an `Exception` object to throw an exception if a condition occurs. The `Exception` object can be one of the built-in classes, or it can be a custom exception class. Below is an example:
```py
x = 10
if x > 5:
    raise Exception('x should not exceed 5. The value of x was: {}'.format(x))
```

When ran, that code outputs the following:
```py
Traceback (most recent call last):
  File "<input>", line 4, in <module>
Exception: x should not exceed 5. The value of x was: 10
```

The program comes to a halt and displays our exception to screen, offering clues about what went wrong.

## Custom Exceptions

To create a custom exception class, simply create a `Class` that inherits from an existing Exception class. The Python Docs linked above give some decent examples, but here is a simple one:
```py
class MyException(ArithmeticError):
    # all classes need a constructor
    def __init__(self, out):
        self.msg = 'My custom output: ' + out
    # tell python how to convert an instance of this class to a string
    def __str__(self):
        return self.msg

x = 3 + 5
if x == 8:
    raise MyException('I h8 the number 8')
```

Running that would output:
```
---------------------------------------------------------------------------
MyException                               Traceback (most recent call last)
Cell In[4], line 2    # (using IPython shell)
      1 if x == 8:
----> 2     raise MyException('I h8 the number 8')

MyException: My custom output: I h8 the number 8
```

Notice that the above `MyException` class inherits from the `ArithmeticError` class (this was chosen at random). So that means that it has all the attributes and methods of its parent. If we were to run `dir()` on it in an `IPython` shell we would get:
```py
In [5]: dir(MyException)
Out[5]: 
[ # bunch of dunder methods....,
    'add_note',
    'args',
    'with_traceback']
```

## The `AssertionError` Exception

Instead of waiting for a program to crash midway, you can also start by making an assertion in Python. We use the [`assert` keyword](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement) to ensure that a certain condition is met.

Have a look at the following example, where it is asserted that the code will be executed on a Linux system:
```py
import sys
assert ('linux' in sys.platform), "This code runs on Linux only."
```

If you run this code on a Linux machine, the assertion passes. If you were to run this code on a Windows machine, the outcome of the assertion would be `False` and the output would be:
```
Traceback (most recent call last):
  File "<input>", line 2, in <module>
AssertionError: This code runs on Linux only.
```

If the builtin local variable `__debug__==True`, and you can assume it always is (read more in the `assert` link above), then it evaluates the expression. In the example, `('linux' in sys.platform)` is the condition. If this condition is `True`, then the program can continue. If the condition is `False`, the program will throw an `AssertionError` exception.

In this example, throwing an `AssertionError` exception is the last thing that the program will do. The program will stop completely. What if that is not what you want?

## The `try` and `except` Blocks

The `try` and `except` block in Python is used to catch and handle exceptions. Python executes code inside the `try` block as a "normal" part of the program. The code inside the `except` block is the program's *response to any exceptions in the preceding `try` clause*.
```py
try:
    # ... do normal stuff
except:
    # handle any errors
```

As you saw earlier, when syntactically correct code runs into an error, Python will throw an exception error. This exception error will crash the program if it is unhandled. The `except` clause determines how your program responds to exceptions.

The following function can help you understand the `try` and `except` block:
```py
def linux_interaction():
    assert ('linux' in sys.platform), "Function can only run on Linux systems."
    print('Doing something.')
```

The `linux_interaction()` can only run on a Linux system. The `assert` in this function will throw an `AssertionError` exception if you call it on an operating system other than Linux.

You can give the function a `try` using the following code:
```py
try:
    linux_interaction()
except:
    pass
print("Completed program")
```

*Note:*
> You should avoid the use of a catch-all `except` as you saw above. More details below in the [Exception Catch-All](#exception-catch-all-bad) section.

The way you handled the error here is by handing out a `pass`. If you were to run this code on a Windows machine, you would get:
```
Completed program
```

The good thing here is that the program did not crash. But it would be nice to see if some type of exception occurred whenever you ran your code. To this end, you can change the `pass` into something that would generate an informative message, like so:
```py
try:
    linux_interaction()
except:
    print('Linux function was not executed')
print("Completed program")
```

Executing this code on a Windows machine:
```
Linux function was not executed
Completed program
```

When an exception occurs in a program running this function, the program will continue as well as inform you about the fact that the function call was not successful.

What you did not get to see was the *type of error that was thrown* as a result of the function call. In order to see exactly what went wrong, you would need to *catch* the error that the function threw.

### Catching Exceptions with `except` 

In python this is done wthin the `except` statement by specifying the *type* of exception you want to catch, and any nicknames you want to refer to it as in the `except` block with the `as` keyword:
```py
except <Exception_type> as <your_nickname>:
    # ...
```

The following code is an example where you capture the `AssertionError` and output that message to screen:
```py
try:
    linux_interaction()
except AssertionError as error:
    print(error)
    print('The linux_interaction() function was not executed')
```

Running this function on a Windows machine outputs the following:
```
Function can only run on Linux systems.
The linux_interaction() function was not executed
```

The first message is the `AssertionError`, informing you that the function can only be executed on a Linux machine. The second message tells you which function was not executed.

Here's another example where a *built-in exception* is caught and processed:
```py
try:
    with open('file.log') as file:
        read_data = file.read()
except:
    print('Could not open file.log')
```

If `file.log` does not exist, this block of code will output the following:
```
Could not open file.log
```

This is an informative message, and our program will still continue to run. Looking at the [Python built-in exceptions](https://docs.python.org/3/library/exceptions.html) page, we can find the error we should be catching:
> Exception `FileNotFoundError`
> 
> Raised when a file or directory is requested but doesn't exist. Corresponds to errno ENOENT.

To catch this type of exception and print it to the terminal, you could use the following code:
```py
try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
```

In this case, if `file.log` does not exist, the output would be the following:
```
[Errno 2] No such file or directory: 'file.log'
```

You can have more than one function call in your `try` clause and anticipate catching various exceptions. A thing to note here is that the code in the `try` clause will stop as soon as an exception is encountered.

#### Exception Catch-All (Bad)

If you want to catch **all exceptions**, you would simply use the `Exception` base class.

*Warning:*
> Catching `Exception` hides all errors, even those which are completely unexpected.
> This is why you should avoid bare `except` clauses in your Python programs.
> Instead, you'll want to refer to _specific exception classes_ you want to catch and handle.

#### Catching Multiple Exceptions

Look at the following code. Here, you first call the `linux_interaction()` function and then try to open a file:
```py
try:
    linux_interaction()
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError as fnf_error:
    print(fnf_error)
except AssertionError as error:
    print(error)
    print('Linux linux_interaction() function was not executed')
```

If the file does not exist, running this code on a Windows machine will output the following:
```
Function can only run on Linux systems.
Linux linux_interaction() function was not executed
```

Inside the `try` clause, the program ran into an exception immediately and did not get to the part where it attempts to open `file.log`. If you were to run that on a Linux machine you would get:
```
[Errno 2] No such file or directory: 'file.log'
```

**Here are the key takeaways**:
- A `try` clause is executed up until the point where the first exception is encountered.
- Inside the `except` clause, or the exception handler, you determine how the program responds to the exception.
- You can anticipate multiple exceptions and differentiate how the program should respond to them.

## The `else` Block

In Python, using the `else` statement, you can instruct a program to execute a certain block of code *only if there were no exceptions*.

Look at the following example:
```py
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    print('Executing the else clause.')
```

If you were to run this code on a Linux system, the output would be the following:
```
Doing something.
Executing the else clause.
```

Because the program did not run into any exceptions, the `else` block was executed. You can also have *nested* `try`/`except` blocks inside the `else` block and catch possible exceptions there as well:
```py
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
```

If you were to execute this code on a Linux machine, you would get the following result:
```
Doing something.
[Errno 2] No such file or directory: 'file.log'
```

From the output, you can see that the `linux_interaction()` function ran. Because no exceptions were encountered, an attempt to open `file.log` was made. That file did not exist, and instead of opening the file, you caught the `FileNotFoundError` exception.

## The `finally` Block

Imagine that you always had to implement some sort of action to clean up after executing your code. Python enables you to do so using the `finally` clause, which runs regardless of whether there was an exception or not.
```py
try: 
    # ... normal code

# can have `except` and/or `else` blocks

finally:
    # .... cleanup code
```

Here's a more solid example:
```py
try:
    linux_interaction()
except AssertionError as error:
    print(error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print(fnf_error)
finally:
    print('Cleaning up, irrespective of any exceptions.')
```

Running the previous code on a Windows machine would output the following:
```
Function can only run on Linux systems.
Cleaning up, irrespective of any exceptions.
```

## Summary

- `raise` allows you to throw an exception at any time.
- `assert` enables you to verify if a certain condition is met and throw an exception if it isn't.
- In the `try` clause, all statements are executed until an exception is encountered.
- `except` is used to catch and handle the exception(s) that are encountered in the `try` clause.
- `else` lets you specify code sections that should run only when **no exceptions** are encountered in the `try` clause.
- `finally` lets you specify code sections that should **always** run, with or without any previously encountered exceptions.

## Resources

- [PyDocs - `assert`](https://docs.python.org/3/reference/simple_stmts.html#the-assert-statement)
- [PyDocs - Exceptions](https://docs.python.org/3/library/exceptions.html)

## Sources

- [RealPython - Exceptions](https://realpython.com/python-exceptions/)

[Back to README](README.md)
