# Introduction to Section 1: Python


## JQR Section 1 Overview

This is Section 1 in the NCWDG JQR, where new Computer Network Operations (CNO) developers go from a Python Zero to a Python Hero. The section is structured in a way that first teaches students the basics of a specific topic using Markdown files in every folder, known as a **learning** Module. The learning modules then test students' knowledge by having them complete python challenges (`application.py`). After several modules, or topics, their combined use is tested in the form of a **competency** module.

There are 7 total competency modules. Each of them attempts to challenge the student more than the basic application challenges in the learning modules preceding it. All coding challenges are graded using the `test_appliction.py` script in each directory. All the students (and graders) must do to test the code is run `pytest` in the directory. `pytest` setup is covered in [1.01_environment](../1.01_environment/environment.md).

### Table of Contents

|     Section    |   Brief   |
-----------------|-----------|
| [1.00 Overview](../1.00_overview/README.MD)  | Provides the overview for the entire section |
| [1.01 Environment](../1.01_environment/README.md) | Instructs student on `python` and `pytest` setup | 
| [1.02 Basic Syntax](../1.02_basic_syntax/README.md)  | Executing first python code and following basic python rules | 
| [1.03 Variable Types](../1.03_variable_types/README.md)  | Basic python Data Types |
| [1.04 Operators](../1.04_operators/README.md)  | Overview of python Arithmetic, Comparison, Assignment, Bitwise, Membership, Identity, and Logical operator types | 
| [1.05 Conditionals](../1.05_conditionals/README.md) | Intro to python `if`, `elif`, and `else` statements |
| 1.06_loops  | TODO |
| 1.07_debugging  | TODO |
| **1.08_competency_1_fizzbuzz**  | TODO |
| 1.09_numbers  | TODO |
| 1.10_strings  | TODO |
| [1.11 Typecasting](../1.11_typecasting/README.md)  | Overview on getting variables of different types to work together | 
| [1.12 Lists Tuples and Sets](../1.12_lists_tuples_and_sets/README.md)  | Intro to the popular sequence objects and best use cases |
| [1.13 Dictionaries](../1.13_dictionaries/README.md)  | A quick run down on python dictionaries and their most important features |
| **[1.14 Competency 2: Decryption](../1.14_competency_2_decryption/README.md)**  | Tasks the student with implementing a Vigenere cipher, a Substitution Cipher, and an XOR One Time Pad cipher to get a flag |
| [1.15 Functions](../1.15_functions/README.md)  | Overview on function creation, variable scope, function arguments, and function return values |
| 1.16_modules  | TODO |
| 1.17_unit_tests  | TODO |
| 1.18_file_io  | TODO |
| **1.19_competency_3_wordle**  | TODO |
| 1.20_data_structures  | TODO |
| 1.21_algorithms  | TODO |
| **1.22_competency_4_sorting**  | TODO |
| 1.23_classes_and_objects  | TODO |
| **1.24_competency_5_ship**  | TODO |
| 1.25_recursion  | TODO |
| 1.26_json  | TODO |
| **1.27_competency_6a_json_parser**  | TODO |
| 1.28_exceptions  | TODO |
| **1.29_competency_6b_dijkstras**  | TODO |
| 1.30_pytest  | TODO |
| **1.31_competency_7_test_eval**  | TODO |

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
