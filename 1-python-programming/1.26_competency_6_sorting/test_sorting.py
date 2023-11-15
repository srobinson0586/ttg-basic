#!/bin/python
# Python Sorting - Pytest Suite
import sorting
import random

sample1 = ["is", "this", "a", "sorted", "list"]
sample2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sample3 = ["c", "c", "c", "b", "b", "b", "a", "a", "a"]
sample4 = [random.randint(0, 100) for _ in range(100)]

sorted_1 = sorted(sample1)
sorted_2 = sorted(sample2)
sorted_3 = sorted(sample3)
sorted_4 = sorted(sample4)
        
def test_bubble():
    assert sample1 != sorted_1, "See link: https://stackoverflow.com/a/38134344"
    bubble_rv = sorting.bubble_sort(sample1)
    assert sorted_1 is not bubble_rv, "See link: https://stackoverflow.com/a/38134344"
    assert sorted_1 == bubble_rv, "bubble_sort incorrectly sorted on the the first test case (input: a list of strings)"
    
    assert sample2 != sorted_2, "See link: https://stackoverflow.com/a/38134344"
    bubble_rv = sorting.bubble_sort(sample2)
    assert sorted_2 is not bubble_rv, "See link: https://stackoverflow.com/a/38134344"
    assert sorted_2 == bubble_rv, "bubble_sort incorrectly sorted on the the second test case (input: a list that was already sorted)"
    
    assert sample3 != sorted_3, "See link: https://stackoverflow.com/a/38134344"
    bubble_rv = sorting.bubble_sort(sample3)
    assert sorted_3 == bubble_rv, "bubble_sort incorrectly sorted on the the third test case (input: a reverse sorted list of strings with duplicates)"
    assert sorted_2 is not bubble_rv, "See link: https://stackoverflow.com/a/38134344"
    
    assert sample4 != sorted_4, "See link: https://stackoverflow.com/a/38134344"
    bubble_rv = sorting.bubble_sort(sample4)
    assert sorted_4 == bubble_rv, "bubble_sort incorrectly sorted on the the fourth test case (input: a list of 100 numbers)"
    assert sorted_4 is not bubble_rv, "See link: https://stackoverflow.com/a/38134344"

def test_insertion():
    assert sample1 != sorted_1, "See link: https://stackoverflow.com/a/38134344"
    insert_rv = sorting.insertion_sort(sample1)
    assert sorted_1 == insert_rv, "insertion_sort incorrectly sorted on the the first test case (input: a list of strings)"
    assert sorted_1 is not insert_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample2 != sorted_2, "See link: https://stackoverflow.com/a/38134344"
    insert_rv = sorting.insertion_sort(sample2)
    assert sorted_2 == insert_rv, "insertion_sort incorrectly sorted on the the second test case (input: a list that was already sorted)"
    assert sorted_2 is not insert_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample3 != sorted_3, "See link: https://stackoverflow.com/a/38134344"
    insert_rv = sorting.insertion_sort(sample3)
    assert sorted_3 == insert_rv, "insertion_sort incorrectly sorted on the the third test case (input: a reverse sorted list of strings with duplicates)"
    assert sorted_3 is not insert_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample4 != sorted_4, "See link: https://stackoverflow.com/a/38134344"
    insert_rv = sorting.insertion_sort(sample4)
    assert sorted_4 == insert_rv, "insertion_sort incorrectly sorted on the the fourth test case (input: a list of 100 numbers)"
    assert sorted_4 is not insert_rv, "See link: https://stackoverflow.com/a/38134344"

def test_selection():
    assert sample1 != sorted_1, "See link: https://stackoverflow.com/a/38134344"
    select_rv = sorting.bubble_sort(sample1)
    assert sorted_1 == select_rv, "selection_sort incorrectly sorted on the the first test case (input: a list of strings)"
    assert sorted_1 is not select_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample2 != sorted_2, "See link: https://stackoverflow.com/a/38134344"
    select_rv = sorting.bubble_sort(sample2)
    assert sorted_2 == select_rv, "selection_sort incorrectly sorted on the the second test case (input: a list that was already sorted)"
    assert sorted_2 is not select_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample3 != sorted_3, "See link: https://stackoverflow.com/a/38134344"
    select_rv = sorting.bubble_sort(sample3)
    assert sorted_3 == select_rv, "selection_sort incorrectly sorted on the the third test case (input: a reverse sorted list of strings with duplicates)"
    assert sorted_3 is not select_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample4 != sorted_4, "See link: https://stackoverflow.com/a/38134344"
    select_rv = sorting.bubble_sort(sample4)
    assert sorted_4 == select_rv, "selection_sort incorrectly sorted on the the fourth test case (input: a list of 100 numbers)"
    assert sorted_4 is not select_rv, "See link: https://stackoverflow.com/a/38134344"

def test_merge():
    assert sample1 != sorted_1, "See link: https://stackoverflow.com/a/38134344"
    merge_rv = sorting.bubble_sort(sample1)
    assert sorted_1 == merge_rv, "merge_sort incorrectly sorted on the the first test case (input: a list of strings)"
    assert sorted_1 is not merge_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample2 != sorted_2, "See link: https://stackoverflow.com/a/38134344"
    merge_rv = sorting.bubble_sort(sample2)
    assert sorted_2 == merge_rv, "merge_sort incorrectly sorted on the the second test case (input: a list that was already sorted)"
    assert sorted_2 is not merge_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample3 != sorted_3, "See link: https://stackoverflow.com/a/38134344"
    merge_rv = sorting.bubble_sort(sample3)
    assert sorted_3 == merge_rv, "merge_sort incorrectly sorted on the the third test case (input: a reverse sorted list of strings with duplicates)"
    assert sorted_3 is not merge_rv, "See link: https://stackoverflow.com/a/38134344"

    assert sample4 != sorted_4, "See link: https://stackoverflow.com/a/38134344"
    merge_rv = sorting.bubble_sort(sample4)
    assert sorted_4 == merge_rv, "merge_sort incorrectly sorted on the the fourth test case (input: a list of 100 numbers)"
    assert sorted_4 is not merge_rv, "See link: https://stackoverflow.com/a/38134344"