# C Programming - Scores

[Back to Overview](../README.md)

## Objectives

This competency will provide you the opportunity to put all the new skills and topics into practice. 

## Scores Implementation Description

For this competency, you will be writing the code needed for the Scores program. 

Scores is a program that creates an array of user defined length, fills that array with random integers, and then prints the array's contents as well as the average, highest, and lowest value of the array.

We have given you access to the CS50 library (Courtesy of Harvard University). This will allow you to receive user input since user input will not be taught until later in the JQR due to the complexity. 

You will make use of the `get_int()` function in this library to determine how big to make the scores array. You should be familiar with how the `get_int()` function works from the [previous competency](../2.09_competency_1_fizzbuzz/README.md).

You will also make use of the `fill_random_array()` function in this library to fill an array with random integers.

### Using fill_random_array():
This function takes an array and size as parameters and then fills the array with random integers. Below is some sample code for using the function:
```c
int arr[10] = {};
fill_random_array(arr, 10);
// arr now holds 10 random integer values
```

### Example Scores Usage:
```bash
$ ./scores
Enter length: 10

Generated Array - 23, 73, 36, 94, 55, 46, 12, 42, 54, 86
Average - 52
Highest - 94
Lowest - 12
```

## Assignment
- [ ] Implement [`scores.c`](./scores.c) with the functionality described above so that it correctly prints the array values as well as the average, highest, and lowest value for that array.
- [ ] Your program must additionally meet the following requirements:
  - Use of loops to iterate through the array
  - Use of appropriate arithmetic operators
  - Get user input with the `get_int()` function
  - Fill the array using the `fill_random_array()` function

[Back to Overview](../README.md)

