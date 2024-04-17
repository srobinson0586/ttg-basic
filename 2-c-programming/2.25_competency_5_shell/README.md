# C Programming - Shell

[Back to Overview](../README.md)

JQR Addressed: Implement functionality of custom shell in C to demonstrate advanced concepts of C programming that include malloc/calloc, free, data structures, and logical program flow

Platform: Linux

Starter code: [Makefile](./Makefile), [shell.h](./shell.h), [shell.c](./shell.c), [main.c](./main.c), and [final_test.txt](./final_tests.txt)

Requirements: `gcc` and `valgrind` or `Visual Studio`

### Purpose

- This assignment will introduce you to memory management and data structures and expand upon your abilities to develop logical solutions using C.

- By the end of this competency, you should have a basic understanding of:
  - malloc/calloc
  - free
  - data structures
  - logical program flow

- Trainees will be expected to explain these concepts to the Training Lead or a qualified signer.

- This assignment is the basic building block for future competencies.

### Assignment

- Create a custom shell using C:
  - According to the ```man``` pages, implement the following shell commands (for `wc` and `cat`, you don't need to handle flags (e.g., `-l`) or multiple files in one command (e.g., `cat file1.txt file2.txt`)):
    - `wc`
    - `cat`
    - `exit`
  - Implement the following user-defined shell commands:
    - `student`
      - prompts the user to enter:
        1. student id
        2. student name
        3. hacker name
    - `student print`
      - prints information (ie student id, student name, and hacker name) for all students that have been added

- Must make use of a student structure
  - All instances of student structure must exist wholly on the heap
  - The data fields for student name and hacker name must exist wholly on the heap

- Must make use of a linked list to keep track of all students created with `student` shell command.

- Must indicate if user inputs unrecognized command.

- All allocated memory must be managed appropriately.

- The shell should run in a while loop until an `exit` option is selected by the user.
  - All allocated memory should be freed before exiting.

- Test your implementations by typing the following in the terminal:

    ```bash
    $ make
    ```

- Ensure you have the all of the given files in your current directory

- Rely on GDB to troubleshoot your program.

### Completion

- [ ] Header file with includes, defines, and function prototypes

- [ ] Use of valid function for getting user input: `fgets`, `getc`, `getchar`, `fgetc`, and `getline`

- [ ] A `student` structure containing the data: student id, student name, and hacker name

- [ ] All instances of `student` are dynamically allocated and freed

- [ ] Student id, student name, and hacker name are dynamically allocated and freed

- [ ] A linked list containing all students created

- [ ] Correct implementation of `wc` command

- [ ] Correct implementation of `cat` command

- [ ] Custom `student` command that prompts user for: student id, student name, and hacker name

- [ ] Custom `student print` command that prints all students created

- [ ] Indicates if user inputs an unrecognized command

- [ ] Indicates if user inputs ill-formatted command

- [ ] Program runs until user inputs `exit`

- [ ] All input tests in `final_tests.txt` pass with expected results

- [ ] Running `make` runs shell

- [ ] Program has no memory leaks

- [ ] Program has no warnings

[Back to Overview](../README.md)