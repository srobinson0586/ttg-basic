# C Programming - Heap Arrays and Strings

## Heap Arrays

In C programming, the heap is a region of memory used for dynamic memory allocation. Heap memory is managed by the programmer and allows for the allocation and deallocation of memory at runtime. One way to use heap memory is through dynamic **heap arrays**, using functions like `malloc` or `calloc`, for arrays whose size can be determined at runtime. These dynamically allocated arrays are allocated on the program's heap memory, which is a larger and more flexible region of memory. Heap arrays are suitable for large or dynamically sized arrays and they have a longer lifetime than stack arrays as they exist until explicitly deallocated using `free()`.

Key differences between stack arrays and heap arrays:

- **Memory Location**: Stack arrays are allocated on the stack, while heap arrays are allocated on the heap.
- **Size**: Stack arrays have a fixed size determined at compile-time, while heap arrays can have a dynamic size determined at runtime.
- **Lifetime**: Stack arrays have a shorter lifetime, limited to the scope of the function in which they are declared, while heap arrays can have a longer lifetime, lasting until explicitly deallocated.
- **Efficiency**: Stack memory allocation and deallocation are generally faster than heap memory, but the stack has limited capacity.
- **Error Handling**: Heap memory allocation can fail, so it's important to check for NULL after allocating heap memory.

Here's an example of a heap array using dynamic memory allocation:
```c
#include <stdio.h>
#include <stdlib.h>

int main() {
    int *heapArray;
    int size;

    // Get the size of the array from the user
    printf("Enter the size of the array: ");
    scanf("%d", &size);

    // Allocate memory for the array on the heap
    heapArray = (int *)malloc(size * sizeof(int));

    // Check if memory allocation was successful
    if (heapArray == NULL) {
        printf("Memory allocation failed.\n");
        return 1; // Exit with an error code
    }

    // Initialize the array elements
    for (int i = 0; i < size; i++) {
        heapArray[i] = i * 10; // Set each element to 10 times its index
    }

    // Print the array elements
    printf("Heap Array Elements:\n");
    for (int i = 0; i < size; i++) {
        printf("%d ", heapArray[i]);
    }
    printf("\n");

    // Free the allocated memory
    free(heapArray);

    return 0;
}
```

The program prompts the user to enter the size of the array, allocates memory for the array on the heap, initializes the array elements, prints the array elements, and finally frees the allocated memory.

For example, if the user enters a size of 5, the output might look like this:

```
Enter the size of the array: 5
Heap Array Elements:
0 10 20 30 40
```

This output shows the elements of the heap array, where each element is initialized to 10 times its index. Keep in mind that freeing allocated memory using free() is crucial to prevent memory leaks.

## Heap Strings

Similarly, **heap strings** involve dynamic memory allocation on the heap in C programming. Heap strings are represented as dynamically allocated character arrays (**char\***) used to store and manipulate strings of characters.

Heap strings are useful in storing and working with variable-length strings like names, sentences, or any sequence of characters.  Like heap arrays, functions like **malloc()**, **calloc()**, and **free()** are used for dynamic memory allocation and deallocation, respectively.

Heap string example:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    char *heapString;

    // Allocate memory for the string
    heapString = (char *)malloc(20 * sizeof(char));

    // Check if memory allocation is successful
    if (heapString == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Input a string into the dynamically allocated memory
    printf("Enter a string (up to 19 characters): ");
    scanf("%19s", heapString);

    // Display the dynamically allocated string
    printf("Heap String: %s\n", heapString);

    // Free the dynamically allocated memory
    free(heapString);

    return 0;
}
```

If a user enters the string "DynamicString" when prompted, they would get the following output:
```
Enter a string (up to 19 characters): DynamicString
Heap String: DynamicString
```

In this example, the program dynamically allocates memory for a character array (string) on the heap, allows the user to input a string, displays the dynamically allocated string, and then frees the allocated memory using `free`. This approach is useful when you need to work with strings whose length may vary and want to manage memory dynamically at runtime.

### String Functions

While heap arrays can be manipulated based on the data type they hold, heap strings are often manipulated using string functions like strlen, strcpy, and strcat, discussed in the previous "Stack Strings" section.

Below is an example that demonstrates the use of `malloc`, `strlen`, `strcpy`, and `strcat` with heap strings:

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    // Allocate memory for two strings
    char *string1 = (char *)malloc(20 * sizeof(char));
    char *string2 = (char *)malloc(20 * sizeof(char));

    // Check if memory allocation is successful
    if (string1 == NULL || string2 == NULL) {
        fprintf(stderr, "Memory allocation failed\n");
        return 1;
    }

    // Input two strings
    printf("Enter the first string: ");
    scanf("%19s", string1);

    printf("Enter the second string: ");
    scanf("%19s", string2);

    // Use strlen, strcpy, and strcat
    int length1 = strlen(string1);
    printf("Length of string1: %d\n", length1);

    // Copy string2 into string1
    strcpy(string1, string2);
    printf("After strcpy, string1: %s\n", string1);

    // Concatenate "Concatenated" to string1
    strcat(string1, "Concatenated");
    printf("After strcat, string1: %s\n", string1);

    // Free the dynamically allocated memory
    free(string1);
    free(string2);

    return 0;
}
```

In this example, `strlen` is used to find the length of the first string, `strcpy` is used to copy the second string into the first one, and `strcat` is used to concatenate "Concatenated" to the first string.

Let's assume the user enters the first string as "Hello" and the second string as "World". The program will then output the length of the first string, copy the second string into the first one, and concatenate "Concatenated" to the first string:

```
Enter the first string: Hello
Enter the second string: World
Length of string1: 5
After strcpy, string1: World
After strcat, string1: WorldConcatenated
```

## Resources

- [Dynamic Memory Allocation - Geeksforgeeks](https://www.geeksforgeeks.org/dynamic-memory-allocation-in-c-using-malloc-calloc-free-and-realloc/)

## Sources


[Back to README](README.md)