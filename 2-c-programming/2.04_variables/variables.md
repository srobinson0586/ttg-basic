# C - Variables

A variable is a name given to a storage area that our programs can manipulate. As discussed in the previous section, each variable in C has a specific type, which determines the size and layout of the variable's memory; the range of values that can be stored within that memory; and the set of operations that can be applied to the variable.

The name of a variable can be composed of letters, digits, and the underscore character. It must begin with either a letter or an underscore. Upper and lowercase letters are distinct because C is case-sensitive. Based on the basic types explained in the previous chapter, there will be the following basic variable types:

C programming language allows you to define various other types of variables, which we will cover in later sections like Enumeration, Pointer, Array, Structure, Union, etc. This section will focus only on basic variable types.

## Variable Definition in C

A variable definition tells the compiler where and how much storage to create for the variable. A variable definition specifies a data type and contains a list of one or more variables of that type as follows:
```
type variable_list;
```
- **type** must be a valid C data type including `char`, `w_char`, `int`, `float`, `double`, `bool`, or any user-defined object;
- **variable_list** may consist of one or more identifier names separated by commas. 

Example valid declarations:

```c
int    i, j, k; // declares and defines the variables i, j, and k; instructs the compiler to create the variables as type `int`.
char   c, ch;
float  f, salary;
double d;
```

## Variable Initialization in C

Variables can also be initialized (assigned an initial value) in their declaration. The initializer consists of an equal sign followed by a constant expression as follows:

```
type variable_name = value;
```

Examples:
```c
extern int d = 3, f = 5;    // declaration of d and f. 
int d = 3, f = 5;           // definition and initializing d and f. 
byte z = 22;                // definition and initializes z. 
char x = 'x';               // the variable x has the value 'x'.
```

For definition without an initializer: variables with static storage duration are implicitly initialized with NULL (all bytes have the value 0); the initial value of all other variables are undefined.

## Variable Declaration in C

A variable declaration provides assurance to the compiler that there exists a variable with the given type and name so that the compiler can proceed for further compilation without requiring the complete detail about the variable. A variable definition has its meaning at the time of compilation only, the compiler needs actual variable definition at the time of linking the program.

A variable declaration is useful when you are using multiple files and you define your variable in one of the files which will be available at the time of linking of the program. You will use the keyword **extern** to declare a variable at any place. Though you can declare a variable multiple times in your C program, it can be defined only once in a file, a function, or a block of code.

### Example

Try the following example, where variables have been declared at the top, but they have been defined and initialized inside the main function:

```c
#include <stdio.h>

// Variable declaration:
extern int a, b;
extern int c;
extern float f;

int main () {

   /* variable definition: */
   int a, b;
   int c;
   float f;
 
   /* actual initialization */
   a = 10;
   b = 20;
  
   c = a + b;
   printf("value of c : %d \n", c);

   f = 70.0/3.0;
   printf("value of f : %f \n", f);
 
   return 0;
}
```

When the above code is compiled and executed, it produces the following result:

```
value of c : 30
value of f : 23.333334
```

The same concept applies on function declaration where you provide a function name at the time of its declaration and its actual definition can be given anywhere else. For example:
```c
// function declaration
int func();

int main() {

   // function call
   int i = func();
}

// function definition
int func() {
   return 0;
}
```

## Resources

   - [C Variables and Constants - GeeksforGeeks](https://www.geeksforgeeks.org/variables-in-c)
   - [Learn-C.org - C Variables](https://www.learn-c.org/en/Variables_and_Types)

## Source

- [Tutorialspoint - C Variables and Constants](https://www.tutorialspoint.com/cprogramming/c_variables.htm)

[Back to README](README.md)