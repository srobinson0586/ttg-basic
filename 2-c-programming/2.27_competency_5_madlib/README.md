# Complete a large project with nested structs in C

[Back to OVERVIEW](../../README.md)

JQR Addressed: Demonstrate low-level software engineering capability by designing and implementing a program to meet customer requirements in C.

## Purpose

This competency will give you experience designing and implementing a large
project with nested structs in C.


## Instructions

- Read and understand [`spec.txt`](./spec.txt), the specification for the
  .madlib file format.

- Then implement a madlib parser program in C with the additional constraints:
   1. Be able to handle arbitrarily long lines in the input file. This probably
      means using getline instead of fgets.

   2. Create a structure that can represent an arbitrary category (e.g., noun,
      adjective, verb, etc).

   3. Store all categories found in the template in a dynamically reallocated
      array (i.e, an array of contiguous elements in memory, which you reallocate
      as needed as it grows).

   4. Create a structure that can represent an instance of an arbitrary
      category.

   5. Each category structure should contain a circularly linked list of the
      instances it contains.

   6. To choose a random instance of a particular category, you should choose
      a random short and then iterate through the circularly linked list of the
      appropriate category that many steps.

   7. Write a Makefile for your project. Your project should compile and run
      with no compiler warnings and no Valgrind errors.

[Back to OVERVIEW](../../README.md)