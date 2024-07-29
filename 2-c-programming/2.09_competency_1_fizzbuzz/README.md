# C Programming - FizzBuzz

[Back to Overview](../README.md)

## Objectives

This competency will provide you the opportunity to put all the skills and topics from the start of the C section until this point into practice. 

## FizzBuzz Implementation Description

For this competency, you will be writing the code needed for the FizzBuzz program. 

FizzBuzz is a program that prints numbers from 1 to a given limit, replacing multiples of 3 with "Fizz," multiples of 5 with "Buzz," and multiples of both 3 and 5 with "FizzBuzz."

We have given you access to the CS50 library (Courtesy of Harvard University). This will allow you to receive user input since user input will not be taught until later in the TTG-B due to the complexity. 

You will make use of the `get_int()` function in this library to receive a limit from the user. You should use a loop to iterate from 1 to the given input.

For each number in this range, the program should check if it's a multiple of both 3 and 5. If so, you should print "FizzBuzz."

If the number is only a multiple of 3, you should print "Fizz". Similarly, if the number is only a multiple of 5, you should print "Buzz".

If none of the above conditions are met, the program should simply print the number itself.

### Using get_int():
This function prompts the user for an integer. The user's input is validated and the function will prompt the user again if necessary. Below is some sample code for using the function:
```c
int num = get_int("Input: ");
// num now holds the value the user typed
```
More information can be found [here](https://manual.cs50.io/3/get_int)

### Printing a number:
Here is some sample code for printing a number which will be covered in detail in a later [section](../2.11_strings/knowledge_check.md):
```c
int num = 11;
printf("%i\n", num);
```
For now just know that the `%i` within the string lets the `printf` function know that we intend to pass an integer as an additional parameter.

### Example FizzBuzz Usage:

```bash
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
  - Use of appropriate arithmetic operators
  - Get user input with the `get_int()` function

[Back to Overview](../README.md)