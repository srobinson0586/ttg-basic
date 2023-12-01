# Python Algorithms

[Back to README](README.md)

> Algorithms are a key concept in computer science that extends beyond a single programming language. In reality, it takes more than a single day to learn about algorithms. Universities typically require a quarter or a semester long class on algorithms as a requirement to graduate with a computer science degree. However, this section aims to familiarize newer developers with the core ideas of algorithms so they can complete the JQR and understand more of what a Google search might yield. There will *always* be more to learn about algorithms and what they have to offer.

As developers, it is our job to write code efficiently and effectively to solve complex problems. We typically accomplish this by analyzing problems to create step-by-step instructions on how to always get our desired output from given input. During the process of creating step-by-step instructions to solve problems, we are formulating an algorithm.

An **algorithm** is a step-by-step, systematic procedure or set of instructions used to perform a specific task or solve a problem. It is a *well-defined and unambiguous sequence of actions* that takes one or more inputs and produces one or more outputs based on a defined set of rules or logic.

Key characteristics of algorithms include:

- **Input**: An algorithm takes zero or more inputs, which are the data or variables required to perform the task or solve the problem.

- **Output**: An algorithm produces one or more outputs, which are the results or solutions generated after performing the steps.

- **Definiteness**: An algorithm's steps should be well-defined and clear, leaving no room for ambiguity or interpretation.

- **Finiteness**: An algorithm should have a finite number of steps, meaning that it should eventually terminate and not run indefinitely.

- **Effectiveness**: An algorithm should be feasible and practical, meaning that it can be implemented in a real-world scenario using available resources.

- **Generality**: An algorithm should be applicable to a broader set of inputs, not just limited to specific cases.

Algorithms are essential in computer programming because they provide a precise and structured way to approach problems and tasks. They serve as building blocks for writing code and designing software solutions. Programmers use algorithms to develop efficient and optimized solutions for various computational challenges.

Algorithms can be expressed in various forms, including natural language, pseudo-code, flowcharts, or programming languages like Python, C++, Java, etc. They are used in various domains, including data processing, searching and sorting, mathematical calculations, artificial intelligence, and more.

A very simple example of an algorithm is a function that returns the sum of two numbers. Take a look at the following:

```python
def addNumbers(x, y):
    result = x + y
    return result
```

This function takes **input** (`x` and `y`), has an **output** (`result`), has a **finite** number of **definite** steps, is **effective**, and **is generalized for a broader set of inputs** through the abstraction of its inputs `x` and `y`. In summary, it has all of the characteristics that an algorithm should have.

## Iterative and Recursive Algorithms

 **Iterative** and **recursive** algorithms are two different approaches to solve problems in computer programming. Both approaches involve repeating a set of instructions or steps to achieve a desired outcome, but they differ in their implementation and control flow. All algorithms can be classified as being iterative, recursive, or both.

### Iterative Algorithm Characteristics

In iterative algorithms, a problem is solved using loops or repeated instructions. The loop iterates over a range of values or a data structure to process each element step by step until the desired result is achieved.

- Iterative algorithms use explicit control flow, and the iteration can be done using various loop structures, such as `for` loops or `while` loops.

- Each iteration processes a specific element or a subset of data and updates variables or accumulators accordingly to reach the final result.

- Iterative algorithms are often used when the problem can be divided into smaller, *incremental* steps that can be processed *sequentially*.

### Recursive Algorithm Characteristics

In recursive algorithms, the problem is solved by breaking it down into smaller, similar subproblems. Each subproblem is solved using the same algorithm (i.e., the recursive algorithm calls on itself to solve the problem) until it reaches a **base case**, which is a simple problem that can be directly solved. A base case is the stopping point for a recursive algorithm which prevents it from calling itself infinitely.

- The algorithm calls itself (recursively) to solve the subproblems and combines their solutions to obtain the solution to the original problem.

 - Recursive algorithms use implicit control flow, as the function calls itself, leading to a chain of function calls until the base case is reached.

- Recursive algorithms are often used when the problem has a *recursive structure* or can be expressed in terms of smaller, repetitive instances of the same problem.

### Example

Below are two algorithms for finding the factorial of a number `n`. One algorithm uses an iterative approach while the other uses a recursive approach.

#### Iterative Approach

```python
def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

In the iterative approach, the `factorial_iterative()` function calculates the factorial of a given non-negative integer `n`. It uses a `for` loop to multiply all integers from 1 to `n` together, updating the `result` variable at each iteration.

#### Recursive Approach

```python
def factorial_recursive(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    # Base case: this is checked every time to see if the algorithm has reached its stopping point
    if n == 0 or n == 1:
        return 1

    # Recursive step: if the algorithm has not reached the base case, then it places another call to itself
    return n * factorial_recursive(n - 1)
```

In the recursive approach, the  `factorial_recursive()` function calculates the factorial by breaking the problem down into smaller subproblems. If `n` is 0 or 1, it returns 1 (base case). Otherwise, it multiplies `n` with the factorial of `n-1` (recursive step), until it reaches the base case.

> Each call to a function uses computer memory, which is finite. So if some program is using a recursive function that never reaches a base case (or has no base case), the recursion carries on until the computer runs out of memory to set up new function calls, at which point the program will crash. The classification of this error would be a 'stack overflow'.

* * * 

Both of these functions will yield the same results for some number `n`. You can play around with them by copying and pasting the code into your own Python script.

It can be difficult to understand how recursion works by simply looking at recursive code. It may be worthwhile to use the recursion visualization tool at https://recursion.vercel.app/ to understand the recursion trees that are created for different problems.

## Complexities

When we write and use algorithms in our programs, we want them to perform as quickly and efficiently as possible. This means using the least amount of available processing power and memory resources. We measure the performance of algorithms through **complexities**.

Algorithm complexities, also known as **time** and **space** complexities, are measurements that describe how the performance of an algorithm scales with the size of its input. They help analyze and compare different algorithms in terms of their efficiency and resource usage. The quantifier that is most commonly used is **Big O**, which describes an algorithm's performance in the worst-case scenario.

#### Time Complexity:

- Time complexity measures the amount of time an algorithm takes to run as a function of the size of the input.
- It quantifies how the number of operations performed by the algorithm grows with the size of the input.
- Time complexity is typically expressed using the **big O** notation **O(*f(n)*)**, where ***f(n)*** represents an upper bound on the number of operations, and ***n*** is the size of the input.
- Common time complexity classes include **O(*1*)** (constant time), **O(*log(n)*)** (logarithmic time), **O(*n*)** (linear time), **O(*n\*log(n)*)** (linearithmic time), **O(*n^2*)** (quadratic time), **O(*2^n*)** (exponential time), etc.

#### Space Complexity:

- Space complexity measures the amount of memory or storage an algorithm uses as a function of the size of the input.
- It quantifies how the memory requirements of the algorithm grow with the size of the input.
- Space complexity is also typically expressed using **big O** notation, where the focus is on the additional memory used beyond the input data.
- Common space complexity classes include **O(*1*)** (constant space), **O(*n*)** (linear space), **O(*n^2*)** (quadratic space), **O(*log(n)*)** (logarithmic space), etc.

* * *

The image below illustrates how the number of operations required (y-axis) of a function scales with the number of inputs (x-axis) for an algorithm.

![time-complexity-examples](.img/time-complexity-examples.png)

For a relatively small number of inputs, the time/space needed for an algorithm to run is less significant, but can quickly increase for some complexity classes as the total number of inputs grows.

From best to worst, the most common **Big O** time and space complexities are:

1. **O(*1*)**: Constant time/space - the performance of the algorithm remains constant and is unaffected by input size.
2. **O(*log(n)*)**: Logarithmic time/space - the performance of the algorithm scales logarithmically as the input grows
3. **O(*n*)**: Linear time/space - the performance of the algorithm scales linearly with input size.
4. **O(*n\*log(n)*)**: Linearithmic time/space - the algorithm's performance is between linear and quadratic time.
5. **O(*n^2*)**: Quadratic time/space - the performance of the algorithm scales quadratically with input size.
6. **O(*n^k*)**: Polynomial time/space - the performance of the algorithm scales polynomially with input size, where *k* is a constant.
7. **O(*2^n*)**: Exponential time/space - the performance of the algorithm scales exponentially with input size.
8. **O(*n!*)**: Factorial time/space - the performance of the algorithm scales as a factorial of the input size.

Analyzing algorithm complexities is crucial for determining the efficiency and scalability of algorithms. It helps in choosing the most appropriate algorithm for specific tasks and understanding how an algorithm will perform as the input size increases. Generally, algorithms with lower time and space complexities are considered more efficient, as they require fewer resources and complete their tasks faster, especially for large inputs. However, achieving low complexity may involve trade-offs with readability and code complexity, making it essential to find a balance between efficiency and maintainability.

## Sorting and Searching Algorithms

Sorting and searching algorithms are fundamental concepts in computer science and data analysis that involve organizing and retrieving data in an efficient and systematic manner. Both types of algorithms are crucial for various applications and tasks, including information retrieval, data analysis, and optimization problems.

### Sorting Algorithms
Sorting algorithms are used to arrange elements in a specific order, often in ascending or descending order. The primary objective of a sorting algorithm is to rearrange data in a way that makes it easier to search, process, or analyze. For example, it would be much easier to find a name on a roster of 10000 people if it was sorted in alphabetical (ascending) order.

Common sorting algorithms include:

- **Bubble Sort**: A simple iterative sorting algorithm that repeatedly compares adjacent elements and swaps them if they are in the wrong order. Bubble sort has a time complexity of **O(*n^2*)** and is not recommended for large datasets due to its inefficiency.

- **Merge Sort**: A sorting algorithm that recursively divides the data into halves, sorts them, and then merges the sorted halves back together. Merge sort has a time complexity of **O(*n\*log(n)*)** and is widely used for efficient sorting.

- **Quick Sort**: A sorting algorithm that partitions the data into two sub-arrays around a pivot element and recursively sorts the sub-arrays. Quick sort has an average time complexity of **O(*n\*log(n)*)** but can degrade to **O(*n^2*)** in a worst-case scenario.

- **Insertion Sort**: An iterative algorithm that builds the sorted array one element at a time by repeatedly inserting elements into their correct positions. Insertion sort has a time complexity of **O(*n^2*)** but can be efficient for small datasets.

> Python has a built-in sorting function called `sorted()`. Behind the scenes, `sorted()` uses the *Timsort* sorting algorithm, which is a combination of *Merge Sort* and *Insertion Sort*.


### Searching Algorithms

Searching algorithms are used to find the location or presence of a specific target value within a dataset. The target value can be an element in an array, a key in a dictionary, or a record in a database, among other data structures. The main goal of a searching algorithm is to locate the target value and determine its position within the data. Searching for data becomes an easier process when we know the data is sorted (again, think of the roster example).

Common searching algorithms include:

- **Linear Search**: This simple algorithm sequentially checks each element in the data until the target value is found. Linear search works on unsorted data and has a time complexity of **O(*n*)**, where ***n*** is the number of elements in the data. Linear searches are typically implemented using `for` or `while` loops.

- **Binary Search**: Binary search is a more efficient algorithm that works on sorted data. It repeatedly divides the data into halves and compares the target value with the middle element, discarding the half of the data where the target cannot be. Binary search has a time complexity of **O(*log(n)*)**, making it significantly faster than linear search for large datasets. A binary search algorithm can usually be implemented with iteration or recursion.

- **Hashing**: Hashing is a technique used in hash tables to quickly access data based on a *unique* key. Hashing algorithms convert the key into an index, allowing for **O(*1*)** constant-time access to the desired data in an ideal scenario. When you access a Python dictionary's value using a key, hashing takes place behind the scenes to access the value in **O(*1*)** constant time.

* * *

Both searching and sorting algorithms are essential for various applications, and their selection depends on the specific requirements and characteristics of the data being processed. Efficient searching and sorting algorithms play a crucial role in optimizing performance and improving the overall efficiency of algorithms and data processing tasks.

## Resources

#### Sorting Animations

Click [here](https://www.toptal.com/developers/sorting-algorithms) to view animations of the most common algorithms for sorting.

- Clicking on 'Play All' will play each animation side-by-side so you can observe and compare the time that it takes for each algorithm to complete for input that is randomized, nearly sorted, reverse sorted, and has few unique values. 
- There is also a button to change the size of the input so you can observe how each algorithm performs when there is more or less input. 
- It may be worthwhile to compare two algorithms represented on this page (i.e., bubble sort and heap sort). What are the big Os of each algorithm that you compared? Are the time differences clear for large inputs?

#### Examples and Pseudocode for Common Sorting Algorithms

Among other online resources, these may come in useful for the next competency as they illustrate an example of each algorithm and provide pseudocode that can be referenced for implementation in most programming languages.

- [TutorialsPoint | Bubble sort](https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm)
- [TutorialsPoint | Insertion sort](https://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm)
- [TutorialsPoint | Selection sort](https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm)
- [TutorialsPoint | Merge sort](https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm)

## Sources
- [Big-O Cheat Sheet](https://www.bigocheatsheet.com/)

[Back to README](README.md)
