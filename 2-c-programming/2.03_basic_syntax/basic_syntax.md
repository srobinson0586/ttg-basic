# C - Basic Syntax

You have seen the basic structure of a C program, so it will be easy to understand other basic building blocks of the C programming language.

## Semicolons

In a C program, the semicolon is a statement terminator. That is, each individual statement must be ended with a semicolon. It indicates the end of one logical entity.

Given below are two different statements:

```c
printf("Hello, World! \n");
return 0;
```

## Comments

Comments are like helping text in your C program and they are ignored by the compiler. Single line comments are indicated by **//**.  Multi-line comments start with **/*** and terminate with the characters ***/** as shown below:

```c
// single line comment

/* Multi-line
   Comment */
```

You cannot have comments within comments and they do not occur within a string or character literals.

## Identifiers

A C identifier is a name used to identify a variable, function, or any other user-defined item. An identifier starts with a letter A to Z, a to z, or an underscore '_' followed by zero or more letters, underscores, and digits (0 to 9).

C does not allow punctuation characters such as @, $, and % within identifiers. C is a **case-sensitive** programming language. Thus, _Manpower_ and _manpower_ are two different identifiers in C. Here are some examples of acceptable identifiers:
 \- | - | - | - | - 
--- | --- | --- | --- | ---
mohd | zara | abc | move_name | a_123
myname50 | _temp | j | a23b9 | retVal

## Keywords

The following list shows the reserved words in C. These reserved words may not be used as constants or variables or any other identifier names.
 \- | - | - | - 
--- | --- | --- | ---
auto | else | long | switch 
break | enum | register | typedef 
case | extern | return | union 
char | float | short | unsigned 
const | for | signed | void 
continue | goto | sizeof | volatile 
default | if | static | while 
do | int | struct | _Packed 
double

## Whitespace in C

A line containing only whitespace, possibly with a comment, is known as a blank line, and a C compiler totally ignores it.

Whitespace is the term used in C to describe blanks, tabs, newline characters and comments. Whitespace separates one part of a statement from another and enables the compiler to identify where one element in a statement, such as int, ends and the next element begins. Therefore, in the following statement:

```c
int age;
```

There must be at least one whitespace character (usually a space) between int and age for the compiler to be able to distinguish them. On the other hand, in the following statement:

```c
fruit = apples + oranges;   // get the total fruit
```

No whitespace characters are necessary between fruit and =, or between = and apples, although it is a good practice to include them to increase readability.

## Resources

- [GeeksforGeeks - C Tokens](https://www.geeksforgeeks.org/tokens-in-c)
- [Semicolons in C Programming](https://www.learn-c.org/semicolons-in-c)
- [C Programming - Comments](https://www.learn-c.org/comments)
- [C Programming - Identifiers](https://www.learn-c.org/identifiers)
- [C Keywords - GeeksforGeeks](https://www.geeksforgeeks.org/c-keywords/)
- [Whitespace in C Programming](https://www.programiz.com/c-programming/c-formatting)
- [C Coding Style Guidelines](https://users.ece.cmu.edu/~eno/coding/CCodingStandard.html)

## Source

- [C - Basic Syntax](https://www.tutorialspoint.com/cprogramming/c_basic_syntax.htm)

[Back to README](README.md)