# Introduction to Merge Sort 

## Overview 

### Divide and Conquer Algorithm
- Merge sort uses divide and conquer algorithm to break down a problem into multiple subproblems recursively until they becore simple to solve. 

- Solutions are then combined to solve original problem. 

- Merge sort has O(n * log(n)) running time (which is the optimal running time for comparison based algorithms)


### Explanation:

- Divide: The array is recursively divided into two halves until each sub-array contains a single element.
- Merge: The sorted halves are then merged back together in the correct order.
- Base Case: When the array has only one element (i.e., len(arr) == 1), it’s considered sorted.


## General principle of merge sort 

1. Split array in half 
2. Call Merge sort on each half to sort them recursively
3. Merge both sorted halves into one sorted array


