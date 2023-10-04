# Introduction to Section 1: Python


## JQR Section 1 Overview

This is Section 1 in the NCWDG JQR, where new Computer Network Operations (CNO) developers go from a Python Zero to a Python Hero. The section is structured in a way that first teaches students the basics of a specific topic using Markdown files in every folder, known as a **learning** Module. The learning modules then test students' knowledge by having them complete python challenges (`application.py`). After several modules, or topics, their combined use is tested in the form of a **competency** module.

There are 7 total competency modules. Each of them attempts to challenge the student more than the basic application challenges in the learning modules preceding it. All coding challenges are graded using the `test_application.py` script in each directory. All the students (and graders) must do to test the code is run `pytest` in the directory. `pytest` setup is covered in [1.01_environment](../1.01_environment/environment.md).

### Table of Contents

|     Section    |   Brief   |
-----------------|-----------|
| [1.00 Overview](../1.00_overview/README.MD)  | Provides the overview for the entire section |
| [1.01 Environment](../1.01_environment/README.md) | Instructs student on `python` and `pytest` setup | 
| [1.02 Basic Syntax](../1.02_basic_syntax/README.md)  | Executing first python code and following basic python rules | 
| [1.03 Variable Types](../1.03_variable_types/README.md)  | Basic python Data Types |
| [1.04 Operators](../1.04_operators/README.md)  | Overview of python Arithmetic, Comparison, Assignment, Bitwise, Membership, Identity, and Logical operator types | 
| [1.05 Conditionals](../1.05_conditionals/README.md) | Intro to python `if`, `elif`, and `else` statements |
| [1.06 Loops](../1.06_loops/README.md)  | Intro to `while` loops, `for` loops, and loop control statements |
| [1.07 Debugging](../1.07_debugging/README.md)  | Overview of print statement debugging and the Python Debugger |
| **[1.08 Competency 1: FizzBuzz](../1.08_competency_1_fizzbuzz/README.md)**  | The student will implement the `fizzbuzz` function to demonstrate knowledge of basic programming concepts like arithmetic operations, conditional statements, and loops  |
| [1.09 Numbers](../1.09_numbers/README.md)  | Covers Python's numerical types, truthiness of numbers, and introduces the `math` module |
| [1.10 Strings](../1.10_strings/README.md)  | Information about strings including access, modification, truthiness, string functions, and string types |
| [1.11 Typecasting](../1.11_typecasting/README.md)  | Overview on getting variables of different types to work together | 
| [1.12 Lists Tuples and Sets](../1.12_lists_tuples_and_sets/README.md)  | Intro to the popular sequence objects and best use cases |
| [1.13 Dictionaries](../1.13_dictionaries/README.md)  | A quick run down on python dictionaries and their most important features |
| **[1.14 Competency 2: Decryption](../1.14_competency_2_decryption/README.md)**  | Implement a Vigenere cipher, a Substitution Cipher, and an XOR One Time Pad cipher to get a flag |
| [1.15 Functions](../1.15_functions/README.md)  | Overview on function creation, variable scope, function arguments, and function return values |
| [1.16 Modules](../1.16_modules/README.md)  | How to use reusable code and function definitions that can be imported into other programs |
| [1.17 Unit Tests](../1.17_unit_tests/README.md) | Testing individual units or components of a software application in isolation to ensure they behave as expected. |
| [1.18 File IO](../1.18_file_io/README.md)  | Basics on reading, writing, and modifying data stored in files |
| **[1.19 Competency 3: Wordle](../1.19_competency_3_wordle/README.md)**  | Recreate the sensational game Wordle using python |
| [1.20 Classes and Objects](../1.20_classes_and_objects/README.md)  | Fundamentals on objects and classes. Covers object-oriented programming fundamentals like encapsulation, polymorphism, and inheritance. |
| [1.21 Data Structures](../1.21_data_structures/README.md)  | Coverage of basic data structures like arrays, stacks, binary search trees, graphs, and linked lists. |
| [1.22 Design Patterns](../1.22_design_patterns/README.md) | Introduction to the Factory, Singleton, Adapter, and Bridge design patterns. |
| **[1.23 Competency 4: Ship](../1.23_competency_4_ship/README.md)**  | Implement a Ship class to represent any type of ship, then use the Ship class to represent a fleet.  |
| [1.24 Algorithms](../1.24_algorithms/README.md) | Basics of algorithms, including their characteristics, iterative and recursive algorithms, time and space complexities, and algorithms for searching and sorting. |
| **[1.25 Competency 5: Sorting](../1.25_competency_5_sorting/README.md)**  | Implement bubble sort, selection sort, insertion sort, and merge sort. |
| [1.26 JSON](../1.26_json/README.md)  | In depth explanation of JSON and the `json` Python package |
| **[1.27 Competency 6: Network Analysis](../1.27_competency_6_network_analysis/README.md)**  | Parse a JSON file without the `json` package. Implement Dijkstra's shortest path algorithm. Use both to find the shortest path to a target IP address. |
| [1.28 Exceptions](../1.28_exceptions/README.md)  | In depth explanation of built-in/custom Python Exceptions and `try`/`catch`/`except`/`finally` blocks |
| [1.29 Pytest](../1.29_pytest/README.md)  | Quick intro to `pytest` and how to create test cases |
| **[1.30 Competency 7: Test Eval](../1.30_competency_7_test_eval/README.md)**  | Find bugs in a Python package by writing test cases and documenting them |

If you don't have a Linux Operating System (OS) either as a host, or inside a Virtual Machine (VM), please inform the TRAINO. The Python section of the JQR can be completed in a Windows environment for the most part, but you will need Linux for further sections.

## Python Overview

Python is a high-level, interpreted, interactive and object-oriented scripting language. Python is designed to be highly readable. It uses English keywords frequently whereas the other languages use punctuations. It has fewer syntactical constructions than other languages.

-   **Python is Interpreted** − Python is processed at runtime by the interpreter. You do not need to compile your program before executing it. This is similar to Javascript and Bash.
-   **Python is Interactive** − You can actually sit at a Python prompt and interact with the interpreter directly to write your programs.
-   **Python is Object-Oriented** − Python supports Object-Oriented style or technique of programming that encapsulates code within objects.
-   **Python is a Beginner's Language** − Python is a great language for the beginner-level programmers and supports the development of a wide range of applications from simple text processing to WWW browsers to games.

If you would like more guidance on what the above paragraph really means, and really anything taught in the entire JQR, YouTube videos are highly recommended. If you don't understand it, Google it. Below are two recommendations for inch-deep, mile-wide intros to python:
- [Python explained in 2 Minutes](https://youtu.be/QoIRX37VZpo)
- [Python in 100 Seconds](https://www.youtube.com/watch?v=x7X9w_GIm1s)


## Python Features

Python's features include:
-   **Easy-to-learn** : Python has few keywords, simple structure, and a clearly defined syntax. This allows a student to pick up the language quickly.
-   **Easy-to-maintain** : Python's source code is fairly easy-to-maintain.
-   **A broad standard library** : Python's bulk of the library is very portable and cross-platform compatible on UNIX, Windows, and Macintosh.
-   **Interactive Mode** : Python has support for an interactive mode which allows interactive testing and debugging of snippets of code.
-   **Portable** : Python can run on a wide variety of hardware platforms and has the same interface on all platforms.
-   **Extendable** : You can add low-level modules to the Python interpreter. These modules enable programmers to add to or customize their tools to be more efficient.
-   **Scalable** : Python provides a better structure and support for large programs than shell scripting.
    

Apart from the above-mentioned features, Python has a big list of good features. A, few are listed below :
-   It supports functional and structured programming methods as well as Object-Oriented Programming.
-   It can be used as a scripting language or can be compiled to byte-code for building large applications.
-   It provides very high-level dynamic data types and supports dynamic type checking.
-   It supports automatic garbage collection.
-   It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java.


## Resources
- [Python explained in 2 Minutes](https://youtu.be/QoIRX37VZpo)
- [Python in 100 Seconds](https://www.youtube.com/watch?v=x7X9w_GIm1s)

## Sources

- [Tutorialspoint - Python Overview](https://www.tutorialspoint.com/python3/python_overview.htm)

[Back to README](README.md)
