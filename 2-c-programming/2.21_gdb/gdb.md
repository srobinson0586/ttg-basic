# C Programming - GDB (Gnu Debugger)

## Overview

GNU Debugger, commonly referred to as **GDB**, is the most popular debugger for Linux systems to debug C and C++ programs. A debugger is a program that runs other programs, allowing the user to exercise control over these programs, and to examine variables when problems arise.

GNU Debugger helps you in getting information about the following:
- If a core dump happened, then what statement or expression did the program crash on?
- If an error occurs while executing a function, what line of the program contains the call to that function, and what are the parameters?
- What are the values of program variables at a particular point during execution of the program?
- What is the result of a particular expression in a program?

### How GDB Debugs

GDB works by interfacing with the executable file of a program, allowing you to inspect and manipulate its runtime behavior. You may run the program up to a certain point, then stop and print out the values of certain variables at that point, or step through the program one line at a time and print out the values of each variable after executing each line.

GDB uses a simple command line interface and the syntax to start gdb is:

```bash
gdb ./compiled_c_code
```

When you compile your C program, you can include debugging information using the **-g** flag. This information includes details about source code lines, variable names, and other symbols. When you start GDB with your compiled program, GDB loads the executable and reads the debugging information. It then creates a mapping between the machine code and the corresponding source code. While you can use GDB to analyze executables without this information, including this when possible enhances GDB's ability to map machine code instructions back to your original source code and provide helpful context. 

Once loaded GDB allows you to examine the values of variables, inspect memory, and even modify variables during runtime. 

### Points to Note
- Even though GDB can help you in finding out memory leakage related bugs, but it is not a tool to detect memory leakages. Valgrind is a suitabe tool for this purpose.
- GDB cannot be used for programs that compile with errors and it does not help in fixing those errors.

### Installation

GDB should have been installed back in section 2.01.  This may be confirmed by running the following command which will output the installed version if found:

```bash
$ gdb --version
```

GEF also was installed in section 2.01.  To verify, run the following command which should result in a **gef➤** prompt: 

```bash
$ gdb -q
```

### GEF

GEF (GDB Enhanced Features) is a powerful extension for the GNU Debugger (GDB) that enhances its functionality and provides a more user-friendly interface for reverse engineering and debugging. GEF aims to make the debugging process more efficient and convenient.  Once installed it is automatically loaded when you start GDB.  

Features:

1. **User Interface Improvements:**
   - GEF enhances the GDB command-line interface with colorization and additional information to make it more visually appealing and user-friendly.
   - It provides a more intuitive prompt and helps organize information in a way that is easier to understand.

2. **Context-Sensitive Commands:**
   - GEF introduces context-sensitive commands that adapt to the current state of the program being debugged.
   - Commands are extended to provide information and interact with the program in a more meaningful way.

3. **Symbolic Debugging:**
   - GEF supports symbolic debugging by displaying source code alongside the assembly code, making it easier for developers to understand the flow of their programs.
   - It provides commands to set breakpoints based on function names, source lines, or memory addresses.

4. **Memory Inspection and Manipulation:**
   - GEF simplifies memory inspection and manipulation by introducing commands for examining and modifying memory contents.
   - It offers features such as searching for specific patterns in memory and displaying memory maps.

5. **Registers and Stack Analysis:**
   - GEF provides commands to analyze and manipulate registers and the call stack, helping developers understand the program's state at any given point.
   - It supports various formats for displaying register values and provides commands for stack navigation.

6. **Multi-Architecture Support:**
   - GEF is designed to work with multiple architectures supported by GDB, allowing users to seamlessly switch between them.

7. **Scripting Support:**
   - GEF supports Python scripting, enabling users to automate repetitive tasks and extend GDB functionality further.

8. **Plugins and Extensibility:**
   - GEF is extensible and allows users to create plugins to add custom features or integrate additional tools into the debugging environment.

### Basic GDB Commands:

GDB provides a large set of commands to inspect and manipulate the program during runtime. The following are the one used most frequently: 

- b main - Puts a breakpoint at the beginning of the program
- b - Puts a breakpoint at the current line
- b N - Puts a breakpoint at line N
- b +N - Puts a breakpoint N lines down from the current line
- b fn - Puts a breakpoint at the beginning of function "fn"
- d N - Deletes breakpoint number N
- info break - list breakpoints
- r - Runs the program until a breakpoint or error
- c - Continues running the program until the next breakpoint or error
- f - Runs until the current function is finished
- s - Runs the next line of the program
- s N - Runs the next N lines of the program
- n - Like s, but it does not step into functions
- u N - Runs until you get N lines in front of the current line
- p var - Prints the current value of the variable "var"
- bt - Prints a stack trace
- u - Goes up a level in the stack
- d - Goes down a level in the stack
- q - Exit gdb

## Breakpoints and Watchpoints

In GDB, setting breakpoints and watchpoints are crucial techniques for controlling program execution and monitoring variable changes during debugging. Both help you gain control over the debugging process, allowing you to inspect and analyze your program's behavior at specific locations or when certain conditions are met.

### Setting Breakpoints:

A breakpoint is a designated point in your code where the program will pause its execution, allowing you to inspect the program's state at that specific point. Here's how you set breakpoints in GDB:

1. **Setting a Breakpoint at a Line:**
   To set a breakpoint at a specific line in your source code, use the `break` command followed by the file name and line number:

   ```bash
   (gdb) break filename.c:line_number
   ```

   For example:

   ```bash
   (gdb) break example.c:10
   ```

2. **Setting a Breakpoint at a Function:**
   You can also set a breakpoint at the beginning of a specific function:

   ```bash
   (gdb) break function_name
   ```

   For example:

   ```bash
   (gdb) break main
   ```

3. **Disabling and Enabling Breakpoints:**
   You can disable or enable breakpoints using the `disable` and `enable` commands:

   ```bash
   (gdb) disable breakpoints  # Disable all breakpoints
   (gdb) enable breakpoints   # Enable all breakpoints
   ```

### Setting Watchpoints:

Watchpoints are used to monitor changes to a specific variable or memory address. When the value of the watched variable changes, the program pauses, allowing you to inspect the changes. Here's how you set watchpoints:

1. **Setting a Watchpoint for a Variable:**
   Use the `watch` command followed by the variable name:

   ```bash
   (gdb) watch variable_name
   ```

   For example:

   ```bash
   (gdb) watch counter
   ```

2. **Setting a Watchpoint for an Expression:**
   You can also set watchpoints for more complex expressions:

   ```bash
   (gdb) watch expression
   ```

   For example:

   ```bash
   (gdb) watch array[i]
   ```

3. **Disabling and Enabling Watchpoints:**
   Similar to breakpoints, you can disable or enable watchpoints using the `disable` and `enable` commands:

   ```bash
   (gdb) disable watchpoints  # Disable all watchpoints
   (gdb) enable watchpoints   # Enable all watchpoints
   ```

4. **Deleting Watchpoints:**
   To remove a watchpoint, use the `delete` command followed by the watchpoint number:

   ```bash
   (gdb) delete watch watchpoint_number
   ```

### Example:

```bash
(gdb) break main          # Set a breakpoint at the beginning of main
(gdb) run                 # Start the program
(gdb) watch variable_name # Set a watchpoint for a variable
(gdb) continue            # Continue execution
```

These commands illustrate setting a breakpoint at the beginning of the `main` function, setting a watchpoint for a variable, and continuing program execution until the watchpoint is hit.

## Navigating Stack Frames

GDB operates on the concept of stack frames, representing different levels of function calls in your program. You can move between stack frames to inspect local variables in different functions.

From previous sections you may recall that the call stack is a region of memory used to manage function calls and returns. Each time a function is called, a new stack frame is created on top of the call stack to store local variables, return addresses, and other information related to the function call.

Here's how GDB uses and interacts with stack frames during a debugging session:

1. **Current Stack Frame:**
   When you start debugging a program in GDB, you are initially in the context of the outermost or top-level stack frame, which is usually the `main` function.

2. **Examining Local Variables:**
   GDB allows you to examine the values of local variables within the current stack frame. For example, you can use the `print` command to inspect the values of variables within the current function.

   ```bash
   (gdb) print variable_name
   ```

3. **Switching Stack Frames:**
   As your program executes and calls other functions, you can switch between stack frames to inspect variables in different functions. The `up` and `down` commands are used to move up and down the call stack, respectively.

   ```bash
   (gdb) up    # Move to the calling function's stack frame
   (gdb) down  # Move back to the previous stack frame
   ```

4. **Examining Arguments:**
   You can examine the arguments of the current function by using the `info args` command.

   ```bash
   (gdb) info args
   ```

5. **Examining Backtrace:**
   The `bt` (backtrace) command provides a complete backtrace of the call stack, showing the sequence of function calls that led to the current point in the program.

   ```bash
   (gdb) bt
   ```

6. **Setting Breakpoints in Specific Frames:**
   GDB allows you to set breakpoints within specific stack frames. This can be useful when you want to break only when a particular function is called.

   ```bash
   (gdb) break function_name
   ```

## Debugging Examples

### Divide by Zero
This example demonstrates how you would capture an error that is happening due to an exception raised while dividing by zero.

1. Source Code; save as crash.c

```c
#include <stdio.h>

int divint(int, int);

int main() {
    int x = 5, y = 2;
    printf("%d\n", divint(x, y));

    x = 3; y = 0;
    printf("%d\n", divint(x, y));

    return 0;
}

int divint(int a, int b) {
    return a / b;
} 
```
2. Compile, with debugging enabled.
```bash 
$gcc -g crash.c -o crash
```

3. To debug the problem, start gdb debugger at the command prompt

```bash
$gdb crash 
# Gdb prints summary information and then the gef prompt
```

4. Run the program from within GDB
```bash
gef➤  r
```

Output (some details may vary, such as memory addresses)
```bash
Starting program: crash 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
2

Program received signal SIGFPE, Arithmetic exception.
0x00005555555551d4 in divint (a=0x3, b=0x0) at crash.c:16
16	    return a / b;
```
In this case the program crashed and **gef** prints out a lot of information.  Scroll up to find the relevant information as seen in the out put above. In particular, it crashed trying to execute line 16 of crash.c.  The function parameters 'a' and 'b' had values 3 and 0 respectively.  

Note that **gef** automatically dumps information about the state of stack and all registers. This information can be critical when debugging more complex issues. 

3.  Additional insights may be obtain by executing the following commands (Explanations in comments):

```bash
gef➤  l
11	
12	    return 0;
13	}
14	
15	int divint(int a, int b) {
16	    return a / b;
17	}
# l is short for 'list'.  Useful for seeing the context of 
# the crash, lists source code lines around 16 of crash.c 

gef➤  where
/#0  0x00005555555551d4 in divint (a=0x3, b=0x0) at crash.c:16
/#1  0x00005555555551a5 in main () at crash.c:10
# Equivalent to 'bt' or backtrace.  Produces what is known 
# as a 'stack trace'.  Read this as follows:  The crash occurred 
# in the function divint at line `16` of crash.cc.  This, in turn, 
# was called from the function main at line 10 of crash.cc 

gef➤  up
/#1  0x00005555555551a5 in main () at crash.c:10
10	    printf("%d\n", divint(x, y));
# Move from the default level '0' of the stack trace up one level 
# to level 1.

gef➤  list
5	int main() {
6	    int x = 5, y = 2;
7	    printf("%d\n", divint(x, y));
8	
9	    x = 3; y = 0;
10	    printf("%d\n", divint(x, y));
11	
12	    return 0;
13	}
14	
# list now lists the source code lines near line 10 of crash.cc 

gef➤  p x
$1 = 0x3
# print the value of the local (to main) variable x 
```

### Uninitialized Pointer

1. Source Code; save as crash2.c

```c
#include <stdio.h>

void setint(int*, int);

int main() {
    int a;
    setint(&a, 10);
    printf("%d\n", a);

    int* b;
    setint(b, 10);
    printf("%d\n", *b);

    return 0;
}

void setint(int* ip, int i) {
    *ip = i;
}
```

2. Compile with debugging enabled using the same method as the previous example.  When you run this program on your linux machine, it will produce the following result:

```bash
10
Segmentation fault (core dumped)
```

3. Debug using GDB:
```bash
gef➤  r

Starting program: /home/hm/crash2 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".
10

Program received signal SIGSEGV, Segmentation fault.
0x000055555555520c in setint (ip=0x0, i=0xa) at crash2.c:18
18	    *ip = i;

# Truncated GEF dump; relevant details are in the first 10 lines of output for this example. 

gef➤  where
/#0  0x000055555555520c in setint (ip=0x0, i=0xa) at crash2.c:18
/#1  0x00005555555551bf in main () at crash2.c:11
```

Unfortunately, the program will not crash in either of the user-defined functions, main or setint, so there is no useful trace or local variable information. In this case, it may be more useful to single-step through the program.

```bash
gef➤  b main
Breakpoint 1 at 0x555555555175: file crash2.c, line 5.

gef➤  r
Starting program: /home/hm/crash2 
[Thread debugging using libthread_db enabled]
Using host libthread_db library "/lib/x86_64-linux-gnu/libthread_db.so.1".

Breakpoint 1, main () at crash2.c:5
5	int main() {

# Truncated GEF dump

gef➤  n
7	    setint(&a, 10);

# n = next, runs one line of the program
gef➤  n
8	    printf("%d\n", a);

gef➤  n
10
11	    setint(b, 10);

gef➤  s
setint (ip=0x0, i=0xa) at crash2.c:18
18	    *ip = i;
# s = step, is like next, but it will step into functions. 
# In this case the function stepped into is setint.

gef➤  p ip
$3 = (int *) 0x0

gef➤  p *ip
Cannot access memory at address 0x0
```

The value of *ip is the value of the integer pointed to by ip. In this case, it is an unusual value of 0x0. The problem in this case is that the pointer was never properly initialized. By pure luck, the process of assigning a value to *ip does not crash the program, but it creates some problem that crashes the program when it finishes

## Resources

- [GDB: The GNU Project Debugger - Official website of GNU Debugger](http://sourceware.org/gdb/)
- [GNU Debugger - GNU Debugger at Wikipedia](http://en.wikipedia.org/wiki/GDB)
- [How to Debug Using GDB - Another tutorial for GDB](http://cs.baylor.edu/~donahoo/tools/gdb/tutorial.htm)

## Sources
- [GNU Debugger Tutorial](https://www.tutorialspoint.com/gnu_debugger)