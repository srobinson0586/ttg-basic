# Complete a large project with nested structs in C

[Back to Overview](../README.md)

JQR Addressed: Demonstrate low-level software engineering capability by designing and implementing a program to meet customer requirements in C.

## Purpose

This competency will give you experience designing and implementing a large
project with nested structs in C.

## Instructions

### .madlib Format:

A .madlib file is stored in text format and contains 5 types of lines. Take a look at [first.madlib](./first.madlib) to see an example. The 5 types of lines are as follows:

1. Category directives:

   Lines beginning with `@` specify the beginning of a list of words
   of a specific category. The name of the category follows the `@`
   immediately and is followed immediately by a `:` and a newline
   character (e.g., `@noun:`). There should not be duplicate category names in a single
   file. The first line in the file must be a category directive.

2. Category instances:

   Non-empty lines immediately following a category directive indicate
   an instance of that category. Each category must have at least 1
   instance.

3. Category terminators:

   Empty lines are used to indicate the end of a category. There must
   be at least 1 empty line following each category.

4. Template directives:

   A template directive consists of the text `*template:` followed
   by a newline. There is exactly 1 template directive per .madlib
   file. The remainder of the file is used as the template for the
   mad lib.

5. Template body:

   Every line after the template directive is treated as part of the
   body of the template. The template body consists of:
   
   - plain text that will be copied directly to the final output
   - variables that will be replaced by a single instance of a specific category
   
   Variables are indicated by the syntax `<category>`, where the
   category name is enclosed in angled brackets (e.g., `<noun>`
   should be replaced by a single instance following a `@noun:`
   category directive earlier in the file).


### .madlib Parser:

A mad lib parser program should read in the .madlib file and output
text that matches the template, where all variables have been
replaced by instances of the specified category. The following functionality should also be met:

1. Be able to handle arbitrarily long lines in the input file. This probably
   means using `getline()` instead of `fgets()`.

2. Create a structure that can represent an arbitrary category (e.g., noun,
   adjective, verb, etc).

3. Store all categories found in the template in a dynamically reallocated
   array (i.e, an array of contiguous elements in memory, which you reallocate
   as needed as it grows).

4. Create a structure that can represent an instance of an arbitrary
   category.

5. Each category structure should contain a circularly linked list of the
   instances it contains.

6. To choose a random instance of a particular category, you should choose
   a random number and then iterate through the circularly linked list of the
   appropriate category that many steps.

7. Write a Makefile for your project. Your project should compile and run
   with no compiler warnings and no Valgrind errors.

If the input file contains an error, the parser should detect it,
output a helpful error message, and abort parsing. The following
errors should be detected:

1. Malformed line (e.g., a line that does not fall into one of the
   categories listed above).

2. Category with no instances.

3. Duplicate category names.

4. Missing template directive.

5. Nonexistent category referenced by variable in template.

[Back to Overview](../README.md)