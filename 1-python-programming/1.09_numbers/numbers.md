# Python - Numbers

[Back to README](README.md)

Whether it is for simple arithmetic like you'd perform on a basic calculator or for complex arithmetic used in cryptography, data analysis, simulation models, etc., you will constantly be working with numbers as a programmer when you code. Knowing how to make numbers work for you will allow you to more easily achieve your desired program behaviors.

## Numerical Types

As mentioned in [module 1.03](../1.03_variable_types/variable_types.md), Python 3 supports three different numerical types:

*   **`int` (signed integers)** − They are often called just integers or ints, are positive or negative whole numbers with no decimal point.
    
*   **`float` (floating point real values)** − Also called floats, they represent real numbers and are written with a decimal point dividing the integer and fractional parts. Floats may also be in scientific notation, with E or e indicating the power of 10 (2.5e2 = 2.5 x 10^2 = 250).
    
*   **`complex` (complex numbers)** − are of the form `a + bJ`, where `a` and `b` are floats and `J` (or `j`) represents the square root of -1 (which is an imaginary number). The real part of the number is `a`, and the imaginary part is `b`. We will not be using Complex numbers much in the JQR.

### Examples

Here are some examples of numbers


|int     |float       |complex     |
|--------|------------|------------|
|`10`    |`0.0`       |`3.14j`     |
|`100`   |`15.20`     |`45.j`      |
|`-786`  |`-21.9`     |`9.322e-36j`|
|`080`   |`32.3+e18`  |`.876j`     |
|`-0490` |`-90.`      |`-.6545+0J` |
|`-0x260`|`-32.54e100`|`3e+26J`    |
|`0x69`  |`70.2-E12`  |`4.53e-7j`  |


## The `math` Module

Python's `math` module is a built-in module that provides a set of mathematical functions and constants. It offers a wide range of mathematical operations and calculations that are commonly used in scientific, engineering, financial, and other numerical computations. Using the `math` module can simplify the work required to manipulate numbers for your applications. More information on Python modules is given in [1.16_modules](../1.16_modules).

To use what the `math` module has to offer, you need to import it at the beginning of your Python script or interactive session:

```python
import math
```

### Math Constants

The `math` module has constants for:

- Pi
- Tau
- Euler's number
- Infinity
- NaN (not a number)

They can be accessed in your code using the following:

```python
math.pi
math.tau
math.e
math.inf
math.nan
```

Respectively, their values are:

```
3.141592653589793
6.283185307179586
2.718281828459045
inf
nan
```

### Math Functions

There are many mathematical functions offered by the `math` module (which can be referenced [here](https://docs.python.org/3/library/math.html)), but some of the common functions that you might use are:

- **`abs(x)`** - The absolute value of `x`: the (positive) distance between `x` and zero.

- **`ceil(x)`** - The ceiling of `x`: the smallest integer not less than `x`.

- **`cmp(x, y)`** - returns 1 if `x > y`, 0 if `x == y`, or -1 if `x < y`

- **`exp(x)`** - The exponential of `x`: ex

- **`fabs(x)`** - The absolute value of a floating point `x`.

- **`floor(x)`** - The floor of `x`: the largest integer not greater than `x`.

- **`log(x)`** - The natural logarithm of `x`, for `x > 0`.

- **`log10(x)`** - The base-10 logarithm of `x` for `x > 0`.

- **`max(x1, x2,...)`** - The largest of its arguments: the value closest to positive infinity.

- **`min(x1, x2,...)`** - The smallest of its arguments: the value closest to negative infinity.

- **`modf(x)`** - The fractional and integer parts of `x` in a two-item tuple. Both parts have the same sign as `x`. The integer part is returned as a float.

- **`pow(x, y)`** - The value of `x**y`.

- **`round(x [,n])`** - `x` rounded to `n` digits from the decimal point. Python rounds away from zero as a tie-breaker: round(0.5) is 1.0 and round(-0.5) is -1.0.

- **`sqrt(x)`** - The square root of `x` for `x > 0`.

#### Example uses

```python
x = 5.5
y = 10
z = 3

print(f"Ceiling of {x} = ", math.ceil(x))
print(f"Floor of {x} = ", math.floor(x))
print(f"{y}^{z} = {math.pow(y, 3)}")
```

#### Output

```
Ceiling of 5.5 = 6
Floor of 5.5 = 5
10^3 = 1000
```

## Truthiness

Using Python we have the ability to use numbers as part of conditional statements like:

```python
if <value>:

while <value>:
```

These statements are valid because Python can evaluate numerical values in a boolean (True or False) context. 

Here's how truthiness works for numerical values in Python:

- **Non-zero Values:** Numerical values that are non-zero (positive or negative) are considered truthy. This means that if a numeric value is not zero, it evaluates to `True` in a boolean context.

- **Zero Value:** The numeric value zero (0) is considered falsy. It evaluates to `False` in a boolean context.

### Examples

#### Truthy

```python
x = 42
if x:
    print("x is truthy")
```

```
x is truthy
```

#### Falsy

```python
x = 0
if x:
    print("x is truthy")
else:
    print("x is falsy")
```

```
x is falsy
```

# Sources

- [Math | Python Docs](https://docs.python.org/3/library/math.html)
- [Python Math Module | Geeksforgeeks](https://www.geeksforgeeks.org/python-math-module/)

[Back to README](README.md)