# C Programming - Dynamic Memory

This sections focuses in on dynamic memory management in C. The C programming language provides several functions for memory allocation and management. These functions can be found in the **<stdlib.h>** header file.

Function | Description
---| ---
**void \*calloc(int num, int size);** | This function allocates an array of **num** elements each of which size in bytes will be **size** and intializes the memory to 0.
**void free(void \*address);** | This function releases a block of memory block specified by address.
**void \*malloc(size\_t size);** | This function allocates an array of **num** bytes and leave them uninitialized.
**void \*realloc(void \*address, int newsize);** | This function re-allocates memory extending it upto **newsize**.

## Allocating Memory Dynamically

While programming, if you are aware of the size of an array, then it is easy and you can define it as an array. For example, to store a name of any person up to a maximum of 100 characters, so you can define something as follows −

```c
char name[100];
```

But now let us consider a situation where you have no idea about the length of the text you need to store, for example, you want to store a detailed description about a topic. Here we need to define a pointer to character without defining how much memory is required and later, based on requirement, we can allocate memory as shown in the below example:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

   char name[100];
   char *description;

   strcpy(name, "Zara Ali");

   /* allocate memory dynamically */
   description = malloc( 200 * sizeof(char) );
	
   /* check that dynamic memory was successfully allocated */
   if( description == NULL ) {
      fprintf(stderr, "Error - unable to allocate required memory\\n");
   }

   /* store a string in dynamically allocated memory */
   strcpy( description, "Zara ali a DPS student in class 10th");
   
   printf("Name = %s\\n", name );
   printf("Description: %s\\n", description );
}
```

When the above code is compiled and executed, it produces the following result:

```
Name = Zara Ali
Description: Zara ali a DPS student in class 10th
```

The same program can be written using `calloc` by replacing **malloc* with **calloc** as follows:

```c
calloc(200, sizeof(char));
```

Using functions for dynamic memory allocation gives us a greater sense of control over sizing and resizing memory. This is unlike stack arrays where once the size defined, you cannot dynamically change it.

### Resizing and Releasing Memory

When your program exits or terminates, the operating system will typically automatically release all the memory allocated by your program.  However it is a good practice to call the function **free()** when the program does not need the memory anymore to prevent potential memory leaks.

Alternatively, you can increase or decrease the size of an allocated memory block by calling the function **realloc()**. Below is the above program making use of **realloc()** and **free()** functions:


```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {

   char name[100];
   char *description;

   strcpy(name, "Zara Ali");

   /* allocate memory dynamically */
   description = malloc( 30 * sizeof(char) );
	
   if ( description == NULL ) {
      fprintf(stderr, "Error - unable to allocate required memory\\n");
   } else {
      strcpy( description, "Zara ali a DPS student.");
   }
	
   /* suppose you want to store bigger description */
   description = realloc( description, 100 * sizeof(char) );
	
   if ( description == NULL ) {
      fprintf(stderr, "Error - unable to allocate required memory\\n");
   } else {
      strcat( description, "She is in class 10th");
   }
   
   printf("Name = %s\\n", name );
   printf("Description: %s\\n", description );

   /* release memory using free() function */
   free(description);
}
```

When the above code is compiled and executed, it produces the following result.

```
Name = Zara Ali
Description: Zara ali a DPS student.She is in class 10th
```

If you try the above example without re-allocating extra memory, the **strcat()** function will give an error due to lack of available memory in **description**.

## Typecasting

In C programming, the term **typecasting** refers to the conversion of a variable from one data type to another. For example, if you want to store a `long` value into a simple integer then you can type cast `long` to `int`. Typecasting can be explicit or implicit, and it is often necessary when you want to perform operations involving variables of different types. You can convert the values from one type to another explicitly using the **cast operator** as follows:

```
(type_name) expression
```

Consider the following example where the cast operator causes the division of one integer variable by another to be performed as a floating-point operation:

```c 
#include <stdio.h>

main() {

   int sum = 17, count = 5;
   double mean;

   mean = (double) sum / count;
   printf("Value of mean : %f\\n", mean );
}

When the above code is compiled and executed, it produces the following result −

Value of mean : 3.400000

It should be noted here that the cast operator has precedence over division, so the value of **sum** is first converted to type **double** and finally it gets divided by count yielding a double value.

Type conversions can be implicit which is performed by the compiler automatically, or it can be specified explicitly through the use of the **cast operator**. It is considered good programming practice to use the cast operator whenever type conversions are necessary.
```

### Integer Promotion

Integer promotion is the process by which values of integer type "smaller" than **int** or **unsigned int** are converted either to **int** or **unsigned int**. Consider an example of adding a character with an integer −

```c
#include <stdio.h>

main() {

   int  i = 17;
   char c = 'c'; /\* ascii value is 99 \*/
   int sum;

   sum = i + c;
   printf("Value of sum : %d\\n", sum );
}
```

When the above code is compiled and executed, it produces the following result −

```
Value of sum : 116
```

Here, the value of sum is 116 because the compiler is doing integer promotion and converting the value of 'c' to ASCII before performing the actual addition operation.

### Usual Arithmetic Conversion

The **usual arithmetic conversions** are implicitly performed to cast their values to a common type. The compiler first performs _integer promotion_; if the operands still have different types, then they are converted to the type that appears highest in the following hierarchy −

![Usual Arithmetic Conversion](../images/usual_arithmetic_conversion.png)

The usual arithmetic conversions are not performed for the assignment operators, nor for the logical operators `&&` and `||`. Let us take the following example to understand the concept −

```c
#include <stdio.h>

main() {

   int  i = 17;
   char c = 'c'; /* ascii value is 99 */
   float sum;

   sum = i + c;
   printf("Value of sum : %f\n", sum );
}
```

When the above code is compiled and executed, it produces the following result:
```
Value of sum : 116.000000
```

Here, it is simple to understand that first 'c' gets converted to integer, but as the final value type is **double**, usual arithmetic conversion applies and the compiler converts 'i' and 'c' into **float** and adds them yielding a float result.

## Typecasting memory

In the context of C programming, **typecasting memory** refers to the act of interpreting the contents of a block of memory as if it were of a different data type. This is commonly done by using pointers and casting them to a different type.

Here's an example to illustrate typecasting memory using pointers:

```c
#include <stdio.h>

int main() {
    int integerValue = 42;

    // Using a pointer to access the memory location of the integer
    int *intPointer = &integerValue;

    // Typecasting the pointer to interpret the memory as a char pointer
    char *charPointer = (char *)intPointer;

    // Accessing the memory as a char (1 byte)
    for (int i = 0; i < sizeof(int); i++) {
        printf("Byte %d: %d\n", i, charPointer[i]);
    }

    return 0;
}
```

When compiled and executed you will get the following result:

```
Byte 0: 42
Byte 1: 0
Byte 2: 0
Byte 3: 0
```
In this example, an integer variable `integerValue` is stored in memory. The program then creates a pointer (`intPointer`) to the memory location of the integer. Subsequently, a new pointer (`charPointer`) is created by typecasting the original pointer to a char pointer.

When you iterate through the memory using the char pointer, it treats each byte as a separate character, effectively allowing you to inspect the individual bytes that make up the integer. This kind of manipulation is often used in low-level programming or when dealing with binary data.

Here's how the output is interpreted:

- Byte 0: Represents the least significant byte of the integer, which contains the value 42.
- Byte 1-3: Represent the remaining three bytes of the integer, which are zero because the integer value 42 does not use these bytes in this particular system's little-endian representation.

It's important to note that the output may vary on different systems, especially if they use a big-endian representation or have a different size for an integer. The key takeaway is that typecasting memory allows you to inspect the individual bytes making up a variable, which can be useful in certain low-level programming scenarios. Also typecasting memory should be done with caution, as it can lead to undefined behavior if misused. The alignment and **endianness** of the system can also affect the interpretation of the memory contents.

## Endianness

Endianness refers to the byte order in which multibyte data types are stored in computer memory and will vary depending one the CPU architecture (i.e. x86, ARM). There are two common types of endianness: 

- **Big-Endian:**
   In a big-endian system, the most significant byte (the byte containing the highest-order bits) is stored at the lowest memory address. Subsequent bytes follow in increasing order of significance.
- **Little-Endian:**
   In a little-endian system, the least significant byte (the byte containing the lowest-order bits) is stored at the lowest memory address. Subsequent bytes follow in increasing order of significance.

Here's an example showing the representation of number in both order types:

```c
#include <stdio.h>

// Function to print the bytes of an integer
void printBytes(unsigned int num) {
    unsigned char *bytePtr = (unsigned char *)&num;

    printf("Original Integer: %u\n", num);

    printf("Little-Endian Representation: ");
    for (int i = 0; i < sizeof(num); i++) {
        printf("%02x ", bytePtr[i]);
    }
    printf("\n");

    printf("Big-Endian Representation: ");
    for (int i = sizeof(num) - 1; i >= 0; i--) {
        printf("%02x ", bytePtr[i]);
    }
    printf("\n\n");
}

int main() {
    // Example with the number 123456789
    unsigned int exampleNumber = 123456789;

    printf("Example with the number %u:\n", exampleNumber);
    printBytes(exampleNumber);

    return 0;
}
```

The output will show the original integer and its byte representation in both little-endian and big-endian formats:
```
Example with the number 123456789:
Original Integer: 123456789
Little-Endian Representation: 15 cd 5b 07
Big-Endian Representation: 07 5b cd 15
```

In this output, you can see that the little-endian representation starts with the least significant byte (`15`) at the lowest memory address, while the big-endian representation starts with the most significant byte (`07`) at the lowest memory address. The individual bytes are displayed in hexadecimal format.

## Resources

- [Dynamic Memory Allocation in C](https://www.youtube.com/watch?v=Dn87Bna23TQ)
- [Type Conversion in C | Implicit and Explicit Type Conversion](https://www.youtube.com/watch?v=xi2wf0Zy2Y4)
- [Different pointer types - Typecasting pointers of different types](https://www.youtube.com/watch?v=38khfegkGPU)
- [Endianness Explained With an Egg](https://www.youtube.com/watch?v=NcaiHcBvDR4)

## Sources

- [C Memory Management - Tutorialspoint](https://www.tutorialspoint.com/cprogramming/c_memory_management.htm)
- [C Typecasting - Tutorialspoint](https://www.tutorialspoint.com/cprogramming/c_type_casting.htm)

[Back to README](README.md)