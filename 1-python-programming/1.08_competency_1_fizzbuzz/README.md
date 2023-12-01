# Python Competency 1 - FizzBuzz

[Back to OVERVIEW](../README.md)

Code: [`fizzbuzz.py`](./fizzbuzz.py)

## Objectives

This competency will provide you the opportunity to put all the skills and topics from the start of the Python section until this point into practice. After completing this competency, you should be comfortable with:

- [Basic Syntax](../1.02_basic_syntax/README.md)
- [Variable Types](../1.03_variable_types/README.md)
- [Operators](../1.04_operators/README.md)
- [Conditionals](../1.05_conditionals/README.md)
- [Loops](../1.06_loops/README.md)

## FizzBuzz Implementation Description

For this competency, you will be writing in the code needed for the FizzBuzz program. 

FizzBuzz is a program that prints numbers from 1 to a given limit, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both 3 and 5 with "FizzBuzz."

You will make use of a variable called `limit` that is already created for you. This variable determines how many numbers will be printed. You should use a loop to iterate from 1 to the given `limit`.

For each number, the program should check if it's a multiple of both 3 and 5. If so, you should print "FizzBuzz."

If the number is only a multiple of 3, you should print "Fizz". Similarly, if the number is only a multiple of 5, you should print "Buzz".

If none of the above conditions are met, the program should simply print the number itself.

As an example, a correct implementation of fizzbuzz with the `limit = 20` would be:

```
1
2
Fizz
4
Buzz
Fizz
7
8
Fizz
Buzz
11
Fizz
13
14
FizzBuzz
16
17
Fizz
19
Buzz
```

## Assignment
- [ ] Implement [`fizzbuzz.py`](./fizzbuzz.py) with the functionality described above so that it correctly prints out "Fizz", "Buzz", "FizzBuzz", or the current number in the loop iteration
- [ ] Your program must additionally meet the following requirements:
  - Use of a loop to iterate through the number range
  - Use of conditional statements and operators
  - Use of appropriate arithmetic operator(s)
- [ ] Run `pytest` in your current directory.  If there are no errors, you completed this section.
  - To help debug if you are having issues, [`expected.txt`](./expected.txt) contains the expected output and [`actual.txt`](./actual.txt) contains the output your program produces. 

[Back to OVERVIEW](../README.md)