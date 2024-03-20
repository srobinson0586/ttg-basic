2.00_overview
2.01_tools
2.02_basic_syntax
2.03_variables_data_types
CONSTANTS??
2.04_operators
2.05_conditionals
2.06_functions_1 #STACK reference?
2.07_competency_1_fizzbuzz
2.08_stack_arrays
2.09_stack_strings
2.10_loops
2.11_competency_2_scores
###STACK
2.12_pointers 
2.13_dynamic_memory
2.14_heap_arrays_strings
2.15_file_io
2.16_user_input
2.17_functions_2
2.18_valgrind
2.19_competency_3a_shell
2.20_structs
2.21_linked_lists
2.22_competency_3b_shell
2.23_gdb
2.24_makefiles
2.25_competency_4_madlib
supplementals
supplementals/2.26_signals
supplementals/2.27_enums
supplementals/2.28_mutex
supplementals/2.29_rollover_overflow
supplementals/2.30_recursion

1.00 Overview
    - General information about C
2.01 Tools
    - manpages
    - Environment (Ubuntu dev env, vxcode extensions)
    - simple compilation (the most basic gcc)
    - Reading library resources???
2.02 Basic Syntax
    - #include standard libraries
    - header files
    - int main()
    - Styling (comments, where to declare variables, blocks, semicolons, keywords, curly braces)
    - printf() for very basic output messages
2.03 Variables and Types
    - char, int, short, long, float, double, unsigned (sizes in bytes, everything is bytes)
    - #define
    - printf() directives (%d, %c, %i, %x, etc.) (print debugging)
2.04 Operators
    - Standard arithmetic operators (+, -, *, /, %)
    - Bitwise operators (<<, >>)
    - Assignment operators (++, --, -=, +=, *=, /=)
    - Order of operations
    - <math.h> functions (pow(), sqrt(), ceil(), floor().) (changing linker flag for math.h)
2.05 Conditionals
    - Conditional operators
    - 'if' statements
    - Switch statements
2.06 Functions
    - Prototypes
    - Return values
    - Parameters and arguments

--- Comptency 1 FizzBuzz ---

2.08 Stack-based Arrays
    - Creating an array
    - Accessing elements of an array directly
    - What happens when you try to access out-of-bounds memory
2.09 Stack-based Strings
    - Declaration and assignment (using char[])
    - Null-termination (importance of knowing string boundaries)
    - <string.h> functions like strlen() and strcmp()
    - printf() directive for strings
    - Read only strings
2.10 Loops
    - For and while loops
    - Do while
    - Iterating through each element of an array or string
        - One example of iterating through a 2-D array
    - A forever loop (while or zoidberg)
    - Reinforcement of conditional operators
    - breaks
    - continues

--- Competency 2 Array of scores; find min, max, average, etc. ---

2.12 Pointers
    - Declaring a pointer
    - Dereferencing
    - Using '&' and '*'
    - Pointers to pointers (**)
2.13 Dynamic Memory
    - endianess
    - malloc()
    - calloc()
    - reallocarray()
    - typecasting memory
    - free
2.14 Heap-based Arrays and Strings
    - strcat(), strcpy(), strdup(), memcpy(), strtok(), strstr()
2.15. File I/O
    - Descriptors (STDIN, STDOUT, STDERR are all just file desciptors)
    - Open/close
    - Read/write
2.16 User Input
    - getline() (Application to create own getline)
    - scanf()
    - fgets()
    - misc
2.17 Functions Part 2
    - Pass by reference/working with pointers
    - Function pointers
2.18 Valgrind
    - Understanding output
    - Tracing the error stack
    - Valgrind cheat sheet

--- Competency 3a Shell Part 1 ---

2.20 Structs
    - Struct definitions (typedef)
    - Accessing struct fields
    - Offsetof
2.21 Linked Lists
    - Singly linked lists
    - Doubly linked lists
    - Circular???

--- Competency 3b Shell Part 2 ---

2.23 GDB
    - GDB cheat sheet
    - Setting breakpoints
    - Stepping through code
2.24 Makefiles
    - make
    - Makefile syntax

--- Competency 4 Madlib with Trainee Supplied Makefile ---

Supplementals
    - Signals
    - Enums
    - Overflow/Underflow
    - Mutex
    - Unions