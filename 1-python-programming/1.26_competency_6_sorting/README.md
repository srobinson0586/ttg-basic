# Python Competency 6 - Sorting

[Back to OVERVIEW](../README.md)

Code: [`sorting.py`](./sorting.py) 

## Objectives

This competency will help you apply the knowledge you have learned from previous competencies and recent modules. After completing this competency, you should be comfortable with:

- [Data Structures](../1.20_data_structures/README.md)
- [Algorithms](../1.21_algorithms/README.md)


## Implementation of Sorting Algorithms

The objective of this module is to implement the functions `bubble_sort`, `insertion_sort`, `selection_sort`, and `merge_sort`. Each of these is a sorting algorithm that is used to structure data in ascending or descending order. It may be useful to refer to the webpages linked at the bottom of this file for pseudocode and examples of how each algorithm works. A brief description of each function is below:

**`bubble_sort`**:
- Represents the Bubble Sort algorithm, which is an iterative sorting algorithm that has a worst-case time complexity of **O(*n^2*)** and constant **O(*1*)** space complexity. 
- Bubble sort works by comparing adjacent elements in a list and swapping them if they are out of order. 
- Bubble sort can be useful on small datasets that are sorted or nearly sorted, but quickly becomes inefficient as the size of input grows.

**`insertion_sort`**:
- Represents the Insertion Sort algorithm, which is an iterative sorting algorithm with a worst case time complexity of **O(*n^2*)** and constant **O(*1*)** space complexity. 
- The algorithm works by dividing the input list into two parts: a sorted subarray and an unsorted subarray. 
- It iteratively picks elements from the unsorted subarray and inserts them into their correct positions in the sorted subarray; this process is repeated until the entire list becomes sorted. 
- Like Bubble sort, insertion sort has fair performance for small inputs, but can become inefficient for larger inputs.

**`selection_sort`**:
- Represents the Selection Sort algorithm, which is an iterative sorting algorithm with a worst case time complexity of **O(*n^2*)** and constant **O(*1*)** space complexity. 
- The algorithm divides the input list into two subarrays: a sorted subarray and an unsorted subarray. 
- It iteratively finds the minimum (or maximum) element from the unsorted subarray and places it at the correct position in the sorted subarray and repeats the process until the entire list becomes sorted. 
- Selection sort is inefficient even with small input sizes, but the algorithm itself is simple to understand and is typically implemented for practicing algorithm implementation.

**`merge_sort`**:
- Represents Merge Sort, which is a recursive sorting algorithm with a worst case time complexity of **O(*n\*log(n)*)** and a worst-case space complexity of **O(*n*)**. 
- The algorithm works by dividing the input list into smaller sublists, sorting them individually, and then merging the sorted sublists to produce the final sorted list. 
- The algorithm continuously divides the list in half until it reaches individual elements (sublists of size 1), and then merges them back together in a sorted order. 
- Merge sort is highly efficient algorithm which performs well with large inputs.

Each of these functions will be tested with using several lists as inputs. You may wish to test your functions on your own inputs before running `pytest`.

## Resources

Many implementations of these algorithms exist, but the following links are good starting point before searching elsewhere:

- [TutorialsPoint | Bubble sort](https://www.tutorialspoint.com/data_structures_algorithms/bubble_sort_algorithm.htm)
- [TutorialsPoint | Insertion sort](https://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm)
- [TutorialsPoint | Selection sort](https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm)
- [TutorialsPoint | Merge sort](https://www.tutorialspoint.com/data_structures_algorithms/merge_sort_algorithm.htm)

## Assignment
- [ ] Implement the four functions in [`sorting.py`](./sorting.py) with the functionality described above (`bubble_sort()`, `insertion_sort()`, `selection_sort()`, and `merge_sort()`)
- [ ] OPTIONAL: Implement `test()` in [`sorting.py`](./sorting.py) to test the functionality of your four sorting functions. This is especially helpful if you have errors in the next step. 
- [ ] Run `pytest` in your current directory.  If there are no errors, you completed this section.

[Back to OVERVIEW](../README.md)