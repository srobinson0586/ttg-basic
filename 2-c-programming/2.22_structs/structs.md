# C Programming - Structs

## Overview
A struct (short for structure) is a user-defined data type that allows you to group together variables of different data types under a single name. It is used to create more complex data structures, representing entities in your program in a way that makes sense and is easier to manage. 

Key reasons why you might use structs in your C programs:

1. **Grouping Related Data:**
   - Structs allow you to group different types of variables together under one name. This is particularly useful when you have a set of related data that needs to be treated as a single unit.

2. **Organizing Data:**
   - When dealing with entities that have multiple attributes or properties (e.g., a person with a name, age, and height), structs help organize the data in a logical and structured manner.

3. **Improving Code Readability:**
   - By encapsulating related data within a struct, your code becomes more readable and self-explanatory. Structs provide a way to represent real-world entities in your program, making the code more intuitive and easier to understand.

4. **Simplifying Function Parameters:**
   - When a function needs to work with multiple related parameters, passing a struct as a parameter simplifies the function signature and improves code maintainability.

5. **Creating Data Structures:**
   - Structs are fundamental for building more complex data structures, such as linked lists, trees, and queues. They provide a way to define the structure of the elements within these data structures.

6. **Memory Efficiency:**
   - Structs allow you to group related data together in memory, potentially improving cache locality and overall memory efficiency.

Consider a simple example of representing a point in 2D space using a struct:

```c
struct Point {
    int x;
    int y;
};
```

With this struct, you can create variables representing points:

```c
struct Point p1 = {3, 5};
struct Point p2 = {-1, 7};
```

Now, each point is a single entity with both `x` and `y` coordinates, making it easier to work with and manipulate related data.

## Declaring a Struct

To declare a struct, you use the `struct` keyword followed by the name of the structure. For example:

```c
// Declaration of a struct named 'Person'
struct Person {
    char name[50];
    int age;
    float height;
};
```

In this example, we've defined a struct named `Person` that has three members: a character array `name`, an integer `age`, and a floating-point number `height`.

### Creating Struct Variables

Once you've declared a struct, you can create variables of that type:

```c
// Creating a variable of type 'Person'
struct Person person1;
```

### Accessing Struct Members

You can now access the members of a struct using the dot (`.`) operator:

```c
// Assigning values to struct members
strcpy(person1.name, "John Doe");
person1.age = 25;
person1.height = 5.9;

// Accessing and printing struct members
printf("Name: %s\n", person1.name);
printf("Age: %d\n", person1.age);
printf("Height: %.2f\n", person1.height);
```

### Initializing Structs

You can also initialize a struct at the time of declaration:

```c
struct Person person2 = {"Jane Doe", 30, 5.6};
```

### Arrays of Structs

It is also possible to create arrays of structs:

```c
struct Person people[3] = {
    {"Alice", 22, 5.4},
    {"Bob", 28, 6.0},
    {"Charlie", 35, 5.8}
};
```

### Passing Structs to Functions

Additionally you can pass structs to functions as arguments:

```c
void printPerson(struct Person p) {
    printf("Name: %s\n", p.name);
    printf("Age: %d\n", p.age);
    printf("Height: %.2f\n", p.height);
}

// Call the function with a struct variable
printPerson(person1);
```

## Pointers to Structs

Using pointers to structs allows for more efficient memory usage and manipulation of data, especially when dealing with dynamic memory allocation or passing structs to functions.

Pointers to structs in C allow you to work with structs in a dynamic and flexible manner. By using pointers, you can manipulate the data within a struct directly in memory, and you can pass structs efficiently between functions.

### Declaring a Struct

Let's consider a simple struct representing a person:

```c
struct Person {
    char name[50];
    int age;
    float height;
};
```

### Declaring a Pointer to a Struct

To declare a pointer to a struct, you use the `struct` keyword followed by the struct's name and an asterisk `*`. Here's an example:

```c
struct Person *personPtr;
```

### Allocating Memory for a Struct

Before using a pointer to a struct, you need to allocate memory for the struct. This is often done using dynamic memory allocation functions like `malloc` or `calloc`. For example:

```c
struct Person *personPtr = (struct Person *)malloc(sizeof(struct Person));
```

This allocates enough memory to store a `struct Person` and returns a pointer to that memory.

### Accessing Struct Members via Pointers

You can access struct members through a pointer using the arrow operator (`->`). For instance:

```c
// Assigning values through a pointer
strcpy(personPtr->name, "John Doe");
personPtr->age = 25;
personPtr->height = 5.9;
```

### Passing Pointers to Structs to Functions

When you pass a pointer to a struct to a function, you can modify the original struct within the function. This is more efficient than passing the entire struct by value. Here's an example function that takes a pointer to a struct:

```c
void printPerson(struct Person *ptr) {
    printf("Name: %s\n", ptr->name);
    printf("Age: %d\n", ptr->age);
    printf("Height: %.2f\n", ptr->height);
}

// Call the function with a pointer to a struct
printPerson(personPtr);
```

### Freeing Allocated Memory

If you allocate memory for a struct using `malloc` or similar functions, it's crucial to free that memory when you're done with it to prevent memory leaks:

```c
free(personPtr);
```

### Full Example Using Pointers to Structs

```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Person {
    char name[50];
    int age;
    float height;
};

int main() {
    // Allocate memory for a struct
    struct Person *personPtr = (struct Person *)malloc(sizeof(struct Person));

    // Assign values through a pointer
    strcpy(personPtr->name, "John Doe");
    personPtr->age = 25;
    personPtr->height = 5.9;

    // Access and print values through a pointer
    printf("Name: %s\n", personPtr->name);
    printf("Age: %d\n", personPtr->age);
    printf("Height: %.2f\n", personPtr->height);

    // Free allocated memory
    free(personPtr);

    return 0;
}
```