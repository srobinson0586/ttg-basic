# C Programming: Data Types

Where Python has dynamic data typing (i.e. "Duck typing"), C has strict data typing, meaning you need to declare the data type of a variable before using it. Data types in C refer to an extensive system used for declaring variables or functions of different types. The type of a variable determines how much space it occupies in storage and how the bit pattern stored is interpreted.  Also C is a statically typed language, so the type of a variable cannot change once it's declared.

In C programming, there are several common data types that you can use to store different kinds of values. Here are the most commonly used data types:

1. **int (Integer)**:
   - Used to store whole numbers (positive or negative) without decimal points.
   - Typical size is 4 bytes, but it can vary depending on the compiler and platform.
   - Example:
   ```c
   int age; // Declaration of an integer variable
   age = 25; // Assigning a value to the variable
   ```

1. **float (Floating-Point)**:
   - Used to store numbers with decimal points.
   - Typically 4 bytes in size.
   - Example:
   ```c
   float price; // Declaration of a floating-point variable
   price = 3.99; // Assigning a value to the variable
   ```

1. **double (Double Precision Floating-Point)**:
   - Used to store floating-point numbers with higher precision compared to `float`.
   - Typically 8 bytes in size.
   - Example:
   ```c
   double pi; // Declaration of a double precision floating-point variable
   pi = 3.14159265359; // Assigning a value to the variable
   ```

1. **char (Character)**:
   - Used to store a single character or a small integer.
   - Always 1 byte in size.
   - Example:
   ```c
   char grade; // Declaration of a character variable
   grade = 'A'; // Assigning a value to the variable
   ```
1. **char array (String)**:
   - In C, a string is an array of characters; there is not a dedicated data type as in Python. 
   - Example:
   ```c
   char name[20]; // Declaration of a character array for a string
   strcpy(name, "John Smith"); // Assigning a string to the array
   ```

1. **_Bool (Boolean)**:
   - Used to represent Boolean values, which can be either true or false.
   - 0 typically represents `false`, and any non-zero value represents `true`.
   - Size is implementation-dependent but often 1 byte.
   - Example: 
   ```c
   int isTrue; // Declaration of a boolean variable using an integer
   isTrue = 1; // Assigning a value (true)
   ```

1. **short (Short Integer)**:
   - Used to store small whole numbers.
   - Typically 2 bytes in size.
   - Example:
   ```c
   short distance; // Declaration of a short integer variable
   distance = 100; // Assigning a value to the variable
   ```

1. **long (Long Integer)**:
   - Used to store larger whole numbers.
   - Size can vary but is typically 4 bytes or more.
   - Example:
   ```c
   long population; // Declaration of a long integer variable
   population = 1000000L; // Assigning a value to the variable (the 'L' denotes a long literal)
   ```

1. **Arrays**:
   - Used to store a collection of elements of the same data type.
   - Size is determined by the number of elements and the data type.
   - Example:
   ```c
   // Declaration of an integer array with 5 elements
   int numbers[5];
   numbers[0] = 1;
   numbers[1] = 2;
   // ...
   numbers[4] = 5;

   // Declaration and initialization of a character array
   char vowels[] = {'a', 'e', 'i', 'o', 'u'}; 
   ```
1. **void**:
    - Represents an absence of type for use in several contexts.
    - Common use as a return type for functions that do not return any value.
    - Example:
    ```c
    void printHello() {
        printf("Hello, World!\n");
    }
    ```
1. **Pointers**:
    - Used to store memory addresses of other variables.
    - Size is platform-dependent but often 4 or 8 bytes on modern systems.
    - Example:
    ```c
    int *ptr; // Declaration of an integer pointer
    int value = 42;
    ptr = &value; // Assigning the address of 'value' to 'ptr'
    ```

NOTE: Pointers will be discussed in greater detail in section 2.12

## Integer Types

The following table provides the details of standard integer types with their storage sizes and value ranges:

Type | Storage Size | Value range
-------- | -------- | --------
char | 1 byte | -128 to 127 or 0 to 255
unsigned char  | 1 byte | 0 to 255 |
signed char | 1 byte | -128 to 127 
int | 2 or 4 bytes | -32,768 to 32,767 or -2,147,483,648 to 2,147,483,647 
unsigned int | 2 or 4 bytes | 0 to 65,535 or 0 to 4,294,967,295
short | 2 bytes | -32,768 to 32,767 
unsigned short | 2 bytes | 0 to 65,535
long | 8 bytes or (4bytes for 32 bit OS) | -9223372036854775808 to 9223372036854775807
unsigned long | 8 bytes | 0 to 18446744073709551615

To get the exact size of a type or a variable on a particular platform, you can use the **sizeof** operator. The expressions _sizeof(type)_ yields the storage size of the object or type in bytes. 

Below is an example to get the size of various type on a machine using different constant defined in limits.h header file:
```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>

int main(int argc, char** argv) {

    printf("CHAR_BIT    :   %d\n", CHAR_BIT);
    printf("CHAR_MAX    :   %d\n", CHAR_MAX);
    printf("CHAR_MIN    :   %d\n", CHAR_MIN);
    printf("INT_MAX     :   %d\n", INT_MAX);
    printf("INT_MIN     :   %d\n", INT_MIN);
    printf("LONG_MAX    :   %ld\n", (long) LONG_MAX);
    printf("LONG_MIN    :   %ld\n", (long) LONG_MIN);
    printf("SCHAR_MAX   :   %d\n", SCHAR_MAX);
    printf("SCHAR_MIN   :   %d\n", SCHAR_MIN);
    printf("SHRT_MAX    :   %d\n", SHRT_MAX);
    printf("SHRT_MIN    :   %d\n", SHRT_MIN);
    printf("UCHAR_MAX   :   %d\n", UCHAR_MAX);
    printf("UINT_MAX    :   %u\n", (unsigned int) UINT_MAX);
    printf("ULONG_MAX   :   %lu\n", (unsigned long) ULONG_MAX);
    printf("USHRT_MAX   :   %d\n", (unsigned short) USHRT_MAX);

    return 0;
}
```

When you compile and execute the above program, it produces the following result on Linux:
```
CHAR_BIT    :   8
CHAR_MAX    :   127
CHAR_MIN    :   -128
INT_MAX     :   2147483647
INT_MIN     :   -2147483648
LONG_MAX    :   9223372036854775807
LONG_MIN    :   -9223372036854775808
SCHAR_MAX   :   127
SCHAR_MIN   :   -128
SHRT_MAX    :   32767
SHRT_MIN    :   -32768
UCHAR_MAX   :   255
UINT_MAX    :   4294967295
ULONG_MAX   :   18446744073709551615
USHRT_MAX   :   65535
```

## Floating-Point Types

The following table provide the details of standard floating-point types with storage sizes and value ranges and their precision:

Type | Storage size | Value range | Precision
--- | --- | --- | ---
float | 4 byte | 1.2E-38 to 3.4E+38 | 6 decimal places 
double | 8 byte | 2.3E-308 to 1.7E+308 | 15 decimal places
long double | 10 byte | 3.4E-4932 to 1.1E+4932 | 19 decimal places

The header file float.h defines macros that allow you to use these values and other details about the binary representation of real numbers in your programs. The following example prints the storage space taken by a float type and its range values:
```c
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <float.h>

int main(int argc, char** argv) {

    printf("Storage size for float : %d \n", sizeof(float));
    printf("FLT_MAX     :   %g\n", (float) FLT_MAX);
    printf("FLT_MIN     :   %g\n", (float) FLT_MIN);
    printf("-FLT_MAX    :   %g\n", (float) -FLT_MAX);
    printf("-FLT_MIN    :   %g\n", (float) -FLT_MIN);
    printf("DBL_MAX     :   %g\n", (double) DBL_MAX);
    printf("DBL_MIN     :   %g\n", (double) DBL_MIN);
    printf("-DBL_MAX     :  %g\n", (double) -DBL_MAX);
    printf("Precision value: %d\n", FLT_DIG );

    return 0;
}
```

When you compile and execute the above program, it produces the following result on Linux:
```
Storage size for float : 4 
FLT_MAX      :   3.40282e+38
FLT_MIN      :   1.17549e-38
-FLT_MAX     :   -3.40282e+38
-FLT_MIN     :   -1.17549e-38
DBL_MAX      :   1.79769e+308
DBL_MIN      :   2.22507e-308
-DBL_MAX     :  -1.79769e+308
Precision value: 6
```

## The `void` Type

The void type specifies that no value is available. It is used in three kinds of situations:

**Function returns as void**
- There are various functions in C which do not return any value.  This is stated as they return `void`. 
- A function with no return value has the return type as void.
- Example:
```c
void exit (int status);
```
**Function arguments as void** 
- There are various functions in C which do not accept any parameter. 
- A function with no parameter can accept a `void`.
- Example:
```c
int rand(void);
```
**Pointers to void**
- A pointer of type `void *` represents the address of an object, but not its type. 
- A memory allocation function returns a pointer to void which can be cast to any data type.
- Example:
```c
void *malloc( size_t size ); 
```

## Resources

- [Data Types in C - GeeksforGeeks](https://www.geeksforgeeks.org/data-types-in-c/)

## Sources

- [C Data Types - Tutorialspoint](https://www.tutorialspoint.com/cprogramming/c_data_types.htm)

[Back to README](README.md)