# Python Conditionals

[Back to README](README.md)

In the [last module](../1.04_operators/operators.md) we covered several operators that are critical to python condtional statements, mainly Comparison, Logical, Membership, and Identity Operators. These operators can be used in several ways, most commonly in "if statements" and loops.

You've seen all the conditional statements covered in this module in previous modules. Here, we will cover them more in detail.


## `if` Statements

An "if statement" is written by using the `if` keyword. They are used to tell the python interpreter to execute a block of code **only if** the given expression is True.
```py
a = 33  
b = 200  
if b > a:  
  print("b is greater than a")
```

Running that prints:
```
b is greater than a
```

## `elif` Statements

The `elif` keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
```py
a = 33  
b = 33  
if b > a:  
    print("b is greater than a")
elif b < a:
    print("b is less than a")
elif a == b:  
    print("a and b are equal")
```
Running that prints:
```
a and b are equal
```
In this example a is equal to b, so neither the first nor the second condition is true. But the third `elif` condition is true, so we print that "a and b are equal". Note that we could've replaced this last `elif` with an `else` statement.

You must have an `if` statement before you can use `elif`. Also, `elif`s are all tied to the `if` statement that was used before it. Only use `elif`s if only one of them should be true because if another `elif` or `if` before it is True, then the `elif` will never even be evaluated. Here's an example where we try making sure both ints are positive:
```py
a = 82
b = -234

if a > 0:
    print("A is good")
elif b > 0:
    print("B is good")
```

Here, we would be unaware that B is NOT good because the first `if` statement was true and the `elif` was never evaluated. This is a simple example, but keep this in mind when you encounter more complex scenarios.


## `else` Statements

The else keyword catches anything which isn't caught by the preceding conditions. Here we show a better way of coding the first `elif` example that was shown above.
```py
a = 33
b = 33  
if b > a:  
  print("b is greater than a")  
elif b < a:
    print("b is less than a") 
else:  
  print("b is equal to a")  
```

You can have an `else` without a preceding `elif`, but you **need** an `if`:
```py
a = 200  
b = 33  
if b > a:  
  print("b is greater than a")  
else:  
  print("b is not greater than a")  
```


## Short Hand If

If you have only one statement to execute, you can put it on the same line as the if statement. This can be considered bad coding practice, so keep its use to a minimum.
```py
if a > b: print("a is greater than b")
```


## Short Hand If ... Else

If you have only one statement to execute, one for if, and one for else, you can put it all on the same line. This can be used as Python's replacement for the **ternary operator** seen in other languages like C.
```py
a = 2  
b = 330  
max_num = a if a > b else b   # max_num is 330
```

You can also have multiple else statements on the same line. This is considered bad coding practice, so keep it to a minimum:
```py
a = 330  
b = 330  
print("A") if a > b else print("=") if a == b else print("B")
```


## Nested Conditionals

You can have `if`, `elif`, and `else` statements inside other `if`, `elif`, and `else` statements. These are called _nested_ conditional statements.
```py
x = 41

if x > 10:  
  print("Above ten,")  
  if x > 20:  
    print("and also above 20!")  
  else:  
    print("but not above 20.")
elif x < 10:
    print("Under ten")
else:
    print("x IS 10")
```

## Implementing Switches with `match` and `case` 

In many programming languages, there is a concept of a `switch` statement. A switch statement can replace multiple `if` statement checks. It gives a more descriptive way to compare a value with multiple variants. Often times its used in situations where a variable could hold many different values and the program performs different actions depending on the value. 

Switch statements will be covered in much more detail in the TTG-B's C programming section, but here is an example of what a C switch statement could look like:
```c
switch(menuSelection) {
  case 1:  // if (menuSelection === 1)
    // do case 1 stuff
    break

  case 2:  // if (menuSelection === 2)
    // do case 2 stuff
    break

  default:
    // what if none of the above are true
    break
}
```

From version 3.10 upwards, Python has implemented a switch case feature called "structural pattern matching". You can implement this feature with the `match` and `case` keywords. In Python versions before 3.10, you would've implemented the above with:
```py
menu_selection = input("Choose a menu option")  # get input from command line from user
if menu_selection == 1:
    print("You chose 1")
elif menu_selection == 2:
    print("You chose 2")
else:
    print("You didn't choose 1 OR 2")
```

This can now be done more elegantly `match` and `case`:
```py
menu_selection = input("Choose a menu option")  # get input from command line from user

match menu_selection:
    case 1:
        print("You chose 1")
    case 2:
        print("You chose 2")
    case _:
        print("You didn't choose 1 OR 2")
```

If you'd like more examples, checkout [FreeCodeCamp | Python Switch](https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/).

**Note**
> Keep in mind that newer Python features like this one **will not work** on old python versions. You need to be aware of where your code will be ran and by who. If you are in an environment where Python packages don't get updated frequently, usually because of classification hurdles, you are better off sticking to basic builtin python features.

## Resources
- [FreeCodeCamp | Python Switch](https://www.freecodecamp.org/news/python-switch-statement-switch-case-example/)

## Sources
- [TutorialsPoint | if-elif-else](https://www.tutorialspoint.com/python/python_if_else.htm)

[Back to README](README.md)
