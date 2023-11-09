# Python Functions


A function is a block of organized, reusable code that is used to perform a single, related action. Functions provide better modularity for your application and a high degree of code reuse.

As you already know, Python gives you many built-in functions like `print()`, etc. but you can also create your own functions. These functions are called *user-defined functions.*

## Defining a Function

You can *define* functions to provide the required functionality and tell the interpreter what to do. Here are simple rules to define a function in Python.

-   Function blocks begin with the keyword `def` followed by the function name and parentheses `()` .
    
-   Any input parameters or arguments should be placed within these parentheses. You can also define *parameters* inside these parentheses.
    
-   The first statement of a function can be an optional statement - the documentation string of the function or *docstring*.
    - We will provide basic docstrings in our training functions, but you will eventually be expected to provide robust docstrings for your software.
    - Reference this [RealPython Article](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings) if you would like to learn more.
    
-   The code block within every function starts with a colon (`:`) and is indented.
    - If you forgot about how python uses indentation to separate code blocks, please refer back to [1.02_basic_syntax/basic_syntax.md](../1.02_basic_syntax/basic_syntax.md#lines-and-indentation)
    
-   The statement `return <expression>` exits a function, optionally passing back an expression, or value, to the caller. A return statement with no arguments is the same as `return None`.  If there is no `return` in the function, the function will execute normally and return `None`.
    

### Syntax

The below pseudocode shows the basic syntax of a function. The code within isn't valid python.
```py
def functionname(parameters):
   """function_docstring, explain what the function does and what the parameters are used for"""
   do_code_here
   return expression_optional
```

### Example

The following function takes a string as the input parameter and prints it to the standard output device (usually just the terminal you're running the program from). It doesn't return anything. In fact, the final `return` statement is optional here since we aren't returning anything.
```py
def printme(my_str):
   "This prints a passed string into this function"
   print(my_str)
```


### The `return` Statement

The statement `return <expression>` exits a function, optionally passing back an expression to the caller. A return statement with no arguments is the same as return `None`. When program execution hits the `return` statement, it immediately exits and doesn't execute anything after.

You can return a value from a function as follows:
```py
# Function definition is here
def sum(arg1, arg2):
   # if statement for the sake of demonstrating different return types and hitting a `return` before the end of the function
   if arg1 == 1337 or arg2 == 1337:
      return "No hackers allowed"
   
   # Add both the parameters and return them."
   total = arg1 + arg2
   print(f"Inside the function: {total}")
   return total

# Now you can call sum function
total = sum(10, 20)
print(f"Outside the function: {total}")

# first, sum(1337, 28) will run, and its return value will be passed as an argument to print
print(f"Attempting h4ck: {sum(1337, 28)}") 
```

When the above code is executed, it produces the following result:
```
Inside the function: 30
Outside the function: 30
Attempting h4ck: No hackers allowed
```


## Calling a Function

Defining a function gives it a name, specifies the parameters that are to be included in the function, and structures the blocks of code.

Once the basic structure of a function is finalized, you can execute it by calling it from another function or directly from the Python prompt. The following is an example of calling the `printme()` function:

```py
# Function definition is here
def printme(my_str):
   "This prints a passed string into this function"
   print (my_str)

# Now you can call printme function
printme("This is first call to the user defined function!")
printme("Second call to the same function")
```

When the above code is executed, it produces the following result −
```
This is first call to the user defined function!
Second call to the same function
```

### Pass by Reference vs Value

All parameters(arguments) in the Python language are passed by reference. This means that if you change what a parameter refers to within a function, the change also reflects back in the calling function. For example:
```py
# Function definition is here
def changeme(mylist):
   print("Values inside the function before change: ", mylist)
   
   mylist[2] = 50
   print("Values inside the function after change: ", mylist)

# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)
```

Here, we are maintaining reference of the passed object and appending values in the same object. Therefore, this would produce the following result −
```
Values inside the function before change:  [10, 20, 30]
Values inside the function after change:  [10, 20, 50]
Values outside the function:  [10, 20, 50]
```

Below is an example of how **NOT** to update variables within functions. The parameter `mylist` is local to the function `changeme()`. Changing `mylist` within the function does not affect `mylist` in `main()`. 
```py
# Function definition is here
def changeme(mylist):
   "This changes a passed list into this function"
   mylist = [1, 2, 3, 4] # This would assign new reference in mylist
   print("Values inside the function: ", mylist)

# Now you can call changeme function
mylist = [10, 20, 30]
changeme(mylist)
print("Values outside the function: ", mylist)
```

The function accomplishes nothing and finally this would produce the following result −
```
Values inside the function:  [1, 2, 3, 4]
Values outside the function:  [10, 20, 30]
```

Variable scope is covered more in depth below in the [Scope of Variables](#scope-of-variables--variable-namespace) section. If you would like to read more about Python's unique approach to function arguments, check out this [RealPython- Pass by Reference](https://realpython.com/python-pass-by-reference/) article. 

### Immutable Data Types

Since all arguments are passed by reference, keep in mind the *type* of the object you pass in to the function. If the function attempts to modify an **immutable** data type, you will get an error. 

The example above worked because the `list` data type is *mutable*. Lets use the *Python interpreter* to see what happens if we try the same function but pass it a `string` object.
```py
>>> def changeme(mylist):
...    "This changes a passed list into this function"
...    print("Values inside the function before change: ", mylist)
...
...    mylist[2] = 50
...    print("Values inside the function after change: ", mylist)

>>> my_str = 'TRAINO ROCKS!'
>>> changeme(my_str)
Values inside the function before change:  TRAINO ROCKS!
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 5, in changeme
TypeError: 'str' object does not support item assignment
```


## Function Arguments

You can call a function by using the following types of formal arguments:

-   Required (positional) arguments
-   Keyword arguments
-   Default arguments
-   Variable-length arguments

### Required Arguments

Required arguments are the arguments passed to a function in correct positional order. Here, the number of arguments in the function call should match exactly with the function definition.

To call the function `printme()`, you **need** to pass one argument, otherwise it gives a syntax error as follows:
```py
def printme(str):
   "This prints a passed string into this function"
   print(str)

# Now you can call printme function
printme()
```

When the above code is executed, it produces the following error:
```
Traceback (most recent call last):
   File "test.py", line 11, in <module>
      printme();
TypeError: printme() takes exactly 1 argument (0 given)
```

### Keyword Arguments

Keyword arguments are related to the function calls. When you use keyword arguments in a function call, the caller identifies the arguments by the *parameter name*.

This allows you to skip arguments or place them out of order because the Python interpreter is able to use the keywords provided to match the values with parameters. You can also make keyword calls to the `printme()` function in the following ways:
```py
def printme(str):
   "This prints a passed string into this function"
   print(str)

# Now you can call printme function
printme(str="My string")
```

When the above code is executed, it produces the following result:
```
My string
```

The following example gives a clearer picture. Note that the order of parameters does not matter:
```py
def printinfo(name, age):
   "This prints a passed info into this function"
   print("Name: ", name)
   print("Age:  ", age)

# Now you can call printinfo function
printinfo(age=50, name="miki")
```

When the above code is executed, it produces the following result:
```
Name:  miki
Age :  50
```

### Default Arguments

A default argument is an argument that assumes a default value if a value is not provided in the function call for that argument. The default value is specified with an (`=`) after the parameter name in the function declaration. The following example gives an idea on default arguments, it assigns a default age of 35 if it is not specified in function call arguments:
```py
def printinfo(name, age = 35):
   print("Name: ", name)
   print("Age ", age)
   return

# Now you can call printinfo function
printinfo(age=50, name="miki")
printinfo(name="miki")
```

When the above code is executed, it produces the following result:
```
Name:  miki
Age  50
Name:  miki
Age  35
```

### Variable-length Arguments

You may need to process a function for more arguments than you specified while defining the function. These arguments are called *variable-length* arguments and are not named in the function definition, unlike required and default arguments.

The syntax for a function with *non-keyword* variable arguments is given below:
```py
def functionname([formal_args,] *var_args_tuple):
   "function_docstring"
   do_code_here
   return <expression>
```

An asterisk (`*`) is placed before the variable name that holds the values of all nonkeyword variable arguments. This tuple remains empty if no additional arguments are specified during the function call. The following is a simple example:
```py
# Function definition is here
def printinfo(arg1, *vartuple):
   print("Output is: ", arg1)
   
   for var in vartuple:
      print(var)
   return

# Now you can call printinfo function
printinfo(10)
printinfo(70, 60, 50)
```

When the above code is executed, it produces the following result:
```
Output is:  10
Output is:  70
60
50
```

## The Anonymous Functions

These functions are called anonymous because they are not declared in the standard manner by using the **`def`** keyword. You can use the **`lambda`** keyword to create small anonymous functions.

-   Lambda functions can take any number of arguments but return just one value in the form of an expression. *They cannot contain multiple expressions*.
-   An anonymous function cannot be a direct call to print because `lambda` requires an expression.
-   Lambda functions have their own local namespace and cannot access variables other than those in their parameter list and those in the global namespace.

### Syntax

**`lambda`** functions contain only a single statement, which is as follows:
```
lambda [arg1 [,arg2,.....argn]]:expression
```

Below is an short example:
```py
# Function definition is here
sum = lambda arg1, arg2: arg1 + arg2

# Now you can call sum as a function
print("Value of total : ", sum(10, 20))
print("Value of total : ", sum(20, 20))
print("sum is of type : ", type(sum))
```

When the above code is executed, it produces the following result:
```
Value of total :  30
Value of total :  40
sum is of type :  <class 'function'>
```

Feel free to play around with the above lambda function, or define your own, in the interactive python interpreter! Keep in mind that lambda functions aren't extremely common.


## Scope of Variables / Variable Namespace

Some variables in a program may not be accessible at all locations in that program. This depends on where you have declared a variable.

The scope (also called a namespace) of a variable determines the portion of the program where you can access a particular identifier. There are two basic scopes of variables in Python:

-   Global variables
-   Local variables

### Global vs. Local variables

Variables that are *defined inside a function body* have a "local scope" (also called "the local namespace"), and those defined *outside of functions* have a "global scope" (or in "global namespace").

This means that local variables can be **accessed only inside the function** in which they are declared, whereas global variables can be **accessed throughout the program body by all functions**. When you call a function, the variables declared inside it are brought into scope. Below is a simple example:
```py
total = 0   # This is global variable.

# Function definition is here
def sum(arg1, arg2):
   # Add both the parameters and return them.
   total = arg1 + arg2; # Here total is a local variable.
   print("sum()'s local total is: ", total)
   return total

# Now you can call sum function
sum( 10, 20 )
print ("The `global` total is still: ", total )
```

When the above code is executed, it produces the following result:
```
sum()'s local total is:  30
The `global` total is still:  0
```

### Using `global` variables

As long as the interpreter executes the variable definition *before attempting to use it in a function*, a function that is defined before a global variable can still contain a global itself. For example, below you see a function defined, then later on the global is defined. However, since the program runs the variable definition *first*, the function still works:
```py
def print_my_global():
   print("The global in print_my_global is: ", my_global)

my_global = "NCWDG{THIS_IS_THE_GLOBAL}"
print_my_global()
```

The output of this is:
```
The global in print_my_global is:  NCWDG{THIS_IS_THE_GLOBAL}
```

As you saw above, we didn't need to do anything within `print_my_global()` to print the global. However, the rules for **modifying** globals within a function's scope and having that change propagate to the rest of the program are different.

### Modifying `global` variables

When you need to modify global variables within functions, which is common, you need to specify to the interpreter that you are trying to modify the **global** variable, not create a function local variable with the same name.

Below is an example of the **INCORRECT** way to modify global variables within functions.
```py
def print_my_global():
   my_global = "NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}"
   print("The global in print_my_global is: ", my_global)

my_global = "NCWDG{THIS_IS_THE_GLOBAL}"
print("First in main, the global is: ", my_global )
print_my_global()
print("Back in main, the global is: ", my_global )
```

Executing this gives the following output:
```
First in main, the global is:  NCWDG{THIS_IS_THE_GLOBAL}
The global in print_my_global is:  NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}
Back in main, the global is:  NCWDG{THIS_IS_THE_GLOBAL}
```

The **CORRECT** way to modify global variables *within function scopes*, is to use the **`global`** keyword. Specifying the keyword immediately before a global variable name tells python to use the global *object reference*, so any modifications will be reflected throughout the program.
```py
def print_my_global():
   global my_global # tell python to use the global namespace object
   my_global = "NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}"
   print("The global in print_my_global is: ", my_global)

my_global = "NCWDG{THIS_IS_THE_GLOBAL}"
print("First in main, the global is: ", my_global )
print_my_global()
print("Back in main, the global is: ", my_global )
```

Now this generates the output:
```
First in main, the global is:  NCWDG{THIS_IS_THE_GLOBAL}
The global in print_my_global is:  NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}
Back in main, the global is:  NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}
```

### Creating Global Variables Within Functions

You can also create global variables within *any scope*, including non-global scopes like within functions, conditional statements, and loops.

Below we show an example of how to **INCORRECTLY** set global variables within non-global scopes:
```py
def print_my_global():
   #  within a conditional to show more nested scoping
   if True:
      my_global = "NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}"
   print("The global in print_my_global is: ", my_global)

print_my_global()
print("Back in main, the global is: ", my_global )
```

This produces the error output:
```
The global in print_my_global is:  NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'my_global' is not defined
```

To fix this, we again use the **`global`** keyword:
```py
def print_my_global():
   #  within a conditional to show more nested scoping
   if True:
      global my_global
      my_global = "NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}"
   print("The global in print_my_global is: ", my_global)

print_my_global()
print("Back in main, the global is: ", my_global )
```

This produces the output:
```
The global in print_my_global is:  NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}
Back in main, the global is:  NCWDG{TRYING_TO_MAKE_THIS_GLOBAL}
```

## Type Hints

In Python, type hints are a way to indicate the expected data types of the parameters and the return value of a function. While Python is a dynamically typed language, meaning you don't have to explicitly declare the data type of a variable, type hints provide a way to add a layer of clarity to your code and make it more understandable, especially for others who might read or work with your code.

To add type hints to a function, you use the colon (`:`) syntax after the parameter name or the return arrow (`->`) before the return type. Here's a basic example:

```py
def add_numbers(x: int, y: int) -> int:
    result = x + y
    return result
```

In this example, the `add_numbers` function takes two parameters (`x` and `y`), both of which are expected to be of type `int`. The `-> int` syntax at the end indicates that the function is expected to return an integer.

### Benefits of Type Hints:

1. **Code Readability:** Type hints make your code more readable and help other developers (or even future you) understand the expected types of variables.
2. **Editor Support:** Many code editors and IDEs use type hints to provide better autocompletion suggestions and catch potential errors as you write code.
3. **Documentation:** Type hints serve as a form of documentation, making it easier for others to understand how to use your functions correctly.
4. **Catch Errors Early:** While Python is dynamically typed, type hints allow you to catch type-related errors early in development, reducing the chances of runtime errors.

### Common Type Hints:

- `int`: Integer
- `float`: Floating-point number
- `str`: String
- `bool`: Boolean
- `list[type]`: List of elements of a specified type
- `tuple[type, type]`: Tuple with specified types for each element
- `dict[key_type, value_type]`: Dictionary with specified key and value types

Here's an example using a list of strings:

```py
def process_names(names: list[str]):
    for name in names:
        print(f"Hello, {name}")
```

In this function, `process_names` takes a list of strings and doesn't return anything (`None`).

> Note: in cases where you are returning `None`, `-> None` is implied if you do not put a type hint for the return type. Generally, putting `-> None` in your function definition is overkill.

By incorporating type hints into your functions, you enhance the clarity and maintainability of your code, making it easier for both you and others to work with.

## References

- [RealPython - Docstrings](https://realpython.com/documenting-python-code/#documenting-your-python-code-base-using-docstrings)
- [RealPython - Pass by Reference](https://realpython.com/python-pass-by-reference/)
- [RealPython - Namespaces and Scope](https://realpython.com/python-namespaces-scope/)

## Sources

- [Tutorialspoint - Functions](https://www.tutorialspoint.com/python3/python_functions.htm)

[Back to README](README.md)