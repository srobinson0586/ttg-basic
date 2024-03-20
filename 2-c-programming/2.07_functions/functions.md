# C Programming: Functions

A function is a group of statements that together perform a task. Every C program has at least one function, which is **main()**, and all the most trivial programs can define additional functions.

You can divide up your code into separate functions. How you divide up your code among different functions is up to you, but logically the division is such that each function performs a specific task.

A function **declaration** tells the compiler about a function's name, return type, and parameters. A function **definition** provides the actual body of the function.

The C standard library provides numerous built-in functions that your program can call. For example, **strcat()** to concatenate two strings, **memcpy()** to copy one memory location to another location, and many more functions.

A function can also be referred as a method or a sub-routine or a procedure, etc.

## `main()` Function


The `main()` function serves as the entry point for a C program. Its primary purpose is to provide a starting point for the execution of the program. When a C program is executed, the operating system or the C runtime environment looks for the `main()` function and starts executing the code from there. Here are the key purposes of the `main()` function:

1. **Program Initialization**: It allows you to set up any initial conditions, variables, or resources that your program needs before it begins executing its main logic. This can include initializing variables, opening files, and allocating memory.

1. **Program Logic**: The main logic of your program is defined within the `main()` function. It contains the sequence of statements and function calls that accomplish the desired task or functionality of your program.

1. **Program Termination**: When the `main()` function reaches its end (encounters a `return` statement or reaches the closing brace), the program terminates. It allows you to perform cleanup tasks, such as releasing allocated memory or closing open files before the program exits.

1. **Communication with the Operating System**: The `main()` function can return an integer value, which is typically used to indicate the program's exit status to the operating system. A return value of 0 usually signifies a successful execution, while non-zero values can indicate errors or exceptional conditions.

1. **Command-Line Arguments**: The `main()` function can accept command-line arguments, allowing you to pass information to the program when it starts. This enables flexibility in how the program behaves based on the arguments provided.

In summary, the `main()` function serves as the central control point for a C program, where the program's initialization, execution, and termination are managed. It plays a crucial role in determining the flow and behavior of the program and is required in every C program.


## Defining a Function

While you can write an entire C program with all its logic in the `main()` function, there are several compelling reasons to define and use separate functions instead of placing everything in `main()`.  Utilizing functions in C will improve code organization, readability, and maintainability while enabling code reuse and modularity. They are an essential tool for designing efficient and structured C programs.

The general form of a function definition in C programming language is as follows:
```
return_type function_name( parameter list ) {
   body of the function
}
```
A function definition in C programming consists of a _function header_ and a _function body_. Here are all the parts of a function:

- **Return Type** − A function may return a value. The **return_type** is the data type of the value the function returns. Some functions perform the desired actions without returning a value. In this case, the return_type is the keyword **void**. 
- **Function Name** − This is the actual name of the function. The function name and the parameter list together constitute the function signature.
- **Parameters** − A parameter is like a placeholder. When a function is invoked, you pass a value to the parameter. This value is referred to as an **argument**. The parameter list refers to the type, order, and number of the parameters of a function. Parameters are optional; that is, a function may contain no parameters.
- **Function Body** − The function body contains a collection of statements that define what the function does.
    
### Example

Given below is the source code for a function called `max()`. This function takes two parameters *num1* and *num2* and returns the maximum value between the two as an integer:
```c
/* function returning the max between two numbers */
int max(int num1, int num2) {

   /* local variable declaration */
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}
```

## Function Prototypes

A function **declaration** tells the compiler about a function name and how to call the function. The actual body of the function can be defined separately. When we declare a function without it's body, it is known as a function **prototype**. Function prototypes are often created in header (.h) files or at the top of source code files, while their definitions are created elsewhere.

A function declaration has the following parts:

>return_type function_name( parameter list );

For the above defined function `max()`, the function declaration is as follows:
```c
int max(int num1, int num2);
```

Parameter names are not important in function declaration as only their type is required, so the following is also a valid declaration:
```c
int max(int, int);
```

Function declaration is required when you define a function in one source file and you call that function in another file. In such case, you should declare the function at the top of the file calling the function.

## Calling a Function

While creating a C function, you give a definition of what the function has to do. To use a function, you will have to call that function to perform the defined task.

When a program calls a function, the program control is transferred to the called function. A called function performs a defined task and when its return statement is executed or when its function-ending closing brace is reached, it returns the program control back to the main program.

To call a function, you simply need to pass the required parameters along with the function name, and if the function returns a value, then you can store the returned value. For example:
```c
#include <stdio.h>
 
/* function declaration */
int max(int num1, int num2);
 
int main () {

   /* local variable definition */
   int a = 100;
   int b = 200;
   int ret;
 
   /* calling a function to get max value */
   ret = max(a, b);
 
   printf( "Max value is : %d\n", ret );
 
   return 0;
}

/* function returning the max between two numbers */
int max(int num1, int num2) {

   /* local variable declaration */
   int result;
 
   if (num1 > num2)
      result = num1;
   else
      result = num2;
 
   return result; 
}
```

We have kept `max()` along with `main()` and compiled the source code. While running the final executable, it would produce the following result:
```
Max value is : 200
```

## Function Arguments

If a function is to use arguments, it must declare variables that accept the values of the arguments. These variables are called the **formal parameters** of the function. Formal parameters behave like other local variables inside the function and are created upon entry into the function and destroyed upon exit.

While calling a function, there are two ways in which arguments can be passed to a function: *call by value* and *call by reference*

### Function Call By Value

The **call by value** method of passing arguments to a function copies the actual value of an argument into the formal parameter of the function. In this case, changes made to the parameter inside the function have no effect on the argument.

By default, C programming uses _call by value_ to pass arguments. In general, it means the code within a function cannot alter the arguments used to call the function. Consider the function `swap()` definition as follows:

```c
/* function definition to swap the values */
void swap(int x, int y) {

   int temp;

   temp = x; /* save the value of x */
   x = y;    /* put y into x */
   y = temp; /* put temp into y */
  
   return;
}
```

Now, let us call the function `swap()` by passing actual values as in the following example:

```c
#include <stdio.h>
 
/* function declaration */
void swap(int x, int y);
 
int main () {

   /* local variable definition */
   int a = 100;
   int b = 200;
 
   printf("Before swap, value of a : %d\n", a );
   printf("Before swap, value of b : %d\n", b );
 
   /* calling a function to swap the values */
   swap(a, b);
 
   printf("After swap, value of a : %d\n", a );
   printf("After swap, value of b : %d\n", b );
 
   return 0;
}
void swap(int x, int y) {

   int temp;

   temp = x; /* save the value of x */
   x = y;    /* put y into x */
   y = temp; /* put temp into y */
  
   return;
}
```

Put the above code in a single C file, compile and execute it, it will produce the following result:
```
Before swap, value of a : 100
Before swap, value of b : 200
After swap, value of a : 100
After swap, value of b : 200
```

It shows that there are no changes in the values, though they had been changed inside the function.

By default, C uses **call by value** to pass arguments. In general, it means the code within a function cannot alter the arguments used to call the function.

### Function Call By Reference

>Note: The call by reference method of calling a function requires an understanding of how pointers and memory addressing works in C. You may read through this section to get a brief idea of how call by reference works, but we suggest returning to this section after you have gone through the module on [pointers](../2.13_pointers/pointers.md).

The **call by reference** method of passing arguments to a function copies the address of an argument into the formal parameter. Inside the function, the address is used to access the actual argument used in the call. It means the changes made to the parameter affect the passed argument.

To pass a value by reference, argument pointers are passed to the functions just like any other value. So accordingly you need to declare the function parameters as pointer types as in the following function `swap()`, which exchanges the values of the two integer variables pointed to, by their arguments.
```c
/* function definition to swap the values */
void swap(int *x, int *y) {

   int temp;
   temp = *x;    /* save the value at address x */
   *x = *y;      /* put y into x */
   *y = temp;    /* put temp into y */
  
   return;
}
```

Let us now call the function `swap()` by passing values by reference as in the following example:

```c
#include <stdio.h>

int main () {

   /* local variable definition */
   int a = 100;
   int b = 200;
 
   printf("Before swap, value of a : %d\n", a );
   printf("Before swap, value of b : %d\n", b );
 
   /* calling a function to swap the values */
   swap(&a, &b);
 
   printf("After swap, value of a : %d\n", a );
   printf("After swap, value of b : %d\n", b );
 
   return 0;
}
void swap(int *x, int *y) {

   int temp;

   temp = *x; /* save the value of x */
   *x = *y;    /* put y into x */
   *y = temp; /* put temp into y */
  
   return;
}
```

Put the above code in a single C file, compile and execute it to produce the following result:

```
Before swap, value of a : 100
Before swap, value of b : 200
After swap, value of a : 200
After swap, value of b : 100
```

It shows that the change has reflected outside the function as well, unlike call by value where the changes do not reflect outside the function.

## Resources

- [C Functions - GeeksforGeeks](https://www.geeksforgeeks.org/c-functions)
- [Learn-C.org - C Functions](https://www.learn-c.org/en/Functions)

## Sources

- [TutorialsPoint - C Functions](https://www.tutorialspoint.com/cprogramming/c_functions.htm)

[Back to README](README.md)