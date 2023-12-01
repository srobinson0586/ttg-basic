# Python Operators

[Back to README](README.md)

Operators are the symbols which can compute new things using operands. Take for example the expression `4 + 5 = 9`. Here, `4` and `5` are called the operands, `+` is called the operator, and the new value `9` is computed.

## Types of Operators

Python language supports the following types of operators:
- Arithmetic Operators
- Comparison (Relational) Operators
- Assignment Operators
- Logical Operators
- Bitwise Operators
- Membership Operators
- Identity Operators

Lets have a look at all the operators one by one.


## Python Arithmetic Operators

Below you can see an example of all the python arithmetic operators in use:
```py
a = 21
b = 10

c = a + b
print ("Line 1 - Value of c is ", c)

c = a - b
print ("Line 2 - Value of c is ", c )

c = a * b
print ("Line 3 - Value of c is ", c)

c = a / b
print ("Line 4 - Value of c is ", c )

c = a % b
print ("Line 5 - Value of c is ", c)

a = 2
b = 3
c = a**b 
print ("Line 6 - Value of c is ", c)

a = 10
b = 5
c = a//b 
print ("Line 7 - Value of c is ", c)
```

When ran, that script outputs:
```
Line 1 - Value of c is  31
Line 2 - Value of c is  11
Line 3 - Value of c is  210
Line 4 - Value of c is  2
Line 5 - Value of c is  1
Line 6 - Value of c is  8
Line 7 - Value of c is  2
```


- Operator: `+` Addition
  - Description: Adds values on either side of the operator.
- Operator: `-` Subtraction
  - Description: Subtracts right hand operand from left hand operand.
- Operator: `*` Multiplication
  - Description: Multiplies values on either side of the operator
- Operator: `/` Division
  - Description: Divides left hand operand by right hand operand
- Operator: `%` Modulus
  - Description: Divides left hand operand by right hand operand and returns remainder
- Operator: `//` Floor/Integer Division
  - Description: Divides left hand operand by right hand operand and drops the remainder
  - Note: If one of the operands is negative, the result is rounded away from zero (towards negative infinity)
- Operator: `**` Exponent
  - Description: Performs exponential (power) calculation on operators


## Python Comparison Operators

These operators compare the values on either side of them and decide the relation among them. They are also called Relational operators.

Below you can see an example of all the python comparison operators in use:
```py
a = 21
b = 10

if ( a == b ):
  print ("Line 1 - a is equal to b")
else:
  print ("Line 1 - a is not equal to b")

if ( a != b ):
  print ("Line 2 - a is not equal to b")
else:
  print ("Line 2 - a is equal to b")

if ( a < b ):
  print ("Line 3 - a is less than b" )
else:
  print ("Line 3 - a is not less than b")

if ( a > b ):
  print ("Line 4 - a is greater than b")
else:
  print ("Line 4 - a is not greater than b")

a,b = b,a #values of a and b swapped. a becomes 10, b becomes 21

if ( a <= b ):
  print ("Line 5 - a is either less than or equal to  b")
else:
  print ("Line 5 - a is neither less than nor equal to  b")

if ( b >= a ):
  print ("Line 6 - b is either greater than  or equal to b")
else:
  print ("Line 6 - b is neither greater than  nor equal to b")
```

When ran, the above script outputs:
```
Line 1 - a is not equal to b
Line 2 - a is not equal to b
Line 3 - a is not less than b
Line 4 - a is greater than b
Line 5 - a is either less than or equal to  b
Line 6 - b is either greater than  or equal to b
```

- Operator: `==` Equality Comparison
  - Description: If the values of two operands are equal, then the condition becomes true.
- Operator: `!=` Non-equality Comparison
  - Description: If the values of the two operands are not equal, then the condition becomes true.
- Operator: `>`  Greater-than Comparioson
  - Description: If the value of left operand is greater than the value of the right operand, then the condition becomes true.
- Operator: `<`  Less-than Comparison
  - Description: If the value of left operand is less than the value of the right operand, then the condition becomes true.
- Operator: `>=` Greater-than or Equal-to Comparison
  - Description: If the value of left operand is greater than or equal to the value of the right operand, then the condition becomes true.
- Operator: `<=` Less-than or Equal-to Comparison
  - Description: If the value of left operand is less than or equal to the value of the right operand, then the condition becomes true.


## Python Assignment Operators

Python assignment operators assign the right-side value to the left-side variable. There are some operators shown below that will help you write less code by completing two instructions in one operand.

- Operator: `=`
  - Description: Assigns values from right side operands to the left side operand
  - Example: `c = a + b` assigns the value of `a + b` into `c`
- Operator: `:=` **NEW in Python 3.8**
  - Description: Assigns values to variables as part of a larger expression, usually used as a way to make conditional code cleaner.
  - Example: The first python snippet below shows a traditional way of using the return of an expression in a conditional (covered in [1.05_conditionals])
```py
env_base = os.environ.get("PYTHONUSERBASE", None)
if env_base:
    return env_base
```
With the walrus operator, this can be written as:
```py
if env_base := os.environ.get("PYTHONUSERBASE", None):
    return env_base
```
For more, you can check out [PEP 572](https://peps.python.org/pep-0572/#examples).
- Operator: `+=`
  - Description: Adds the right operand to the left operand and assigns the result to the left operand
  - Example: `c += a` is equivalent to `c = c + a`
- Operator: `-=`
  - Description: Subtracts the right operand from the left operand and assigns the result to the left operand
  - Example: `c -= a` is equivalent to `c = c - a`
- Operator: `*=`
  - Description: Multiplies the right operand with the left operand and assigns the result to the left operand
  - Example: `c *= a` is equivalent to `c = c * a`
- Operator: `/=`
  - Description: Divides the left operand with the right operand and assigns the result to the left operand
  - Example: `c /= a` is equivalent to `c = c / a`
- Operator: `%=`
  - Description: Computes the modulus of both operands and assigns the result to the left operand
  - Example: `c %= a` is equivalent to `c = c % a`
- Operator: `**=`
  - Description: Performs the exponential calculation on operators and assigns the result to the left operand
  -Example: `c **= a` is equivalent to `c = c ** a`
- Operator: `//=` 
  - Description: Performs floor division on the operators and assigns the result to the left operand
  - Example: `c //= a` is equivalent to `c = c // a`


## Python Bitwise Operators

Bitwise operators work on bits and perform bit-by-bit operation. Python's built-in `bin()` function can be used to obtain a binary 1s and 0s representation of an integer number. We use it in combination with tuples, string methods, and put it together in a lambda function below to show the use of several bitwise operators:
```py
# lambda function to prettify bin strings, don't need to understand
pprint_bin = lambda b : print(f"{b[0].upper()}".ljust(7) + f":  {bin(b[1]).replace('0b', '').replace('-', '').rjust(8, '0')}")
a = 10
b = 6

pprint_bin(('a',a))
pprint_bin(('b',b))

c = a & b
pprint_bin(('a & b',c))

c = a | b
pprint_bin(('a | b',c))

c = a ^ b
pprint_bin(('a ^ b',c))

c = ~a
pprint_bin(('~a',c))

c = a << 2
pprint_bin(('a << 2',c))

c = a >> 2
pprint_bin(('a >> 2',c))
```

Don't worry too much about understanding the complex `pprint_bin` function, its only a means through which to show pretty output. Everything used in it is covered in later modules. When ran, that script produces the following output:
```
A      :  00001010
B      :  00000110
A & B  :  00000010
A | B  :  00001110
A ^ B  :  00001100
~A     :  00001011 # Unexpected output? Try figuring out why
A << 2 :  00101000
A >> 2 :  00000010
```

Bitwise operators are implemented in nearly every language. You won't use them much in python, but they will be more prevalent in low-level languages like C. Understanding the concept is also important for CNO Developers because it familiarizes you with bit manipulation. For more on bitwise operations in general, check out [Bitwise Operators and WHY we use them](https://www.youtube.com/watch?v=igIjGxF2J-w).


## Python Logical Operators

Logical operators are used to evaluate the relationship between two booleans, or two expressions that evaluate to booleans. Below we use each of the three logical operators to determine which if/else branches get executed (more on them in [1.05_conditionals](../1.05_conditionals/conditionals.md)):
```py
if True and False:
    print("'and1': Both are True!")
else:
    print("'and1': Evaluated to False!")

if True and True:
    print("'and2': Both are True!")
else:
    print("'and2': Evaluated to False!")


if True or False:
    print("'or':   Both are True!")
else:
    print("'or':  Evaluated to False!")


if not False:
    print("'not':  Evaluated to True!")
else:
    print("'not': Evaluated to False!")
```

Running this gives the output:
```
'and1': Evaluated to False!
'and2': Both are True!
'or':   Both are True!
'not':  Evaluated to True!
```

- Operator: `and` Logical AND
  - Description: If both the operands are true then the condition becomes true.
- Operator: `or` Logical OR
  - Description: If any of the two operands are true then the condition becomes true.
- Operator: `not` Logical NOT
  - Description: Used to reverse the logical state of its operand.


## Python Membership Operators


Python’s membership operators test for membership in a sequence, such as strings, lists, or tuples. There are two membership operators as demonstrated below
```py
my_seq = ['a', 'b', 3, 2]

if 'a' in my_seq:
  print("Found 'a'!")

if 'a' not in my_seq:
  print("Didn't find 'a'!")
```

Running that script outputs:
```
Found 'a'!
```

- Operator: `in`
  - Description: Evaluates to true if it finds a variable in the specified sequence and false otherwise.
- Operator: `not in`
  - Description: Evaluates to true if it does not find a value in the specified sequence and false otherwise.


## Python Identity Operators

Identity operators compare the memory locations of two objects. Basically its the result of running `id(a) == id(b)`:
```py
a, b = 1,1
c = 0

print("ID A:", hex(id(a)))
print("ID B:", hex(id(b)))
print("ID C:", hex(id(c)))

# The python interpreter sees that a & b get assigned the same value, so it saves memory space by having them "reference" the same integer "object"
if a is b:
    print("A is B")

if a is not c:
    print("A is not C")

c += 1
# The interpreter sees that c requires a value of 1, so it deletes the previous int object with value 0 and makes c reference the existing object of value 1
if a is c:
    print("A is C")
```

Running the above outputs:
```
ID A: 0x7ffd4649e328
ID B: 0x7ffd4649e328
ID C: 0x7ffd4649e308
A is B
A is not C
A is C
```

- Operator: `is`
  - Description: Evaluates to true if the variables on either side of the operator point to the same object and false otherwise.
- Operator: `is not`
  - Description: Evaluates to false if the variables on either side of the operator point to the same object and true otherwise.


## Python Operators Precedence

The python interpreter doesn't always execute a line of code from left to right. Each programming language may have a different order in which operators are applied to their surrounding operands. In python, the operand precedence order is given by the table on the [Official Python 3 Docs](https://docs.python.org/3/reference/expressions.html#operator-precedence). Higher precedence means that it gets evaluated / executed first.

For arithmetic operations, you can see that python keeps the classic PEMDAS order. If two operators are of the same precedence, they are evaluated left to right.

Below is a small example of throwing together a bunch of operands:
```py
a = 4444
b = 1337
c = 1840
d = 'boring'
e = 2

f = d.replace('boring', 'NCWDG ') * (( a // c + e ^ a ** e ) % 6)
print(f)
```

Running that outputs:
```
NCWDG NCWDG
```

Lets go over step-by-step the interpreter's order of evaluation:
1. `(a ** e)`
2. `(a // c)`
3. `( (a//c) + e)`
4. `( ((a//c) + e) ^ (a**e) )`
5. `( (((a//c) + e) ^ (a**e)) % 6 )`
6. `( d.replace('boring', 'NCWDG ') * ((((a//c) + e) ^ (a**e)) % 6) )`

Precedence TLDR;
> When using complex combinations of operators, use parentheses to make sure the code is doing what you intend it to do, and to help people reading your code understand it. However, don't overdo it with the parentheses either, as seen on step 6.

## Resources

- [YouTube | Bitwise Operators and WHY we use them](https://www.youtube.com/watch?v=igIjGxF2J-w)
- [Python 3 Docs | Operator Precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence)
- [PEP 572](https://peps.python.org/pep-0572/#examples)

## Sources

- [TutorialsPoint | Python Basic Operators](https://www.tutorialspoint.com/python3/python_basic_operators.htm)
- [TutorialsPoint | Python Comparison Operators](https://www.tutorialspoint.com/python3/comparison_operators_example.htm)

[Back to README](README.md)
