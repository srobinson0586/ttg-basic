# C Programming - FizzBuzz

[Back to Overview](../README.md)

## Objectives

This competency will provide you the opportunity to put all the skills and topics from the start of the C section until this point into practice. 

## FizzBuzz Implementation Description

For this competency, you will be writing in the code needed for the FizzBuzz program. 

FizzBuzz is a program that prints numbers from 1 to a given limit, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both 3 and 5 with "FizzBuzz."

We have given you access to the CS50 library (Courtesy of Harvard University). This will allow you to receive user input since user input will not be taught until later in the JQR due to the complexity. You will make use of the `get_int()` function in this library to receive a limit from the user. You should use a loop to iterate from 1 to the given input.

For each number in this range, the program should check if it's a multiple of both 3 and 5. If so, you should print "FizzBuzz."

If the number is only a multiple of 3, you should print "Fizz". Similarly, if the number is only a multiple of 5, you should print "Buzz".

If none of the above conditions are met, the program should simply print the number itself.

### Example Usage:

```
$ ./fizzbuzz
Enter limit: 20
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
- [ ] Implement [`fizzbuzz.c`](./fizzbuzz.c) with the functionality described above so that it correctly prints out "Fizz", "Buzz", "FizzBuzz", or the current number in the loop iteration
- [ ] Your program must additionally meet the following requirements:
  - Use of a loop to iterate through the number range
  - Use of conditional statements and operators
  - Use of appropriate arithmetic operator(s) 
  - Get user input with the `get_int()` function

[Back to Overview](../README.md)